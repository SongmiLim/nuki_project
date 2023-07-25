import gazu
import sys
import webbrowser


from PySide2.QtWidgets import QApplication, QMainWindow
from jiwoon.gazu_api.view.UI.LoginWidget import Ui_Login
from jiwoon.gazu_api.view.main_view import MainUI
from jiwoon.gazu_api.service import exceptions

class Login(QMainWindow, Ui_Login):
  def __init__(self):
    gazu.client.set_host('http://192.168.3.117/api')
    super().__init__()
    super().setupUi(self)
    self.setWindowTitle('login')
    self.ui = MainUI()

    # UI
    self.ID_lineedit.setPlaceholderText('Email@address.com')
    self.pw_lineedit.setPlaceholderText('Password')
    self.pw_lineedit.setEchoMode(self.pw_lineedit.Password)
    self.error_label.setText('')

    # signal & slot.
    self.pw_lineedit.returnPressed.connect(self.login_btn_clicked)
    self.signin_btn.clicked.connect(self.login_btn_clicked)
    self.forgotpw_cmdlinkbtn.clicked.connect(self.forgot_pw_cmdlink_btn_clicked)

  def run_log_in(self):
    try_id = self.ID_lineedit.text()
    try_pw = self.pw_lineedit.text()
    if try_id and try_pw:
      try:
          self.auth.log_in(try_id, try_pw)
          print(f'Logged in as {try_id}')
          self.close()
          # self.Ui()
      except:
        print('Login failed.')
        self.error_label.setText("Couldn't find your Kitsu account")

    else:
      print('Please enter both ID and password.')
      self.error_label.setText('Please enter both ID and password.')

  def login_btn_clicked(self):
    self.run_log_in()
    pass


  def forgot_pw_cmdlink_btn_clicked(self):
    forgot_password_browser = 'http://192.168.3.117/reset-password'
    webbrowser.open(forgot_password_browser)
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())