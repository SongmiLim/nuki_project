"""
특정 task(shot)에 대한 정보를 불러오기 위한 모듈
"""
import os
import gazu
# from .utils import construct_full_path
from datetime import datetime


class CompShot:
    def __init__(self, shot: dict) -> None:
        """
        클릭된 shot으로부터 각종 정보를 추출

        Args:
            shot(dict{dict}):  객체로 만들고자 하는 shot task의 dict
            반드시 asset이 아닌, shot을 entity로 하는 task여야 함
        """
        # if shot_info.get('entity_type_name') != 'Shot':
        #     raise Exception('shot을 위한 task가 아님')
        self.shot = shot
        self._project_name = shot.get('project_name')
        self._sequence_name = shot.get('sequence_name')
        self._shot_name = shot.get('name')
        self._preview_file_id = shot.get('preview_file_id')
        self._preview_file_url = gazu.files.get_preview_file_url(self.preview_file_id) if self.preview_file_id else ""
        self._revision = ""
        self._file_path = ""

        # shot detail data가 있을 경우 none값 가진 data validation
        if shot.get('data'):
            shot_detail_data = shot.get('data')
            self._nb_frames = shot_detail_data.get('nb_frames') if shot_detail_data.get('nb_frames') else ""
            self._frame_in = shot_detail_data.get('frame_in') if shot_detail_data.get('frame_in') else "0"
            self._frame_out = shot_detail_data.get('frame_out') if shot_detail_data.get('frame_out') else "0"
            self._resolution = shot_detail_data.get('resolution') if shot_detail_data.get('resolution') else ""
            self._ext = shot_detail_data.get('ext') if shot_detail_data.get('ext') else ""
            self._fps = shot_detail_data.get('fps') if shot_detail_data.get('fps') else ""
            self._created_at = shot_detail_data.get('created_at') if shot_detail_data.get('created_at') else ""
            self._updated_at = shot_detail_data.get('updated_at') if shot_detail_data.get('updated_at') else ""
            self._preview_file_id = shot_detail_data.get('preview_file_id') if shot_detail_data.get(
                'preview_file_id') else ""

        # shot에 detail data가 없을 경우
        else:
            self._nb_frames = "0"
            self._frame_in = "0"
            self._frame_out = "0"
            self._resolution = "-"
            self._ext = "0"
            self._fps = "-"
            self._created_at = ""
            self._updated_at = ""

    @property
    def project_name(self):
        return self._project_name

    @property
    def sequence_name(self):
        return self._sequence_name

    @property
    def shot_name(self):
        return self._shot_name

    @property
    def nb_frames(self):
        return self._nb_frames

    @property
    def frame_in(self):
        return self._frame_in

    @property
    def frame_out(self):
        return self._frame_out

    @property
    def resolution(self):
        return self._resolution

    @property
    def ext(self):
        return self._ext

    @property
    def fps(self):
        return self._fps

    @property
    def revision(self):
        return self._revision

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at

    @property
    def preview_file_id(self):
        return self._preview_file_id

    @property
    def preview_file_url(self):
        return self._preview_file_url

    @property
    def revision(self):
        # 최신 version을 알기 위해서는 task dict이 필요
        last_comp_task_revision_dict = self.get_task_dict()
        last_comp_task_revision = last_comp_task_revision_dict.get('revision')
        return str(last_comp_task_revision) if last_comp_task_revision else '1'


    @property
    def file_path(self):
        # 최신 version file의 path을 알기 위해서는 task dict이 필요
        last_comp_task_revision_dict = self.get_task_dict()
        last_comp_task_path = last_comp_task_revision_dict.get('path')
        return last_comp_task_path if last_comp_task_path else ''


    def get_task_dict(self) -> dict:
        tasks = gazu.task.all_tasks_for_shot(self.shot)
        for task in tasks:
            if task.get('task_type_name') == 'Compositing':
                last_comp_task_revision_dict = gazu.files.get_last_working_file_revision(task) or {}
                return last_comp_task_revision_dict
