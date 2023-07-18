import gazu
# gazu.client.set_host('http://192.168.3.117/api')
# gazu.log_in('admin@netflixacademy.com', 'netflixacademy')
# haji@netflixacademy.com
# haji1127
from PySide2.QtWidgets import QApplication, QMainWindow

from jiwoon.gazu_api.view.UI.login_view.LoginWidget import Ui_Login


class Login(QMainWindow, Ui_Login):
  def __init__(self):
    gazu.client.set_host('http://192.168.3.117/api')
    super().__init__()
    super().setupUi(self)
    self.setWindowTitle('login')

    # signal & slot.
    self.lineEdit_2.returnPressed.connect(self.login_btn_clicked)
    self.pushButton.clicked.connect(self.login_btn_clicked)

  def login(self):
    id = self.lineEdit.text()
    pw = self.lineEdit_2.text()
    if id and pw:
      try:
          gazu.log_in(id,pw)
          print(f'Logged in as {id}')

          # 로그인 로직에 관한건 더 여기다가 추가. # Perform additional login logic here
      except Exception as e:
        print('Login failed.')
    else:
      print('Please enter both ID and password.')

  def login_btn_clicked(self):
    self.login()
    pass


# app = QApplication()
# window = Login()
# window.show()
# app.exec_()