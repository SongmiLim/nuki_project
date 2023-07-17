import gazu
from PySide2 import QtWidgets

from gazu_api.service.comp_task import CompTask
from gazu_api.service.file_tree import FileTree


class TaskService:
    __project = None
    __shot = None
    __sequence = None
    __task = None
    __task_type = None
    __task_status = None
    __asset_type = None
    __asset_type_dict = None
    __new_values = None
    __temp = None

    def __init__(self, model, view):
        self.model = model
        self.view = view

        gazu.client.set_host("http://192.168.3.117/api")
        gazu.log_in("admin@netflixacademy.com", "netflixacademy")

    @property
    def project(self):
        return self.__project

    @project.setter
    def project(self, name):
        self.__project = gazu.project.get_project_by_name(name)

    @property
    def shot(self):
        return self.__shot

    @shot.setter
    def shot(self, id):
        self.__shot = gazu.shot.get_shot(id)
        # self.__shot = gazu.shot.get_shot_by_name(sequence_dict, "SH01")

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

    def user_info_tree(self,comptasks):
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
    def load_shot(self):
        self.project = self.view.projectEdit.text().strip()
        # self.asset = self.view.assetEdit.text().strip()
        # self.proj_dict = gazu.project.get_project(self.__shot.get('project_id'))

        _todo_comp_tasks = gazu.user.all_tasks_to_do()
        _done_comp_tasks = gazu.user.all_done_tasks()
        _comp_tasks = _todo_comp_tasks + _done_comp_tasks
        tasks = gazu.task.all_tasks_for_shot(self.__shot)

        for task in tasks:
            if task.get('id') == '109ecca1-1f8e-47fd-82d6-99750903416e':
                temp_task = gazu.task.get_task(task.get('id'))
                temp_entity = temp_task.get('entity')
                temp_data = temp_entity.get('data')
                print(temp_data) # for ver, ext

            # if task.get('task_type_name') == "Compositing":
            #     print(task.get('task_type_name'), task.get('task_status_name'), task.get('updated_at'))

        # self.file_tree = self.proj_dict.get('file_tree')

        # info = self.user_info_tree(_comp_tasks)
        # file_tree.update_file_tree()

        # file_tree = FileTree(self.proj_dict)



        # print(tree)

        # for task in tasks:
        #     # comp_task = CompTask(task)
        #     print(task)
        # print(self.__shot)
        # # gazu.files.get_last_output_files_for_entity(self.shot_dict, output_type=output_type, task_type=task_type)
        # # output_types = gazu.files.all_output_types_for_entity(self.__shot)
        # print(output_types)
        # output_files_dict = gazu.files.get_last_output_files_for_entity(self.__shot)
        # print(output_files_dict)

        # plate_task_type = gazu.task.get_task_type_by_name('Compositing')
        # plate_task = gazu.task.get_task_by_entity(self.__shot, plate_task_type)
        #
        #
        # preview_file = gazu.files.get_all_preview_files_for_task(plate_task)
        # print(preview_file)

        # print(gazu.project.get_project_by_name("avengers"))
        # tree = FileTree(gazu.project.get_project_by_name("avengers"))
        # print(tree)
        # tree.update_file_tree()

        # for task in tasks:
            # print(task)


        # print(tasks)
        # output_files_dict = gazu.files.get_last_output_files_for_entity(self.__shot)
        # print(output_files_dict)


        # self.model.datas.append(self.asset['name'], )
        # self.model.layoutChanged.emit()



