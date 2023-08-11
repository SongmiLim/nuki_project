# controller 에서는 시그널만 받고 , 시그널 받으면 service에서 실행할수있록 하기.

# mvc
# - model (x)
# - view (o)
# - controller (o)
# - service(o)


# nuki에서 ui만들고 > ctrl넘기는것처럼 >
# upload_nuki > upload_controller > upload ( service )
# ??? >> login처럼 return ui로 할려고 하는거면 컨트롤러가 필요없나??
# 2시에 물어보기... << 이거 모듈 왜 안되는지...


import sys
from PySide2 import QtWidgets, QtCore
from jiwoon.gazu_api.view.UI.nuki import Nuki
from jiwoon.gazu_api.view.UI.upload_nuki import Upload_Nuki
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