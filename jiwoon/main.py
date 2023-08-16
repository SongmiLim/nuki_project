import sys
from PySide2 import QtWidgets, QtCore
from jiwoon.gazu_api.view.UI.nuki import Nuki
from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget, QPushButton, QVBoxLayout

class foo(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.Init()
    def Init(self):
        nuki_app = Nuki()
#

if __name__ == "__main__":

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    # app = QtWidgets.QApplication(sys.argv)
    apps = Nuki()
    sys.exit(app.exec_())
