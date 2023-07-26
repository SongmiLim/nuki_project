import json
import os

import gazu
from jiwoon.gazu_api.service.logger import Logger


class Auth:
    def __init__(self):
        self.logger = Logger()

        self._host = ''
        self._user = None
        self._user_id = ''
        self._user_pw = ''
        self._valid_host = False
        self._valid_user = False

        self.dir_path = os.path.expanduser('~/.config/Molo/')
        self.user_path = os.path.join(self.dir_path, 'user.json')

        # if self.access_setting():
        #     self.load_setting()

    @property
    def valid_host(self):
        return self._valid_host

    @property
    def valid_user(self):
        """
        Returns:
            bool: 로그인에 성공했다면 True, 아니면 False
        """
        return self._valid_user

    @property
    def user(self):
        """
        Returns:
            dict: 로그인한 계정의 user dict
        """
        return self._user
    @property
    def host(self):
        """
        Returns:
            str: 연결된 host URL
        """
        return self._host

    def log_in(self, try_id, try_pw) -> bool:
        # print(try_id, try_pw)
        if not self._valid_host:
            # raise UnconnectedHostError('Error: Host to login is not connected.')
            # self.error_label.setText("Couldn't find your Host")
            print('error')
        try:
            log_in = gazu.log_in(try_id, try_pw)
            print(f'logged in as {try_id}')
        except gazu.AuthFailedException:
            # raise InvalidAuthError("Error: Couldn't find your Kitsu account")
            print('error')

        self._user = log_in['user']
        self._user_id = try_id
        self._user_pw = try_pw
        self._valid_user = True
        self.logger.enter_log(self.user.get("full_name"))
        return True

    def connect_host(self, try_host) -> bool:
        """
        try_host를 사용해 host에 접속 시도

        Returns:
            bool: 접속에 성공하면 True, 아니면 False 반환
        """
        gazu.set_host(try_host)
        if not gazu.client.host_is_valid():
            # raise InvalidAuthError('Error: Invalid host URL.')
            print('error')
        self._host = gazu.get_host()
        self._valid_host = True
        self.logger.connect_log(self.host)
        return True

    def save_setting(self):
        """
        json file에 정보를 저장
        """
        user_dict = {
            'host': self.host,
            'user_id': self._user_id,
            'user_pw': self._user_pw,
            'valid_host': self.valid_host,
            'valid_user': self.valid_user,
        }
        with open(self.user_path, 'w') as json_file:
            json.dump(user_dict, json_file)
