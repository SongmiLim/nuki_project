import gazu as gazu
from PySide2 import QtWidgets

from jiwoon.gazu_api.service.filetree import FileTree
from jiwoon.gazu_api.service.loader import Loader
from jiwoon.gazu_api.view.progressbar_widget import ProgressBar


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

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.host = gazu.client.set_host("http://192.168.3.117/api")
        self.loader = Loader()
        self.selected_comptask = None
        gazu.log_in("admin@netflixacademy.com", "netflixacademy")

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
        # self.__shot = gazu.shot.get_shot(id)
        self.__shot = gazu.shot.get_shot_by_name(self.sequence, name)
        self.__entity = self.__shot

    # @shot.setter
    # def shot(self, id):
    #     self.__shot = gazu.shot.get_shot(id)

    @property
    def task(self):
        return self.__task

    @task.setter
    def task(self, name):
        self.task_type = name
        self.__task = gazu.task.get_task_by_name(self.__entity, self.task_type)

    @property
    def task_status(self):
        return self.__task_status

    @task_status.setter
    def task_status(self, value):
        self.__task_status = value

    def update_selected_task_count(self):
        """
        table data 선택 한 개수 표시
        """
        self.view.tasks_num_label.setText(
            f'{len(self.model.selection_model.selectedRows())} / {len(self.model.todo_datas) - 1}')

    def update_selected_comptask(self, comptask):
        self.selected_comptask = comptask

    def run_nuke(self):
        tree = FileTree()
        """
               btn_run_nuke 클릭하면 해당 nuke파일이 열리거나,
               현재 파일로 아웃풋 파일들을 로드한다.
               """
        # if self.load_mode:
        #     # 선택한 output file들에 대한 node들을 create or update
        #     create_path_dict, update_path_dict = self.get_outputfiles_path()
        #     molo_nuke.deselect_all_nodes()
        #     self.loader.create_nodes(create_path_dict)
        #     self.loader.update_nodes(update_path_dict)
        #     molo_nuke.focus_selected_node()
        #     self.update_node_status_icon()
        #     self.update_selected_count()
        # else:
        #     if not self.selected_comptask:
        #         return

        # 해당 task의 working file을 생성하거나 open
        selected = self.model.selection_model.selectedRows()
        selected_list = list(map(lambda x: x.row(), selected))
        for index in selected_list:
            pass
            # print('selected_task : ', self.model.selected_datas[index])
        working_file = self.loader.open_nuke_working_file(self.model.selected_datas[0])
        # self.selected_comptask.last_comptask_revision = working_file
        # self.identify_nuke_file()
        # self.update_selected_comptask(self.selected_comptask)
        #
        # self.load_mode = True
        # self.table_model.load_mode = True
        # self.ui.label_selected_count.setVisible(True)
        # self.ui.btn_select_all.setVisible(True)
        # self.ui.btn_deselect_all.setVisible(True)
        # self.ui.btn_refresh_task_table.setVisible(True)
        # self.ui.btn_run_nuke.setText('Load Selected Files')
        #
        # self.update_node_status_icon()
        # self.update_table()
        #
        # self.ui.showMinimized()
        # self.ui.setWindowState(self.ui.windowState() and (not QtCore.Qt.WindowMinimized or QtCore.Qt.WindowActive))
        #

    def reload_comptasks(self):
        """
        task status를 기준으로 각각 self.todo_comptasks, self.done_comptasks로 저장
        user의 comptask목록을 reload
        """
        self.todo_comptasks = []
        self.done_comptasks = []
        self.browser.refresh_comp_tasks()
        for i in self.browser.todo_comp_tasks:
            self.todo_comptasks.append(molo.CompTask(i))
        for i in self.browser.done_comp_tasks:
            self.done_comptasks.append(molo.CompTask(i))
        self.filter_by_checkbox()
        #
        # if not self.selected_comptask:
        #     return

        # for row in range(self.browser_model.rowCount()):
        #     if self.selected_comptask.shot_id == self.browser_model.comptasks[row].shot_id:
        #         self.update_selected_comptask(self.browser_model.comptasks[row])

    def filter_by_checkbox(self):
        """
        self.ui.checkBox_done의 체크 유무에 따라
        self.done_comptasks도 self.comptasks에 포함
        """
        self.comptasks = self.todo_comptasks.copy()
        if self.ui.checkBox_done.isChecked():
            self.comptasks += self.done_comptasks

        self.update_shot_tree()

        self.browser_model.comptasks = self.comptasks
        self.update_shot_count()
        self.sort_by_combobox()
        self.browser_view.scrollToTop()

    def user_info_tree(self, comptasks):
        """
        list : 로그인 된 'user'를 기준으로 정렬된 프로젝트, 시퀀스, 테스크

        user를 기준으로 CompTask를 활용해서 사용자(아티스트)가 할당 되어 있는 task를 tree형태로 보여 준다.

        """
        result_dict = {}
        for comp_task in comptasks:
            proj_name = comp_task.proj_name
            seq_name = comp_task.seq_name
            if proj_name not in result_dict:
                result_dict[proj_name] = {}
            if seq_name not in result_dict[proj_name]:
                result_dict[proj_name][seq_name] = []
            result_dict[proj_name][seq_name].append(comp_task.shot_name)

        return result_dict

    def update_shot_tree(self):
        """
        user가 가지고 있는 task를 self.ui.shot_tree에 초기화 후 표시
        """
        self.ui.shot_tree.clear()
        user_item = QtWidgets.QTreeWidgetItem(self.ui.shot_tree)
        user_item.setText(0, self.auth.user.get("full_name"))
        info = self.user_info_tree(self.sort_by_name(self.comptasks))
        for i in info:
            if not isinstance(i, str):
                continue
            proj_item = QtWidgets.QTreeWidgetItem(user_item)
            proj_item.setText(0, i)
            for j in info[i]:
                if not isinstance(j, str):
                    continue
                seq_item = QtWidgets.QTreeWidgetItem(proj_item)
                seq_item.setText(0, j)
                for k in info[i][j]:
                    if not isinstance(k, str):
                        continue
                    shot_item = QtWidgets.QTreeWidgetItem(seq_item)
                    shot_item.setText(0, k)
        self.ui.shot_tree.expandAll()

    @staticmethod
    def sort_by_name(shot_data):
        """
        self.browser_model data를 shot이름으로 정렬

        Args:
            shot_data: browser_model의 comptasks

        Returns: sorted_shot_data(list)

        """
        sorted_shot_data = sorted(shot_data, key=lambda ct: (ct.proj_name, ct.seq_name, ct.shot_name), reverse=False)
        return sorted_shot_data

    def adjust_header_size(self):
        header = self.view.task_table.horizontalHeader()
        width = []
        for column in range(header.count()):
            header.setSectionResizeMode(column, QtWidgets.QHeaderView.ResizeToContents)
            width.append(header.sectionSize(column))

    def get_all_status(self, shot):
        self.project = shot.get('project_name')
        self.sequence = shot.get('sequence_name')
        self.shot = shot.get('entity_name')
        return self.set_task_init()

    def load_tasks(self, project, sequence, shot):
        self.project = project.get('name')
        self.sequence = sequence.get('name')
        self.shot = shot.get('name')

        status_list = self.set_task_init()
        value = (100 / (len(self.model.todo_datas) - 1)) * (status_list.count(True))
        ProgressBar.set_progressbar(self.view, value)

        self.model.task_status = self.task_status
        self.model.all_task_status = status_list
        self.model.layoutChanged.emit()

    def set_task_init(self):
        self.task_status = True
        self.all_task_status = []
        tasks = gazu.task.all_tasks_for_shot(self.__shot)
        count = 0

        self.model.todo_datas = []
        self.model.todo_datas.append([])
        self.adjust_header_size()

        for task in tasks:
            if task.get('task_type_name') != 'Compositing':
                # self.new_nuke_working_file(CompTask(task))
                task_file = gazu.files.get_all_preview_files_for_task(task.get('id'))
                self.model.todo_datas[count].append(task.get('task_type_name'))
                self.model.todo_datas[count].append(task.get('task_status_name'))
                self.model.todo_datas[count].append(task_file[len(task_file) - 1].get('revision')) if task_file else \
                    self.model.todo_datas[count].append('-')
                self.model.todo_datas[count].append(task_file[len(task_file) - 1].get('extension')) if task_file else \
                    self.model.todo_datas[count].append('-')
                self.model.todo_datas[count].append(task.get('updated_at'))
                self.model.todo_datas.append([])
                count += 1

        for todo_data in self.model.todo_datas:
            if todo_data:
                if todo_data and todo_data[1] != 'Done':
                    self.task_status = False
                else:
                    self.task_status = True
                self.all_task_status.append(self.task_status)

        return self.all_task_status

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
