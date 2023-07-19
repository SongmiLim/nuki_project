import gazu
from jiwoon.gazu_api.service.comp_shot import CompShot
from jiwoon.gazu_api.service.todo_shot import TodoShot
from jiwoon.gazu_api.model.shot_model import shotModel
from jiwoon.gazu_api.view.task_view import MainUI
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QPixmapCache
import os

basedir = os.path.dirname(__file__)
print(basedir)

class ShotService:
    __project = None
    __shot = None
    __sequence = None
    __task = None
    __task_type = None
    __task_status = None

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.host = gazu.client.set_host("http://192.168.3.117/api")
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

    def get_all_tasks_todo(self):
        todo_task_list = gazu.user.all_tasks_to_do()
        comp_task_id = gazu.task.get_task_type_by_name('Compositing')['id']

        for task in todo_task_list:
            if task.get('task_type_id') == comp_task_id:
                todo_shot = TodoShot(task)
                self.model.todo_shots.append(
                    f'{todo_shot.project_name}/{todo_shot.sequence_name}/{todo_shot.shot_name}')

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

    def shot_clicked(self, index):
        # shot_list에서 선택된 아이템의 인덱스 받기
        selected_item = self.view.shot_list.model().data(index, Qt.DisplayRole)
        # print("Selected index:", index.row())
        # print("Selected item text:", selected_item)
        self.clear_shot_detail_info()
        self.clicked_shot_detail_info(selected_item)

    def clicked_shot_detail_info(self, str):
        # 선택한 샷 정보 받아오기
        shot_info_list = str.split('/')
        self.project = shot_info_list[0]
        self.sequence = shot_info_list[1]
        self.shot = shot_info_list[2]
        # 선택한 샷 CompShot 객체로 생성
        comp_shot = CompShot(self.shot)

        # UI에 data 뿌리기
        self.view.label_proj.setText(comp_shot.project_name)
        self.view.label_seq.setText(comp_shot.sequence_name)
        self.view.label_shot.setText(comp_shot.shot_name)
        # self.view.label_proj.setText(comp_shot.nb_frames)
        self.view.label_frame_in.setText(comp_shot.frame_in)
        self.view.label_frame_out.setText(comp_shot.frame_out)
        self.view.label_resolution.setText(comp_shot.resolution)
        self.view.label_fps.setText(comp_shot.fps)
        self.view.label_revision.setText(comp_shot.revision)

        if comp_shot.preview_file_url == "":
            self.view.thumbnail_label.setText("No Image")
            # self.view.thumbnail_label.setPixmap(QPixmap('close.png').scaled(500, 200, Qt.KeepAspectRatio))

        else:
            url_data = gazu.client.get_file_data_from_url(comp_shot.preview_file_url)
            thumbnail = self.get_thumbnail(url_data, comp_shot.preview_file_url)

            self.view.thumbnail_label.adjustSize()
            self.view.thumbnail_label.setPixmap(thumbnail.scaled(500, 200, Qt.KeepAspectRatio))


    def get_thumbnail(self, url_data, thumb_url):
        # 이미지 url을 pixmap으로 변환하기
        pixmap = QPixmap()
        pixmap.loadFromData(url_data)
        QPixmapCache.insert(thumb_url, pixmap)
        return pixmap

# if __name__ == "__main__":
#     model = shotModel()
#     view = MainUI()
