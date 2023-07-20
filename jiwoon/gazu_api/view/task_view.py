import os

from PySide2 import QtCore, QtUiTools
from PySide2.QtWidgets import QMainWindow, QListView

from jiwoon.gazu_api.view.UI.nuki_main_widget import Ui_Nuki


class MainUI(QMainWindow, Ui_Nuki):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # UI
        self.shot_list.setStyleSheet('background-color: transparent')
        self.shot_list.setViewMode(QListView.IconMode)
        self.shot_list.setIconSize(QtCore.QSize(400, 200))
        # self.shot_list.setUniformItemSizes(True)
        self.shot_list.setGridSize(QtCore.QSize(180, 140))
        # self.shot_list.setMovement(QListView.Static)
