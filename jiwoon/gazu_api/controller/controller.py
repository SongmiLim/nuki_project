from PySide2.QtCore import QModelIndex
from jiwoon.gazu_api.model.filetree_model import TreeModel
from jiwoon.gazu_api.model.task_model import TaskModel
from jiwoon.gazu_api.model.shot_model import ShotModel
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
        self.filetree_service = FileTreeService(self.filetree_model, self.view)
        self.shot_service = ShotService(self.shot_model, self.view)
        self.task_service = TaskService(self.task_model, self.view)

        # 초기 데이터 호출
        self.shot_service.get_all_tasks_todo()
        self.filetree_model.production_tree()
        # set Model
        self.view.filetree.setModel(self.filetree_model)
        self.view.filetree.expandAll()
        self.view.task_table.setModel(self.task_model)
        self.view.shot_list.setModel(self.shot_model)

        # show
        self.view.show()

        # events & slots
        # shot_list 에서 사용자 가 한 shot 을 클릭 했을 때 시그널 등록
        self.view.shot_list.clicked.connect(lambda: self.shot_service.shot_clicked(self.task_service))
        self.task_model.task_done.connect(self.shot_service.get_all_task_done_status)
        # self.view.loadButton.clicked.connect(self.task_service.load_shot)
        # self.view.addButton.clicked.connect(self.service.create_asset)
        # self.view.modifyButton.clicked.connect(self.service.update_asset)
        # self.view.deleteButton.clicked.connect(self.service.remove_asset)
        self.view.filetree.clicked[QModelIndex].connect(self.filetree_model.select_filetree)
        self.view.update_filetree_btn.clicked.connect(self.filetree_model.production_tree)
        # self.view.update_filetree_btn.clicked.connect(self.view.filetree.expandAll()) # btn 누를 때도 전부다 확장
