import sys
from PySide2 import QtWidgets, QtCore
from jiwoon.gazu_api.service.upload import UUpload

# from jiwoon.gazu_api.view.UI.upload_nuki import Upload_Nuki

from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget, QPushButton, QVBoxLayout

class foo(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.Init()
    def Init(self):
        nuki_app = UUpload()
        nuki_app.show()
        print('test')
        print(nuki_app)


if __name__ == "__main__":
    # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    apps = UUpload()
    sys.exit(app.exec_())

# import nuke
# import sys
# import os
# from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget, QPushButton, QVBoxLayout
# from jiwoon.gazu_api.service.upload import UUpload
#
#
# def show_upload_ui():
#     from jiwoon.gazu_api.view.UI.upload_ui import Ui_MainWindow
#     from PySide2.QtWidgets import QApplication
#
#     # app = QApplication(sys.argv)
#     window = UUpload()
#     window.show()
#     # sys.exit(app.exec_())