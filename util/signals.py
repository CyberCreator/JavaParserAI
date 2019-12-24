from PyQt5.QtCore import pyqtSignal, QObject
from typing import List


__ALL__: List = ['signal']


class __Signal(QObject):
    waiting = pyqtSignal()
    update_menu = pyqtSignal()
    update_coord = pyqtSignal()


signal: __Signal = __Signal()
