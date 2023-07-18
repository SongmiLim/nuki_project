import os

from PySide2 import QtCore, QtUiTools
from PySide2.QtWidgets import QMainWindow

from jiwoon.gazu_api.view.UI.asset_ui_2 import Ui_MainWindow


class MainUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
