import sys
from PySide2 import QtWidgets, QtCore
from jiwoon.gazu_api.controller.controller import Controller
from jiwoon.gazu_api.view.UI.login import Login
from jiwoon.gazu_api.view.main_view import MainUI

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    # login = Login()
    gz = Controller(MainUI())
    sys.exit(app.exec_())


