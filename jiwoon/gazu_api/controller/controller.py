import os

from PySide2 import QtCore, QtUiTools

from jiwoon.gazu_api.model.filetree_model import TreeModel
from jiwoon.gazu_api.model.task_model import TaskModel
from jiwoon.gazu_api.model.shot_model import ShotModel
from jiwoon.gazu_api.service.nuke_service import NukeService
from jiwoon.gazu_api.service.shot_service import ShotService
from jiwoon.gazu_api.service.task_service import TaskService
from jiwoon.gazu_api.service.filetree_service import FileTreeService


class Controller:

    def __init__(self, view):

        # initializing
        self.view = view
        self.filetree_model = TreeModel()
        self.shot_model = ShotModel()
        self.task_model = TaskModel()
        self.filetree_service = FileTreeService(self.view)
        self.shot_service = ShotService(self.shot_model, self.view)
        self.task_service = TaskService(self.task_model, self.view)
        self.nuke_service = NukeService(self.task_model, self.view)

        # set initialize datas
        self.shot_service.get_all_tasks_todo(self.task_service)
        self.filetree_model.production_tree()

        # set Model
        self.view.filetree.setModel(self.filetree_model)
        self.view.task_table.setModel(self.task_model)
        self.view.shot_list.setModel(self.shot_model)
        self.task_model.selection_model = self.view.task_table.selectionModel()

        # show
        self.view.filetree.expandAll()
        self.view.show()

        # events & slots
        self.view.shot_list.clicked.connect(lambda: self.shot_service.shot_clicked(self.task_service)) # shot_list 에서 사용자 가 한 shot 을 클릭 했을 때 시그널 등록
        self.view.sorted_comboBox.currentTextChanged.connect(self.shot_service.sort_by_combobox) # sort_combobox 클릭 시 sorting 슬롯 호출
        self.view.filetree.clicked.connect(self.filetree_model.select_filetree)
        self.view.update_filetree_btn.clicked.connect(self.filetree_model.production_tree)
        self.view.update_filetree_btn.clicked.connect(self.view.filetree.expandAll)
        self.view.opennuke_btn.clicked.connect(self.nuke_service.run_nuke)
        self.task_model.selection_model.selectionChanged.connect(self.nuke_service.selected_comptask)



