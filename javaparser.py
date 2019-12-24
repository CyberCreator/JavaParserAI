import json
import os
import pathlib
import sys
from PyQt5 import QtWidgets, QtCore
from typing import List
import view
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

from util import initialization_subject_dir, get_list_projects, add_project, delete_project, PKG_DIR, project_analysis
from util.config import NAME_CONFIG_PROJECT_FILE, SUBJECT_DIR_NAME
from util.signals import signal


class MainWin(QtWidgets.QMainWindow, view.Ui_MainWindow):
    A: List = list()
    I: List = list()
    list_projects: List = list()
    current_project: str = str()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._translate: QtCore = QtCore.QCoreApplication.translate
        self.main_render()

        # signals
        self.treeWidget.itemClicked.connect(self.on_item_clicked_menu)
        self.actionAdd_project.triggered.connect(lambda: add_project(self))
        self.actionDelete_this_project.triggered.connect(lambda: delete_project(self, self.current_project))
        signal.update_menu.connect(self.update_left_menu)
        signal.update_coord.connect(self.update_coord)

    def main_render(self):
        self.addToolBar(NavigationToolbar(self.widget.canvas, self))
        self.update_graph()
        self.update_left_menu()

    def update_left_menu(self):
        self.treeWidget.clear()
        self.list_projects = get_list_projects()
        if not(self.current_project in self.list_projects):
            self.current_project = str()
        for i, item in enumerate(self.list_projects):
            QtWidgets.QTreeWidgetItem(self.treeWidget)
            self.treeWidget.topLevelItem(i).setText(0, self._translate("MainWindow", item))

    def update_coord(self):
        AI = pathlib.Path(os.path.join(PKG_DIR, SUBJECT_DIR_NAME, self.current_project, NAME_CONFIG_PROJECT_FILE))
        self.A = json.loads(AI.read_text())['A']
        self.I = json.loads(AI.read_text())['I']
        self.update_graph()

    @QtCore.pyqtSlot(QtWidgets.QTreeWidgetItem, int)
    def on_item_clicked_menu(self, it, col):
        self.current_project = it.text(col)
        if NAME_CONFIG_PROJECT_FILE in os.listdir(os.path.join(PKG_DIR, SUBJECT_DIR_NAME, self.current_project)):
            self.update_coord()
            return
        project_analysis(self, self.current_project)

    def update_graph(self):
        self.widget.canvas.axes.clear()
        self.widget.canvas.axes.plot(self.A, self.I, 'ro')
        self.widget.canvas.axes.set_title(self.current_project)
        self.widget.canvas.draw()


def main():
    app: QtWidgets = QtWidgets.QApplication(sys.argv)
    window: MainWin = MainWin()
    window.show()
    app.exec_()


if __name__ == '__main__':
    initialization_subject_dir()
    main()
