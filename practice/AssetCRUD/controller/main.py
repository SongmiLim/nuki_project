from PySide2.QtWidgets import QApplication, QMainWindow
from practice.AssetCRUD.view.asset_manage_view import MainWindow


if __name__ == "__main__":

    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()