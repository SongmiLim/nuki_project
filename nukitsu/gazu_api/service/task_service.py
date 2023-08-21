from datetime import datetime
import gazu as gazu
from PySide2 import QtWidgets
from nukitsu.gazu_api.service.utils import construct_full_path, OutlineDelegate
from nukitsu.gazu_api.view.progressbar_widget import ProgressBar


class TaskService:
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

    def __init__(self, model, view):
        self.model = model
        self.view = view
        OutlineDelegate(self.view.task_table)
    @property
    def project(self) -> dict:
        return self.__project

    @project.setter
    def project(self, name):
        self.__project = gazu.project.get_project_by_name(name)

    @property
    def sequence(self) -> dict:
        return self.__sequence

    @sequence.setter
    def sequence(self, name):
        self.__sequence = gazu.shot.get_sequence_by_name(self.project, name)

    @property
    def shot(self) -> dict:
        return self.__shot

    @shot.setter
    def shot(self, name):
        self.__shot = gazu.shot.get_shot_by_name(self.sequence, name)
        self.__entity = self.__shot

    @property
    def task(self) -> dict:
        return self.__task

    @task.setter
    def task(self, name):
        self.__task_type = name
        self.__task = gazu.task.get_task_by_name(self.__entity, self.__task_type)

    @property
    def task_status(self) -> bool:
        return self.__task_status

    @task_status.setter
    def task_status(self, value):
        self.__task_status = value


    def adjust_header_size(self):
        header = self.view.task_table.horizontalHeader()
        width = []
        for column in range(header.count()):
            header.setSectionResizeMode(column, QtWidgets.QHeaderView.ResizeToContents)
            width.append(header.sectionSize(column))

    def get_all_status(self, task) -> list:
        self.project = task.get('project_name')
        self.sequence = task.get('sequence_name')
        self.shot = task.get('entity_name')
        return self.set_task_init()

    def load_tasks(self, project, sequence, shot):
        self.model.selection_model.clearSelection()
        self.project = project.get('name')
        self.sequence = sequence.get('name')
        self.shot = shot.get('name')
        self.update_progress_and_status()

    def update_progress_and_status(self):
        status_list = self.set_task_init()
        value = (100 / (len(self.model.todo_datas) - 1)) * (status_list.count(True))
        ProgressBar.set_progressbar(self.view, value)

        self.model.task_status = self.task_status
        self.model.all_task_status = status_list
        self.model.layoutChanged.emit()

    def set_task_init(self) -> list:
        self.task_status = True
        all_task_status = []
        count = 0
        tasks = gazu.task.all_tasks_for_shot(self.__shot)
        files = gazu.files.get_last_output_files_for_entity(self.__shot, output_type=None,
                                                            task_type=None)
        self.model.todo_datas = []
        self.model.todo_datas.append([])
        self.model.selected_datas = []
        self.model.selected_datas.append([])
        self.adjust_header_size()

        for task in tasks:
            if task.get('task_type_name') != 'Compositing':
                # task의 output file이 있는지 찾기
                task_file = None
                for file in files:
                    if file.get('task_type_id') == task.get('task_type_id'):
                        task_file = file
                        files.remove(file)
                        break

                task_preview_file = gazu.files.get_all_preview_files_for_task(task.get('id'))
                self.model.todo_datas[count].append(task.get('task_type_name'))
                self.model.todo_datas[count].append(task.get('task_status_name'))
                self.model.todo_datas[count].append(
                    task_preview_file[len(task_preview_file) - 1].get('revision')) if task_preview_file else \
                    self.model.todo_datas[count].append('-')
                self.model.todo_datas[count].append(
                    task_preview_file[len(task_preview_file) - 1].get('extension')) if task_preview_file else \
                    self.model.todo_datas[count].append('-')
                self.model.todo_datas[count].append(
                    datetime.strptime(task.get('updated_at'), '%Y-%m-%dT%H:%M:%S').strftime('%Y/%m/%d %H:%M'))
                self.model.selected_datas[count].append(task)
                self.model.selected_datas[count][0]['sequence'] = self.sequence
                if task_file:
                    self.model.selected_datas[count][0]['output_type_id'] = task_file.get('id')
                    self.model.selected_datas[count][0]['output_path'] = construct_full_path(task_file)
                self.model.todo_datas.append([])
                self.model.selected_datas.append([])
                count += 1

        for todo_data in self.model.todo_datas:
            if todo_data:
                if todo_data and todo_data[1] != 'Done':
                    self.task_status = False
                else:
                    self.task_status = True

                all_task_status.append(self.task_status)
        return all_task_status

    def reload_tasks(self):
        self.update_progress_and_status()

    def clear_data(self):
        self.model.todo_datas = []


