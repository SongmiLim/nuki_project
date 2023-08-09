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
    __test = None

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.loader = Loader()
        self.selected_comptask = None
        self.load_mode = False

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
        self.project = comptask[0].get('project_name')
        self.sequence = self.model.selected_datas[0][0].get('sequence')['name']
        self.shot = comptask[0].get('entity_name')

    def run_nuke(self):
        """
        btn_run_nuke 클릭하면 해당 nuke파일이 열리거나,
        현재 파일로 아웃풋 파일들을 로드한다.
        """

        # set Tree initializing
        # tree = FileTree(self.project)
        # tree.mnt_point = '{NEW MNT POINT}'
        # tree.root = '{NEW ROOT}'
        # tree.style = '{NEW STYLE}'
        # tree.working_shot_file_path = '{NEW SHOT FILE PATH}'
        # tree.working_asset_file_path = '{NEW ASSET FILE PATH}'
        # tree.working_shot_file_name = '{NEW SHOT FILE NAME}'
        # tree.working_asset_file_name = '{NEW ASSET FILE NAME}'
        # tree.output_shot_file_path = '{NEW SHOT FILE PATH}'
        # tree.output_asset_file_path = '{NEW ASSET FILE PATH}'
        # tree.output_shot_file_name = '{NEW SHOT FILE NAME}'
        # tree.update_file_tree()

        ### CREATE WORKING FILE & OUTPUT FILE
        # task_type = None
        # task_types = gazu.task.all_task_types_for_project(self.project)
        # for task_type in task_types:
        #     if task_type['name'] == 'Layout' and task_type['for_entity'] == self.shot['type']:
        #         task_type = task_type
        #         break
        # task = gazu.task.get_task_by_name(self.shot, task_type)
        # working_file = gazu.files.new_working_file(task)
        # print('working_file',working_file)

        # TYPE 생성, 한번만 실행
        # output_type = gazu.files.get_output_type_by_name('EXR')
        # nuke_file = nuke.onScriptLoad()
        # gazu.files.new_entity_output_file(self.shot, output_type, task_type,
        #                                   'publish', working_file=working_file,
        #                                   revision=working_file['revision'])

        # add preview

        # output_name = '0803_test_jw'
        # output_vide_format = 'mov'
        # kitsu_upload_path = "%s/%s.%s" % (working_file['path'], output_name, output_vide_format)
        # comment = gazu.task.add_comment(task, '3d24de8b-b327-4c95-a469-392637497234', comment=user_comment)
        # preview = gazu.task.add_preview(task, comment, preview_file_path=kitsu_upload_path)

        if self.load_mode:
            pass
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
        else:
            # 해당 task의 working file을 생성하거나 open
            # task_type = None
            # task_types = gazu.task.all_task_types_for_project(self.project)
            # for task_type in task_types:
            #     if task_type['name'] == 'Layout' and task_type['for_entity'] == self.shot['type']:
            #         task_type = task_type
            #         break
            # task = gazu.task.get_task_by_name(self.shot, task_type)
            #
            create_path_dict, update_path_dict = self.get_outputfiles_path()
            # for object_type, path_list in create_path_dict.items():
            #     for nuki_id, file_path in path_list.items():
            #         print('info : ',file_path)
            #
            # preview = gazu.task.add_preview(task, 'comment', preview_file_path=create_path_dict)

            # print('preview',preview)

        # ----------------------------

            selected = self.model.selection_model.selectedRows()
            selected_list = list(map(lambda x: x.row(), selected))
            files = gazu.files.get_last_output_files_for_entity(self.shot, output_type=None,
                                                                task_type=None)
            # print('files',files)
            # 0803 jw_test
            # self.loader.create_nodes(create_path_dict)
            # self.loader.update_nodes(update_path_dict)

            for index in selected_list:
                working_file = self.loader.open_nuke_working_file(self.model.selected_datas[index])

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

    def get_outputfiles_path(self):
        """
        리스트를 받아서 아웃풋 파일의 path를 반환
        """
        selected = self.model.selection_model.selectedRows()
        selected_list = list(map(lambda x: x.row(), selected))

        create_path_dict = {}
        update_path_dict = {}

        for index in selected_list:
            # 선택한 요소들의 노드 반영 상태
            task_type_name = self.model.selected_datas[index][0].get('task_type_name')
            output_id = self.model.selected_datas[index][0].get('output_type_id') if self.model.selected_datas[index][0].get('output_type_id') else ''
            output_path = self.model.selected_datas[index][0].get('output_path') if self.model.selected_datas[index][0].get('output_path') else ''

        #     if node_status == 0:
        #         create_path_dict[task_type_name] = {output_id: output_path}
        #     elif node_status == 1:
        #         update_path_dict[task_type_name] = {output_id: output_path}
        # return create_path_dict, update_path_dict
            create_path_dict[task_type_name] = {output_id: output_path}
            # update_path_dict[task_type_name] = {output_id: output_path}
        return create_path_dict, update_path_dict
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
