import sys
from PySide2 import QtWidgets, QtCore
from nukitsu.gazu_api.view.UI.nuki import Nuki
from nukitsu.gazu_api.view.UI.upload_nuki import Upload_Nuki
from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget, QPushButton, QVBoxLayout

# class foo(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__()
#         self.Init()
#     def Init(self):
#         nuki_app = Nuki()


if __name__ == "__main__":
    # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    apps = Upload_Nuki()
    sys.exit(app.exec_())