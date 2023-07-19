import os

from PySide2 import QtCore, QtUiTools

from jiwoon.gazu_api.service.task_service import TaskService
from jiwoon.gazu_api.service.shot_service import ShotService
from jiwoon.gazu_api.model.shot_model import shotModel

class ShotController:

    def __init__(self, model, view):
        # initializing
        self.view = view
        self.shot_service = ShotService(model, view)

        # 데이터 호출
        self.shot_service.get_all_tasks_todo()
        self.view.shot_list.setModel(model)

        self.view.show()

        # events & slots
        # self.view.loadButton.clicked.connect(self.task_service.load_shot)
        # self.view.addButton.clicked.connect(self.service.create_asset)
        # self.view.modifyButton.clicked.connect(self.service.update_asset)
        # self.view.deleteButton.clicked.connect(self.service.remove_asset)

