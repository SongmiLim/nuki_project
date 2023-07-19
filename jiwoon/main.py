import sys
from PySide2 import QtWidgets

from jiwoon.gazu_api.controller.shot_controller import ShotController
from jiwoon.gazu_api.controller.task_controller import Controller
from jiwoon.gazu_api.model.shot_model import shotModel
from jiwoon.gazu_api.view.login import Login
from jiwoon.gazu_api.view.task_view import MainUI


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
# add nuki Class later(for auth)

# UI = Login()
UI = MainUI()

# shot controller 호출
ShotModel = shotModel()
gz = ShotController(ShotModel, UI)

# task controller 호출
# gz = Controller(Model(), UI)

sys.exit(app.exec_())
