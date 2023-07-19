import sys
from PySide2 import QtWidgets


from jiwoon.gazu_api.controller.task_controller import Controller
from jiwoon.gazu_api.model.task_model import TaskModel
from jiwoon.gazu_api.view.login import Login
from jiwoon.gazu_api.view.task_view import MainUI

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # add nuki Class later(for auth)
    # UI = Login()
    UI = MainUI()
    Model = TaskModel()

    gz = Controller(Model, UI)
    sys.exit(app.exec_())
