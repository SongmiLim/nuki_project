import sys
from PySide2 import QtWidgets, QtCore
from nukitsu.gazu_api.service.upload import UUpload
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget

class foo(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.Init()
    # def Init(self):
    #     nuki_app = UUpload()
    #     nuki_app.show()
    #     print('test')
    #     print(nuki_app)

if __name__ == "__main__":

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    # app = QtWidgets.QApplication(sys.argv)
    apps = UUpload()
    sys.exit(app.exec_())
# nuke mainwidget에 override하는 형태.