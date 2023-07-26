import os
import sys
import webbrowser
from jiwoon.gazu_api.service.exceptions import *
from PySide2 import QtCore, QtUiTools, QtWidgets
from PySide2.QtWidgets import QMainWindow
from jiwoon.gazu_api.controller.controller import Controller
from jiwoon.gazu_api.service.auth import Auth
from jiwoon.gazu_api.view.main_view import MainUI


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login_ui = None
        self.host_ui = None
        self.screen_height = None
        self.screen_width = None
        self.auth = Auth()
        self.setWindowTitle('login')

        if self.auth.valid_host and self.auth.valid_user:
            self.main_widget()
        elif not self.auth.valid_host:
            self.host_widget()
        else:
            self.login_widget()

    def run_log_in(self):
        try_id = self.login_ui.user_id_input.text()
        try_pw = self.login_ui.user_pw_input.text()
        try:
            self.auth.log_in(try_id, try_pw)
        except InvalidAuthError:
            pass
        if self.auth.valid_user:
            if self.login_ui.remember_check.isChecked():
                self.auth.save_setting()
            self.login_ui.close()
            Controller(MainUI())
        else:
            self.login_ui.error_msg.setText('Incorrect ID or password!')
            self.login_ui.error_msg.setStyleSheet("Color : orange")

    def login_btn_clicked(self):
        self.run_log_in()
        pass

    def forgot_pw_cmdlink_btn_clicked(self):
        forgot_password_browser = 'http://192.168.3.117/reset-password'
        webbrowser.open(forgot_password_browser)
        pass

    def host_widget(self):
        """
        host ui 설정
        """
        self.host_ui = self.init_ui('nuki_host_widget.ui')
        self.host_ui.host_input.returnPressed.connect(self.run_connect_host)
        self.host_ui.connect_btn.clicked.connect(self.run_connect_host)

    def login_widget(self):
        """
        로그인 ui 설정
        """
        self.login_ui = self.init_ui('loginwidget.ui')
        self.login_ui.user_id_input.setPlaceholderText('Email@address.com')
        self.login_ui.user_pw_input.setPlaceholderText('Password')
        self.login_ui.user_pw_input.setEchoMode(self.login_ui.user_pw_input.Password)
        self.login_ui.user_pw_input.returnPressed.connect(self.run_log_in)
        self.login_ui.login_btn.clicked.connect(self.run_log_in)

    def run_connect_host(self):
        """
        host ui의 connect_btn에 연결된 함수
        host_input에 입력된 host 주소를 이용해 host 연결을 시도
        """
        try_host = self.host_ui.host_input.text()
        try:
            self.auth.connect_host(try_host)
        except UnconnectedHostError:
            pass
        if self.auth.valid_host:
            self.auth.save_setting()
            self.host_ui.close()
            self.login_widget()
        else:
            self.host_ui.error_msg.setText('Invalid address!')
            self.host_ui.error_msg.setStyleSheet("Color : orange")

    def init_ui(self, ui_path):
        """
    입력된 경로의 .ui 파일을 load한 후 화면에 표시

    Args:
        ui_path(str): 화면에 표시할 ui 파일의 경로

    Returns: load된 ui 객체
    """
        script_path = os.path.realpath(__file__)
        ui_path = os.path.join(os.path.dirname(script_path), ui_path)
        ui_file = QtCore.QFile(ui_path)
        ui_file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        ui = loader.load(ui_file)
        ui_file.close()

        screen_resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.screen_width = screen_resolution.width()
        self.screen_height = screen_resolution.height()

        w = int((self.screen_width - ui.width()) / 2)
        h = int((self.screen_height - ui.height()) / 2)
        ui.move(w, h)
        ui.show()
        return ui

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    myapp = QtWidgets.QApplication(sys.argv)
    login = Login()
    sys.exit(myapp.exec_())

