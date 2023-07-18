from PySide2.QtWidgets import QMainWindow
from jiwoon.gazu_api.view.UI.asset_ui_2 import Ui_MainWindow


class UI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
