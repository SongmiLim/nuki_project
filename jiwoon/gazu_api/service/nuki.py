import os
# import webbrowser
import gazu

from jiwoon.gazu_api.controller.controller import Controller
from jiwoon.gazu_api.service.exceptions import *
from PySide2 import QtCore, QtUiTools, QtWidgets
from PySide2.QtWidgets import QMainWindow, QWidget
from jiwoon.gazu_api.service.auth import Auth
from jiwoon.gazu_api.view.main_view import MainUI


class Nuki(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login_ui = None
        self.host_ui = None
        self.auth = Auth()
        self.valid_info()

    def valid_info(self):
        if self.auth.valid_host and self.auth.valid_user:
            self.main_widget()
        elif not self.auth.valid_host:
            self.host_widget()
        else:
            self.login_widget()

    # def forgot_pw_cmdlink_btn_clicked(self):
    #     forgot_password_browser = 'http://192.168.3.117/reset-password'
    #     webbrowser.open(forgot_password_browser)

    def main_widget(self):
        Controller(MainUI())

    def host_widget(self):
        """
        host ui 설정
        """
        self.host_ui = self.init_ui('../view/UI/nuki_host_widget.ui')
        print(self.host_ui)
        self.host_ui.host_input.returnPressed.connect(self.run_connect_host)
        self.host_ui.connect_btn.clicked.connect(self.run_connect_host)

    def login_widget(self):
        """
        login ui 설정
        """
        self.login_ui = self.init_ui('../view/UI/login_widget_test.ui')
        self.login_ui.ID_lineedit.setPlaceholderText('Email@address.com')
        self.login_ui.pw_lineedit.setPlaceholderText('Password')
        self.login_ui.pw_lineedit.setEchoMode(self.login_ui.pw_lineedit.Password)
        self.login_ui.pw_lineedit.returnPressed.connect(self.run_log_in)
        self.login_ui.signin_btn.clicked.connect(self.run_log_in)
        # self.login_ui.forgotpw_cmdlinkbtn.clicked.connect(self.forgot_pw_cmdlink_btn_clicked)
        # self.login_ui.error_label.setText('')

    def run_log_in(self):
        try_id = self.login_ui.ID_lineedit.text()
        try_pw = self.login_ui.pw_lineedit.text()
        is_valid_email = self.auth.user_email_valid(try_id)

        if is_valid_email:
            try:
                self.auth.log_in(try_id, try_pw)
                self.login_ui.error_label.setText('')
            except InvalidAuthError:
                print('dd, error')
                self.login_ui.error_label.setText("Couldn't find your Kitsu account")

        else:
            if try_id == '' or try_pw == '':
                self.login_ui.error_label.setText("Please enter your email and password.")
            else:
                self.login_ui.error_label.setText("Invalid login credentials. Please try again.")

        if self.auth.valid_user:
            if self.login_ui.remember_checkbox.isChecked():
                self.auth.save_setting()
            self.login_ui.close()
            self.main_widget()

        else:
            print('valid_user, error')

    def run_connect_host(self):
        """
        host ui의 connect_btn에 연결된 함수
        host_input에 입력된 host 주소를 이용해 host 연결을 시도
        """
        try_host = self.host_ui.host_input.text()

        try:
            self.auth.connect_host(try_host)
        except InvalidAuthError:
            raise Exception('Error: Invalid host URL.')

        if self.auth.valid_host:
            # self.auth.save_setting()
            self.host_ui.close()
            self.login_widget()

    def init_ui(self, ui_path):
        """
        입력된 경로의 .ui 파일을 load한 후 화면에 표시

        Args: ui_path(str): 화면에 표시할 ui 파일의 경로

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

        w = int((screen_resolution.width() - ui.width()) / 2)
        h = int((screen_resolution.height() - ui.height()) / 2)
        ui.move(w, h)
        ui.show()
        return ui

