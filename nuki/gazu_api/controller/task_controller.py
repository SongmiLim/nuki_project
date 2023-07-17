from gazu_api.service.task_service import TaskService


class TaskController:

    def __init__(self, model, view):
        # initializing
        self.view = view
        self.service = TaskService(model, view)
        self.view.listView.setModel(model)
        self.view.show()
        self.service.shot = '25c04280-2f8f-4228-81e7-df65ba46b907'  # temp_shot : avengers/SEQ01 / SH01

        # events & slots
        self.view.loadButton.clicked.connect(self.service.load_shot)
        # self.view.addButton.clicked.connect(self.service.create_asset)
        # self.view.modifyButton.clicked.connect(self.service.update_asset)
        # self.view.deleteButton.clicked.connect(self.service.remove_asset)
