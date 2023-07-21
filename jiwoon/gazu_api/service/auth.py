import gazu
from exceptions import *
from jiwoon.gazu_api.view.login import Login


class Auth:
    def __init__(self):
        self._valid_host = False
        # self._valid_user = False

    @property
    def valid_host(self):
        return self._valid_host

    def log_in(self, try_id, try_pw):
        # print(try_id, try_pw)
        if not self._valid_host:
            raise UnconnectedHostError('Error: Host to login is not connected.')
            self.error_label.setText("Couldn't find your Host")

        try:
            log_in = gazu.log_in(try_id, try_pw)
            print(f'logged in as {try_id}')
        except gazu.AuthFailedException:
            raise InvalidAuthError("Error: Couldn't find your Kitsu account")
