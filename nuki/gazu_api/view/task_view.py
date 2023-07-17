from PySide2.QtWidgets import QMainWindow
from gazu_api.view.UI.asset_ui_2 import Ui_MainWindow


class TaskUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
