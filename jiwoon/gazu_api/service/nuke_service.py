import gazu as gazu
from PySide2.QtWidgets import QMessageBox
import nuke
from jiwoon.gazu_api.service.loader import Loader


class NukeService:
    __project = None
    __shot = None
    __sequence = None
    __task = None
    __task_type = None
    __task_status = True
    __asset_type = None
    __asset_type_dict = None
    __new_values = None
    __temp = None
    __entity = None
    __ext = None
    __test = None

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.loader = Loader()
        self.selected_comptask = None

    @property
    def project(self):
        return self.__project

    @project.setter
    def project(self, name):
        self.__project = gazu.project.get_project_by_name(name)

    @property
    def sequence(self):
        return self.__sequence

    @sequence.setter
    def sequence(self, name):
        self.__sequence = gazu.shot.get_sequence_by_name(self.project, name)

    @property
    def shot(self):
        return self.__shot

    @shot.setter
    def shot(self, name):
        self.__shot = gazu.shot.get_shot_by_name(self.sequence, name)
        self.__entity = self.__shot

    @property
    def task(self):
        return self.__task

    @task.setter
    def task(self, name):
        self.task_type = name
        self.__task = gazu.task.get_task_by_name(self.__entity, self.task_type)

    def update_selected_task_count(self):
        """
        table data 선택 한 개수 표시
        """
        self.view.tasks_num_label.setText(f'{len(self.model.selection_model.selectedRows())} / {len(self.model.todo_datas) - 1}')

    def update_selected_comptask(self, comptask):
        self.selected_comptask = comptask
        self.project = comptask[0].get('project_name')
        self.sequence = self.model.selected_datas[0][0].get('sequence')['name']
        self.shot = comptask[0].get('entity_name')

    def run_nuke(self):
        """
        btn_run_nuke 클릭하면 현재 파일로 아웃풋 파일들을 로드한다.
        """

        create_path_dict = self.get_outputfiles_path()
        print('create_path_dict',create_path_dict)
        self.loader.create_nodes(create_path_dict)

    def get_outputfiles_path(self):
        """
        리스트를 받아서 아웃풋 파일의 path를 반환
        """
        selected = self.model.selection_model.selectedRows()
        selected_list = list(map(lambda x: x.row(), selected))

        create_path_dict = {}

        for index in selected_list:
            # 선택한 요소들의 노드 반영 상태
            if self.model.selected_datas[index][0].get('task_status_name') != 'Done':
                host_message_box = QMessageBox()
                host_message_box.setIcon(QMessageBox.Information)
                host_message_box.setText("Done Failed")
                host_message_box.setWindowTitle("error")
                host_message_box.setStandardButtons(QMessageBox.Ok)
                host_message_box.exec_()
                return False
            task_type_name = self.model.selected_datas[index][0].get('task_type_name')
            output_id = self.model.selected_datas[index][0].get('output_type_id') if self.model.selected_datas[index][0].get('output_type_id') else ''
            output_path = self.model.selected_datas[index][0].get('output_path') if self.model.selected_datas[index][0].get('output_path') else ''
            create_path_dict['Shot'] = {self.shot.get('id'): self.project.get('name') + '/' + self.sequence.get('name') + '/' + self.shot.get('name')}
            create_path_dict[task_type_name] = {output_id: output_path}
        return create_path_dict
