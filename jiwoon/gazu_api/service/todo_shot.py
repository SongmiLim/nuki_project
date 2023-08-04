"""
작업자가 할당받은 모든 tasks(shots)에 대한 정보를 불러오기 위한 모듈
"""
import gazu
from PySide2.QtGui import QPixmap, QPixmapCache, QImage
import os

basedir = os.path.dirname(__file__)
default_img = QImage(os.path.join(basedir, '../image/default.jpg'))


class TodoShot:
    def __init__(self, task) -> None:
        self._id = task.get('id')
        # self._comp_tasks = None
        # self._todo_comp_tasks = None
        self._done_comp_tasks = None
        self._project_name = task.get('project_name')
        self._sequence_name = task.get('sequence_name')
        self._shot_name = task.get('entity_name')
        # self.comp_id = gazu.task.get_task_type_by_name('Compositing')['id']
        # self.test = None
        self._preview_file_id = task.get('entity_preview_file_id')
        self._preview_file_url = gazu.files.get_preview_file_url(
            self.preview_file_id) if self.preview_file_id != "" else ""
        self._preview_file_thumbnail = None
        self._due_date = task.get('due_date') if task.get('due_date') else ""
        # self.refresh_comp_tasks()


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
        return self._due_date

    # @property
    # def comp_tasks(self):
    #     """
    #     Returns:
    #         list: 사용자의 전체 compositing task 목록
    #     """
    #     return self._comp_tasks

    # @property
    # def todo_comp_tasks(self):
    #     """
    #     Returns:
    #         list: 사용자의 to_do compositing task 목록
    #     """
    #     return self._todo_comp_tasks
    #

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
    # def sorted_by_name(self):
    #     """
    #     Returns:
    #         list: 'name' 기준으로 정렬된 comp_tasks
    #     """
    #     return self.sort_by('name')
    #
    # @property
    # def sorted_by_due_date(self):
    #     """
    #     Returns:
    #         list: 'due_date' 기준으로 정렬된 comp_tasks
    #     """
    #     return self.sort_by('due_date')
    #
    # @property
    # def sorted_by_priority(self):
    #     """
    #     Returns:
    #         list: 'priority' 기준으로 정렬된 comp_tasks
    #
    #     'priority' 값은 0부터 3까지의 정수로 구성되어 있고,
    #     3이 가장 긴급한 우선순위를 나타내기 때문에 reverse가 True
    #     """
    #     return self.sort_by('priority', True)

    # @property
    # def is_comp_task_for_user(self):
    #     """
    #     Returns:
    #         bool: 사용자에게 할당된 comp task가 있는지 여부 반환
    #
    #     comp task가 하나라도 있으면 True, 아니면 False
    #     """
    #     if len(self.comp_tasks) == 0:
    #         return False
    #     return True
    #
    # def refresh_comp_tasks(self) -> None:
    #     """
    #     사용자의 comp task 를 새로 고침하여 comp_tasks에 반영
    #     """
    #     tasks = gazu.user.all_tasks_to_do()
    #     self._todo_comp_tasks = self.filter_tasks(tasks)
    #
    #     tasks = gazu.user.all_done_tasks()
    #     self._done_comp_tasks = self.filter_tasks(tasks)
    #
    #     # 나중에 comp_tasks 자체를 삭제할 예정
    #     self._comp_tasks = self.todo_comp_tasks + self.done_comp_tasks
    #
    # def filter_tasks(self, tasks: list) -> list:
    #     """
    #     입력된 task 중에서 comp task만 필터링하여 반환
    #
    #     Args:
    #         tasks(list[dict]): 전체 task들의 리스트
    #
    #     Returns:
    #         list[dict]: 필터링 된 comp task 리스트
    #     """
    #     res = []
    #     for i in tasks:
    #         if i.get('task_type_id') != self.comp_id:
    #             continue
    #         res.append(i)
    #     return res
    #
    # def sort_by(self, criterion, reverse=False) -> list:
    #     """
    #     기준(날짜 혹은 숫자)를 기준으로 정렬된 리스트 반환
    #
    #     Args:
    #         criterion(str): 기준으로 사용하고자 하는 key 값
    #             'due_date', 'start_date', 'updated_at', 'created_at', 'last_comment_date' 등
    #         reverse(bool): 정렬 순서 반전 여부를 결정
    #
    #     Returns:
    #         list[dict]: criterion을 기준으로 정렬된 리스트
    #     """
    #     return sorted(self._comp_tasks, key=lambda t: (t.get(criterion) is None, t.get(criterion)), reverse=reverse)
    #
    # def check_new_thing(self):
    #     """
    #     Kitsu 에 생긴 변경 사항을 gazu event를 활용하여, 변경 사항의 유무를 True, False로 반환하는 함수
    #     """
    #     # 기능 추가 예정
    #     pass
