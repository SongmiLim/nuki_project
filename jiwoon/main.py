import sys
from PySide2 import QtWidgets


from jiwoon.gazu_api.controller.controller import Controller
from jiwoon.gazu_api.view.task_view import MainUI

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # add nuki Class later(for auth)
    # UI = Login()

    UI = MainUI()
    gz = Controller(UI)
    sys.exit(app.exec_())

