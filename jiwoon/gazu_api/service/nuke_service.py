import gazu as gazu
from PySide2 import QtWidgets
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
            # create_path_dict = {'Layout': {'2d49b7e6-df15-4c9c-9c36-9cad45ed7aa8': '/home/rapa/jw_test/kitsu/glass_onion_a_knives_out_mystery/shots/sq01/sh01/layout/working/v018/glass_onion_a_knives_out_mystery_sq01_sh01_layout_0018.nk'}}

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

            for index in selected_list:
                working_file = self.loader.open_nuke_working_file(self.model.selected_datas[index])



            # 0803 jw_test
            task_path = '/home/rapa/jw_test/kitsu/glass_onion_a_knives_out_mystery/shots/sq01/sh01/layout/working/v018/BB8.0002.exr'
            create_path_dict = {'Layout': {'2d49b7e6-df15-4c9c-9c36-9cad45ed7aa8': '/home/rapa/jw_test/kitsu/glass_onion_a_knives_out_mystery/shots/sq01/sh01/layout/working/v018/BB8.0002.exr'},
                                'FX': {'2d49b7e6-df15-4c9c-9c36-9cad45ed7aa8': '/home/rapa/jw_test/kitsu/glass_onion_a_knives_out_mystery/shots/sq01/sh01/layout/working/v018/BB8.0002.exr'}}

            self.loader.create_nodes(create_path_dict)
            # self.loader.update_nodes(update_path_dict)

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
            print(task_type_name,'/',output_id,'/',output_path)
        #     if node_status == 0:
        #         create_path_dict[task_type_name] = {output_id: output_path}
        #     elif node_status == 1:
        #         update_path_dict[task_type_name] = {output_id: output_path}
        # return create_path_dict, update_path_dict
            create_path_dict[task_type_name] = {output_id: output_path}
            # update_path_dict[task_type_name] = {output_id: output_path}
        return create_path_dict, update_path_dict

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

    def adjust_header_size(self):
        header = self.view.task_table.horizontalHeader()
        width = []
        for column in range(header.count()):
            header.setSectionResizeMode(column, QtWidgets.QHeaderView.ResizeToContents)
            width.append(header.sectionSize(column))

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
