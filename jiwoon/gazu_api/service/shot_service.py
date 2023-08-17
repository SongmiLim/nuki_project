import gazu
from jiwoon.gazu_api.service.comp_shot import CompShot
from jiwoon.gazu_api.service.todo_shot import TodoShot
from PySide2.QtCore import Qt, QDir
from PySide2.QtWidgets import QMenu, QMessageBox, QFileDialog
from PySide2.QtGui import QPixmap, QPixmapCache, QImage, QCursor
import os
from jiwoon.gazu_api.service.filetree_update import *

basedir = os.path.dirname(__file__)
default_img = QImage(os.path.join(basedir, '../image/nuke.png'))

FILE_FILTERS = [
    '*.nknc (*.nknc)',
    'All files (*)'
]


class ShotService:
    __project = None
    __shot = None
    __sequence = None
    # __task = None
    # __task_type = None
    __task_status = None

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.task_service = None
        # self.host = gazu.client.set_host("http://192.168.3.117/api")
        # gazu.log_in("admin@netflixacademy.com", "netflixacademy")
        # print("host test", gazu.client.get_host)
        self.raw_todo_shots_list = []
        self.filtered_todo_shots = []

    @property
    def project(self):
        """
        Returns:
            dict: 선택한 task의 project 정보
        """
        return self.__project

    @project.setter
    def project(self, name):
        self.__project = gazu.project.get_project_by_name(name)

    @property
    def sequence(self):
        """
        Returns:
            dict: 선택한 task의 sequence 정보
        """
        return self.__sequence

    @sequence.setter
    def sequence(self, name):
        self.__sequence = gazu.shot.get_sequence_by_name(self.project, name)

    @property
    def shot(self):
        """
        Returns:
            dict: 선택한 task의 shot 정보
        """
        return self.__shot

    @shot.setter
    def shot(self, name):
        # self.__shot = gazu.shot.get_shot(id)
        self.__shot = gazu.shot.get_shot_by_name(self.sequence, name)
        # self.__entity = self.__shot

    def get_all_tasks_todo(self, task_service):
        self.task_service = task_service

        # 작업자가 할당받은 모든 todo_shots 불러오기
        self.raw_todo_shots_list = gazu.user.all_tasks_to_do()

        # todo_shots의 많은 정보 중 필요한 정보들만 객체에 저장
        self.filtered_todo_shots = self.filter_todo_shots(task_service)

        # filtered_todo_shots를 view에 load
        self.load_shots_to_view(self.filtered_todo_shots)

        # 작업자 에게 할당된 샷의 총 개수
        assigned_shot_num = self.total_assigned_shot_num()
        self.view.assigned_shot_num.setText(f'{str(assigned_shot_num)} shots')

        self.view.sorted_comboBox.setCurrentIndex(0)
        self.clear_shot_detail_info()

    def filter_todo_shots(self, task_service) -> list:
        filtered_todo_shots = []

        # 할당받은 task 중 compositing에 해당하는 task만 view에 추가
        comp_task_id = gazu.task.get_task_type_by_name('Compositing')['id']
        for task in self.raw_todo_shots_list:
            if task.get('task_type_id') == comp_task_id:
                # 각 task를 TodoShot 객체로 생성
                todo_shot = TodoShot(task)
                shot_thumbnail = self.get_thumbnail(todo_shot.preview_file_url)

                # TodoShot 객체에 done_comp_tasks 값 set
                status_list = task_service.get_all_status(task)
                todo_shot.done_comp_tasks = self.check_tasks_all_done(status_list)

                # 정보가 저장된 todo_shot를 전역적으로 사용하기위해 todo_shots_obj 리스트에 추가
                filtered_todo_shots.append(todo_shot)
        task_service.clear_data()
        return filtered_todo_shots

    def load_shots_to_view(self, todo_shots):
        # 모델의 기존 데이터 리셋 후 update
        self.model.beginResetModel()
        self.model.todo_shots = []

        for todo_shot in todo_shots:
            # 모델에 데이터 추가
            shot_thumbnail = self.get_thumbnail(todo_shot.preview_file_url)
            self.model.todo_shots.append([
                f'{todo_shot.project_name}/{todo_shot.sequence_name}/{todo_shot.shot_name}', shot_thumbnail])
        self.model.endResetModel()

    def check_tasks_all_done(self, status_list) -> bool:
        all_true = True
        for status in status_list:
            if not status:
                all_true = False
                break
        return all_true

    def total_assigned_shot_num(self):
        assigned_shot_num = len(self.model.todo_shots)
        return assigned_shot_num

    def shot_clicked(self):
        _index = self.view.shot_list.selectedIndexes()
        if _index:
            index = _index[0]
            selected_shot = self.model.todo_shots[index.row()]
            selected_shot_info = selected_shot[0]  # selected_shot[0]은 text info, selected_shot[1]은 thumbnail pixmap
            self.clear_shot_detail_info()
            self.clicked_shot_detail_info(selected_shot_info)

    def clear_shot_detail_info(self):
        self.view.label_proj.setText("")
        self.view.label_seq.setText("")
        self.view.label_shot.setText("")
        # self.view.label_proj.setText(comp_shot.nb_frames)
        self.view.label_frame_in.setText("")
        self.view.label_frame_out.setText("")
        self.view.label_resolution.setText("")
        self.view.label_fps.setText("")
        self.view.label_revision.setText("")

    def clicked_shot_detail_info(self, selected_item):

        # 선택한 샷 정보 받아 오기
        self.project, self.sequence, self.shot = selected_item.split('/')

        # send selected_item to task_service
        self.task_service.load_tasks(self.project, self.sequence, self.shot)

        # 선택한 샷 CompShot 객체로 생성
        comp_shot = CompShot(self.shot)

        # UI에 data set
        self.view.label_proj.setText(comp_shot.project_name)
        self.view.label_seq.setText(comp_shot.sequence_name)
        self.view.label_shot.setText(comp_shot.shot_name)
        # self.view.label_proj.setText(comp_shot.nb_frames)
        self.view.label_frame_in.setText(comp_shot.frame_in)
        self.view.label_frame_out.setText(comp_shot.frame_out)
        self.view.label_resolution.setText(comp_shot.resolution)
        self.view.label_fps.setText(comp_shot.fps)
        self.view.label_revision.setText(f'ver {comp_shot.revision}.')

        thumbnail = self.get_thumbnail(comp_shot.preview_file_url)
        self.view.thumbnail_label.adjustSize()
        self.view.thumbnail_label.setPixmap(thumbnail.scaled(400, 200, Qt.KeepAspectRatio))

    def get_thumbnail(self, thumb_url) -> QPixmap:
        if thumb_url == "":
            return self.get_default_thumbnail()
        else:
            # 썸네일 데이터를 url을 통해 받아오기
            thumbnail_data = gazu.client.get_file_data_from_url(thumb_url)
            # 이미지 url을 pixmap으로 변환하기
            pixmap = QPixmap()
            pixmap.loadFromData(thumbnail_data)
            QPixmapCache.insert(thumb_url, pixmap)
            return pixmap

    def get_default_thumbnail(self) -> QPixmap:
        default_thumbnail = QPixmap.fromImage(default_img)
        return default_thumbnail

    def sort_by_combobox(self):
        # self.update_compositing_todo_shots(task_service)
        temp_list = list(self.filtered_todo_shots)
        sorted_shot_list = []

        sorting_option = self.view.sorted_comboBox.currentText()
        if sorting_option == 'Name':
            sorted_shot_list = sorted(temp_list, key=self.sort_by_name)
        elif sorting_option == 'Due date':
            sorted_shot_list = sorted(temp_list, key=self.sort_by_due_date)
        elif sorting_option == 'Priority':
            sorted_shot_list = sorted(temp_list, key=self.sort_by_priority)

        # sorted_shot_list로 데이터 set
        self.load_shots_to_view(sorted_shot_list)

    def sort_by_name(self, item):
        return item.project_name, item.sequence_name, item.shot_name, item.due_date

    def sort_by_due_date(self, item):
        return item.due_date, item.project_name, item.sequence_name, item.shot_name,

    def sort_by_priority(self, item):
        return not item.done_comp_tasks, item.project_name, item.sequence_name, item.shot_name, item.due_date

    def on_custom_context_menu_requested(self, pos):
        index = self.view.shot_list.indexAt(pos)
        if not index.isValid():
            return

        # 선택한 샷이 속한 디렉토리 path 정보 받아 오기
        comp_shot_dir_path = self.get_comp_shot_dir_path(index)

        context_menu = QMenu(self.view)
        file_open_action = context_menu.addAction("open in Files")

        action = context_menu.exec_(QCursor.pos())
        if action == file_open_action:
            self.open_comp_shot_dir(comp_shot_dir_path)

    def get_comp_shot_dir_path(self, index):
        self.project, self.sequence, self.shot = index.data().split('/')
        comp_shot = CompShot(self.shot)
        comp_shot_dir_path = os.path.dirname(comp_shot.file_path)

        return comp_shot_dir_path

    def open_comp_shot_dir(self, comp_shot_dir_path):
        filters = ';;'.join(FILE_FILTERS)
        print("file path:", comp_shot_dir_path)
        # 해당 파일이 없을 시
        if comp_shot_dir_path == '':
            QMessageBox.information(self.view, "Message", "file doesn't exists")
            return

        file_name = QFileDialog.getOpenFileName(self.view, 'open in Files', comp_shot_dir_path,
                                                filter=filters)
        if file_name == "":
            return
        print("Selected File:", file_name)

    def handle_tree_item_clicked(self, text):
        # Find and select matching item in ListWidget
        count = 0
        for count in range(len(self.model.todo_shots)):
            selected_shot = self.model.todo_shots[count]
            selected_shot_info = selected_shot[0]  # selected_shot[0]은 text info, selected_shot[1]은 thumbnail pixmap

            if text in selected_shot_info:
                index = self.model.index(count, 0)
                self.view.shot_list.setCurrentIndex(index)

                self.clear_shot_detail_info()
                self.clicked_shot_detail_info(selected_shot_info)
