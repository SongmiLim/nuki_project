import sys
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QMainWindow
from nukitsu.gazu_api.service.nuki import Nuki

class NukiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        Nuki()


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    apps = NukiApp()
    sys.exit(app.exec_())
