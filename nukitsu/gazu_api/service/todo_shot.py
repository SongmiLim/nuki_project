"""
작업자가 할당받은 모든 tasks(shots)에 대한 정보를 불러오기 위한 모듈
"""
import gazu
from PySide2.QtGui import QPixmap, QPixmapCache, QImage
import os
import datetime

basedir = os.path.dirname(__file__)
default_img = QImage(os.path.join(basedir, '../image/default.jpg'))


class TodoShot:
    def __init__(self, task) -> None:
        self._id = task.get('id')
        self._done_comp_tasks = None
        self._project_name = task.get('project_name')
        self._sequence_name = task.get('sequence_name')
        self._shot_name = task.get('entity_name')
        self._preview_file_id = task.get('entity_preview_file_id')
        self._preview_file_url = gazu.files.get_preview_file_url(self.preview_file_id) if self.preview_file_id != "" else ""
        self._preview_file_thumbnail = None
        self._due_date = task.get('due_date') if task.get('due_date') else ""

    @property
    def id(self):
        """
        Returns: 해당 shot 의 id
        """
        return self._id

    @property
    def project_name(self):
        """
        Returns: 해당 shot 의 project 명
        """
        return self._project_name

    @property
    def sequence_name(self):
        """
        Returns: 해당 shot 의 sequence 명
        """
        return self._sequence_name

    @property
    def shot_name(self):
        """
        Returns: 해당 shot 명
        """
        return self._shot_name

    @property
    def preview_file_id(self):
        return self._preview_file_id

    @property
    def preview_file_url(self):
        return self._preview_file_url

    @property
    def due_date(self):
        if self._due_date is "":
            # Return a date far in the future as a default value
            return str(datetime.datetime.max)
        return self._due_date

    @property
    def done_comp_tasks(self):
        """
        Returns:
            list: 사용자의 done compositing task 목록
        """
        return self._done_comp_tasks

    @done_comp_tasks.setter
    def done_comp_tasks(self, done_comp_tasks):
        """
        Returns:
            list: 사용자의 done compositing task 목록
        """
        self._done_comp_tasks = done_comp_tasks
