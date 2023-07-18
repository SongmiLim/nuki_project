import os

from PySide2 import QtCore, QtUiTools

from jiwoon.gazu_api.service.task_service import TaskService


class Controller:

    def __init__(self, model, view):
        # initializing
        self.view = view
        # self.shot_service = ShotService(model, view)
        self.task_service = TaskService(model, view)
        self.view.listView.setModel(model)
        self.view.show()

        # events & slots
        self.view.loadButton.clicked.connect(self.task_service.load_shot)
        # self.view.addButton.clicked.connect(self.service.create_asset)
        # self.view.modifyButton.clicked.connect(self.service.update_asset)
        # self.view.deleteButton.clicked.connect(self.service.remove_asset)

