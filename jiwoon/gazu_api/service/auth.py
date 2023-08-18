import json
import os
import re
import gazu
from gazu import AuthFailedException

from jiwoon.gazu_api.service.exceptions import *
from jiwoon.gazu_api.service.logger import Logger
from PySide2.QtWidgets import QMessageBox

class Auth:
    def __init__(self):
        self.logger = Logger()
        self._host = ''
        self._user = None
        self._user_id = ''
        self._user_pw = ''
        self._valid_host = False
        self._valid_user = False
        self.dir_path = os.path.expanduser('~/nuki/jiwoon/gazu_api/data')
        self.user_path = os.path.join(self.dir_path, 'user.json')

        if self.access_setting():
            self.load_setting()

    @property
    def valid_host(self):
        return self._valid_host

    @property
    def valid_user(self):
        return self._valid_user

    @property
    def user(self):
        return self._user

    @property
    def host(self):
        return self._host

    def access_setting(self) -> bool:
        """
        디렉토리와 각 json 파일이 존재하는지 확인하고 없으면 초기화

        Returns: self.user_path에 해당하는 json 파일이 존재하거나 생성되면 True, 아니면 False
        """
        if not os.path.exists(self.dir_path):
            try:
                os.makedirs(self.dir_path)
            except OSError:
                raise AuthFileIOError("Error: Failed to create the directory.")
        if not os.path.exists(self.user_path):
            try:
                self.reset_setting()
            except OSError:
                raise AuthFileIOError("Error: Failed to create user.json file.")
        return True

    def load_setting(self):
        """
        json file에서 정보를 읽어오기

        json에 기록된 host나 user의 valid 값이 True이면 자동 login
        """
        user_dict = {}
        with open(self.user_path, 'r') as json_file:
            user_dict = json.load(json_file)

        print(user_dict.get('valid_host'))
        # if user_dict.get('valid_host'):

        if user_dict.get('valid_host') == False:
            self.connect_host("http://http://192.168.3.117/api")
        else:
            self.connect_host(user_dict.get('host'))

        if user_dict.get('valid_user'):
            self.log_in(user_dict.get('user_id'), user_dict.get('user_pw'))

    def log_in(self, try_id, try_pw) -> bool:
        # print(try_id, try_pw)
        # if not self._valid_host:
        #     raise UnconnectedHostError('Error: Host to login is not connected.')
        try:
            log_in = gazu.log_in(try_id, try_pw)
        except AuthFailedException:
            raise InvalidAuthError("Error: Couldn't find your Kitsu account")

        self._user = log_in['user']
        self._user_id = try_id
        self._user_pw = try_pw
        self._valid_user = True
        self.logger.enter_log(self.user.get("full_name"))
        return True

    def user_email_valid(self, try_id) -> bool:
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(email_pattern, try_id):
            return True
        else:
            # print('login failed')
            return False

    def connect_host(self, try_host):
        """
        try_host를 사용해 host에 접속 시도

        Returns: 접속에 성공하면 True, 아니면 False 반환
        """

        gazu.set_host(try_host)

        if not gazu.client.host_is_valid():
            #     host_message_box = QMessageBox()
            #     host_message_box.setIcon(QMessageBox.Information)
            #     host_message_box.setText("Host Connection Failed")
            #     host_message_box.setWindowTitle("error")
            #     host_message_box.setStandardButtons(QMessageBox.Ok)
            #     host_message_box.exec_()
            # else:
            #     # gazu.set_host("http://192.168.3.117/api")
            # print('error')
            # self._host = gazu.get_host()
            # print("host", self._host)
            if self._host == '':
                self._valid_host = False
                return
            else:
                self.connect_host(self._host)

        else:
            self._host = gazu.get_host()
            self._valid_host = True
            # self.logger.connect_log(self.host)
            # return True
        return

    def save_setting(self):
        """
        json file에 정보를 저장
        """
        user_dict = {
            'host': self.host,
            'user_id': self._user_id,
            'user_pw': self._user_pw,
            'valid_host': self._valid_host,
            'valid_user': self._valid_user,
        }
        with open(self.user_path, 'w') as json_file:
            json.dump(user_dict, json_file)

    def reset_setting(self):
        """
        json file에 저장된 정보 삭제
        """
        self._host = ''
        self._user_id = ''
        self._user_pw = ''
        self._valid_host = False
        self._valid_user = False

        self.save_setting()

    @property
    def user_id(self):
        return self._user_id
