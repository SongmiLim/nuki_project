import sys
from PySide2 import QtWidgets, QtCore
from jiwoon.gazu_api.service.upload import UUpload
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

#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     apps = foo()
#     sys.exit(app.exec_())
#######################################
# import sys
# from PySide2.QtWidgets import QApplication, QMainWindow
# from jiwoon.gazu_api.service.upload import UUpload
#
# class foo(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
# def show_ui():
#     nuke_window = foo()
#     nuki_app = UUpload()
#     nuki_app.setupUi(nuke_window)
#     nuki_app.show()
#     print('plz')
#
# if __name__ == '__main__':
#     show_ui()
#######################################

# def show_ui():
#     # app = QApplication(sys.argv)
#     window = UUpload()
#     window.show()
#     print('pleaaaaaaaaaaaaaaaaase')
#     # sys.exit(app.exec_())
#
# def ahh():
#     show_ui()
#
# if __name__ == '__main__':
#     show_ui()


#######################################
# import sys
# from PySide2.QtWidgets import QApplication, QMainWindow
# from jiwoon.gazu_api.service.upload import UUpload
#
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.uupload = UUpload()
#         self.uupload.setupUi(self)
#
# def show_ui():
#     nuke_window = MyWindow()
#     nuke_window.show()
#     print('plz')
#
# if __name__ == '__main__':
#     show_ui()

# nuke mainwidget에 override하는 형태.