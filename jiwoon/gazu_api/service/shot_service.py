import gazu
from jiwoon.gazu_api.service.comp_shot import CompShot
from jiwoon.gazu_api.service.todo_shot import TodoShot
from jiwoon.gazu_api.model.shot_model import shotModel


class ShotService:
    __project = None
    __shot = None
    __sequence = None
    __task = None
    __task_type = None
    __task_status = None

    def __init__(self, model, view):
        self.model = model
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
        print(self.model.todo_shots)

    def clicked_shot_detail_info(self):
        # clicked event 발생 시 선택된 객체로 setting
        # 지금은 일단 임의로 설정해줌
        self.project = "avengers"
        self.sequence = "SEQ01"
        self.shot = "SH01"

        shot_info = self.shot.get('data')
        comp_shot = CompShot(shot_info)

        # print(f'PROJECT {comp_shot.project_name}')
        # print(f'SEQUENCE {comp_shot.sequence_name}')
        # print(f'SHOT {comp_shot.shot_name}')
        # print(f'NUMBER OF FRAMES {comp_shot.nb_frames}')
        # print(f'FRAME RANGE {comp_shot.frame_in} {comp_shot.frame_out}')
        # print(f'RESOLUTION {comp_shot.resolution}')
        # print(f'EXT {comp_shot.ext}')
        # print(f'FPS {comp_shot.fps}')
        # print(f'REVISION {comp_shot.revision}')
        # print(f'CREATED AT {comp_shot.created_at}')
        # print(f'UPDATED AT {comp_shot.updated_at}')
        # print(f'{self.host}/{comp_shot.preview_file_url}')


# if __name__ == "__main__":
#     model = shotModel()
#     s = ShotService(model)
#     s.get_all_tasks_todo()
