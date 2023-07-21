import os

from PySide2 import QtCore, QtUiTools
from PySide2.QtWidgets import QMainWindow

from nuki.jiwoon.gazu_api.view.UI.nuki_main_widget import Ui_Nuki


class MainUI(QMainWindow, Ui_Nuki):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # UI
        self.shot_list.setStyleSheet('background-color: transparent')
