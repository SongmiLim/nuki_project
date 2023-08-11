from datetime import datetime
import gazu as gazu
from PySide2 import QtWidgets
from jiwoon.gazu_api.service.utils import construct_full_path
from jiwoon.gazu_api.view.progressbar_widget import ProgressBar


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
        self.__task_type = name
        self.__task = gazu.task.get_task_by_name(self.__entity, self.__task_type)

    @property
    def task_status(self):
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

    def get_all_status(self, task):
        self.project = task.get('project_name')
        self.sequence = task.get('sequence_name')
        self.shot = task.get('entity_name')
        return self.set_task_init()

    def load_tasks(self, project, sequence, shot):
        self.project = project.get('name')
        self.sequence = sequence.get('name')
        self.shot = shot.get('name')

        self.update_progress_and_status()
        # status_list = self.set_task_init()
        # value = (100 / (len(self.model.todo_datas) - 1)) * (status_list.count(True))
        # ProgressBar.set_progressbar(self.view, value)
        #
        # self.model.task_status = self.task_status
        # self.model.all_task_status = status_list
        # self.model.layoutChanged.emit()

    def update_progress_and_status(self):
        status_list = self.set_task_init()
        value = (100 / (len(self.model.todo_datas) - 1)) * (status_list.count(True))
        ProgressBar.set_progressbar(self.view, value)

        self.model.task_status = self.task_status
        self.model.all_task_status = status_list
        self.model.layoutChanged.emit()

    def set_task_init(self):
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
                # self.new_nuke_working_file(CompTask(task))
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

    def new_nuke_working_file(self, comptask, name='main', comment='') -> dict:
        """
        입력받은 CompTask의 task에 대해 Kitsu DB상에 새로운 working file을 생성하는 함수.
        outputfile 만들 때 쓰일 dictionary 형태 working file을 반환한다.
        open_new_nuke_working_file()를 실행시켜 실제 nuke script를 저장한다.

        Args:
            comptask(molo.CompTask): 생성하고자 하는 compositing task의 CompTask 객체
            name(str, optional): working file dict의 이름, 기본값 "main"
            comment(str, optional): working file dict의 설명

        Returns:
            working_file (dict)
        """
        # nuke = gazu.files.get_software_by_name('nuke')
        nukenc = gazu.files.get_software_by_name('nukenc')
        working_file = gazu.files.new_working_file(comptask.task_dict, name=name, comment=comment,
                                                   software=nukenc, person=self.user)

        # self.working_file_path = construct_full_path(working_file)
        #
        # root_dir = os.path.dirname(self.working_file_path)
        # file_name = os.path.basename(self.working_file_path)
        #
        # if not os.path.isdir(root_dir):
        #     os.makedirs(root_dir)
        #
        # for file in os.listdir(root_dir):
        #     if file == file_name:
        #         raise WorkingFileExistsError("Already exists working file")
        #
        # molo_nuke.project_setting(comptask)
        # molo_nuke.save_script(self.working_file_path)
        # self.logger.create_working_file_log(self.user.get('full_name'), self.working_file_path)

        return working_file

