from nukitsu.gazu_api.view.UI.nuki import Nuki
from PySide2.QtWidgets import QMainWindow


class NukiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        Nuki()
