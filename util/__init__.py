import json
import os
import pathlib
import shutil
import threading
from typing import List, Dict
from PyQt5 import QtWidgets, QtCore, QtSvg
from PyQt5.QtWidgets import QFileDialog

import waiting
from util.config import SUBJECT_DIR_NAME, DIALOG_OK, NAME_CONFIG_PROJECT_FILE
from util.signals import signal


class Waiting(QtWidgets.QDialog, waiting.Ui_Dialog):
    def __init__(self, root, func):
        super(Waiting, self).__init__(root)
        self.setupUi(self)
        self.func = func
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.svgItem = QtSvg.QGraphicsSvgItem(os.path.join(PKG_DIR, 'img', 'waiting.svg'))
        self.graphicsView.setScene(QtWidgets.QGraphicsScene())
        self.graphicsView.scene().addItem(self.svgItem)
        signal.waiting.connect(self.close)
        self.main_render()

    def main_render(self):
        # Initialize the window launch only after the function is launched. fix later.
        self.func()


def run_waiting(self, target=None):
    """
    waiting method
    example:

    method call
    1) self.parent.waiting(self, target=self.push_comm)
    signal for exit waiting dialog in target function
    2) signal.waiting.emit()
    """
    run_wait = Waiting(self, target)
    run_wait.exec_()


def initialization_subject_dir() -> None:
    os.makedirs(os.path.join(PKG_DIR, SUBJECT_DIR_NAME), exist_ok=True)


def get_list_projects() -> List:
    return os.listdir(os.path.join(PKG_DIR, SUBJECT_DIR_NAME))


def run_thread(is_daemon=True):
    """
    Run function in another thread
    """
    def decorator_maker(func):
        def wrapper(*args, **kwargs):
            thread = threading.Thread(target=func, args=args, kwargs=kwargs)
            thread.daemon = is_daemon
            thread.start()

        return wrapper
    return decorator_maker


def msg_question(self, set_text, info_text=None, title='Question') -> int:
    msg_box = QtWidgets.QMessageBox(self)
    msg_box.setIcon(QtWidgets.QMessageBox.Question)
    msg_box.setWindowTitle(title)
    msg_box.setText(set_text)
    msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
    if info_text:
        msg_box.setInformativeText(info_text)
    return msg_box.exec_()


def msg_info(self, set_text, info_text=None, title='Information') -> int:
    msg_box = QtWidgets.QMessageBox(self)
    msg_box.setIcon(QtWidgets.QMessageBox.Information)
    msg_box.setWindowTitle(title)
    msg_box.setText(set_text)
    if info_text:
        msg_box.setInformativeText(info_text)
    return msg_box.exec_()


def get_folder_path_dialog(self, dialog_name: str = 'Select folder') -> str:
    folder_path: str = QFileDialog.getExistingDirectory(self, dialog_name, '/home', QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
    return folder_path


def add_project(self):
    name: str = str()
    folder_path: str = get_folder_path_dialog(self)

    if folder_path:
        name = os.path.basename(folder_path)

    if name in get_list_projects():
        return msg_info(self, 'Unable to copy project.', 'A project with this name has already been uploaded.', name)

    if folder_path:
        run_waiting(self, lambda: copy_tree(folder_path, os.path.join(PKG_DIR, SUBJECT_DIR_NAME, name)))


def delete_project(self, project_name: str) -> None:
    if not project_name:
        msg_info(self, 'No project selected.', 'Please select a project to delete.')
        return

    dialog_result: int = msg_question(self, 'Are you sure you want to delete the project?', project_name)
    if dialog_result == DIALOG_OK:
        run_waiting(self, lambda: __delete_project(project_name))


def project_analysis(self, project_name: str):
    dialog_result: int = msg_question(self, 'This project does not exist in the database.',
                                      'Perform parsing and display on a graph?', project_name)
    if dialog_result == DIALOG_OK:
        run_waiting(self, lambda: __project_analysis(project_name))


@run_thread()
def __project_analysis(project_name: str):
    path_dir: str = os.path.join(PKG_DIR, SUBJECT_DIR_NAME, project_name)

    package: Dict = dict()
    list_class_name: List = list()

    for dir_info in os.walk(path_dir):
        for file_name in dir_info[2]:
            full_file_path: str = os.path.join(dir_info[0], file_name)

            if full_file_path.endswith('.java'):

                try:
                    with open(full_file_path) as file:
                        package_defined: bool = False
                        abstract_check: bool = False

                        for line_file in file:

                            if not package_defined and line_file.startswith('package'):
                                package_name = line_file[8:-2].replace('.', '_') #  The key in the dictionary must not have dots.
                                if not (package_name in package):
                                    package[package_name]: Dict = {
                                        'all_class': list(),
                                        'abstract_count': 0,
                                        'external': 0,
                                        'internal': 0
                                    }
                                list_class_name.append(os.path.basename(full_file_path))
                                package[package_name]['all_class'].append(full_file_path)
                                package_defined = package_name

                            if package_defined and not abstract_check:
                                # This piece of code needs to be taken out of the loop, but I decided to leave it here,
                                # because if checking the 'abstract class' in file.read () is not enough, I will need
                                # read the file line by line, and this can only be done inside the 'For' loop.
                                if 'abstract class' in file.read():
                                    package[package_name]['abstract_count'] += 1
                                abstract_check = True

                except UnicodeDecodeError as e:
                    print(e)

    A: List = list()
    I: List = list()

    print(f'Total Modules Found: {len(package)}')
    for package_name in package:
        print(f' [{package_name}] List of all package classes = {len(package[package_name]["all_class"])}')
        print(f' [{package_name}] List of package abst classes = {package[package_name]["abstract_count"]}')
        A.append(float(package[package_name]['abstract_count'] / len(package[package_name]['all_class'])))

        for class_path in package[package_name]['all_class']:
            try:
                with open(class_path) as file:
                    for file_line in file:
                        buf: bool = False
                        if file_line.startswith('import'):
                            full_import = file_line[7:-2]
                            class_name_import = full_import.split('.')[-1]
                            received_package_name = full_import[:-(len(class_name_import) + 1)].replace('.', '_')

                            if received_package_name in package:
                                for class_name_this_package in package[received_package_name]['all_class']:
                                    if os.path.basename(class_name_this_package)[:-5] == class_name_import:
                                        package[received_package_name]['internal'] += 1
                                        buf = True
                                        break

                            if not buf:
                                package[package_name]['external'] += 1

            except UnicodeDecodeError as e:
                pass

    for package_name in package:
        try:
            one = package[package_name]['external']
            two = package[package_name]['external'] + package[package_name]['internal']
            I.append(float(one / two))
        except ZeroDivisionError as e:
            I.append(0.0)

    coord: Dict = {
        'A': A,
        'I': I,
    }
    json_coord: json = json.dumps(coord)
    pathlib.Path(os.path.join(PKG_DIR, SUBJECT_DIR_NAME, project_name, NAME_CONFIG_PROJECT_FILE)).write_text(json_coord, encoding="utf-8")

    signal.update_coord.emit()
    signal.waiting.emit()


@run_thread()
def __delete_project(folder_name: str):
    shutil.rmtree(os.path.join(PKG_DIR, SUBJECT_DIR_NAME, folder_name))
    signal.update_menu.emit()
    signal.waiting.emit()


@run_thread()
def copy_tree(input_folder: str, output_folder: str):
    shutil.copytree(input_folder, output_folder)
    signal.update_menu.emit()
    signal.waiting.emit()


PKG_DIR: str = os.path.abspath(os.path.join(__file__, "../.."))  # absolute path to the package folder
