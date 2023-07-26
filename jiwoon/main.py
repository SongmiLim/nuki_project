import sys
from PySide2 import QtWidgets, QtCore
from jiwoon.gazu_api.view.UI.nuki import Nuki

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    nuki_app = Nuki()
    sys.exit(app.exec_())


