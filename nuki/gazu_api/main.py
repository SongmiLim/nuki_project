import sys
from PySide2 import QtWidgets

from gazu_api.controller.task_controller import TaskController
from gazu_api.model.task_model import TaskModel
from gazu_api.view.task_view import TaskUI

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gz = TaskController(TaskModel(), TaskUI())
    sys.exit(app.exec_())


