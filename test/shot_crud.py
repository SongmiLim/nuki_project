import gazu

class MyGazu:
    __project = None
    __sequence = None
    __shot = None
    __asset = None
    __task_type = None
    __task = None
    __entity = None

    def __init__(self):
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
        self.__shot = gazu.shot.get_shot_by_name(self.sequence, name)
        self.__entity = self.__shot

    @property
    def asset(self):
        return self.__asset

    @asset.setter
    def asset(self, name):
        self.__asset = gazu.asset.get_asset_by_name(self.project, name)
        self.__entity = self.__asset

    @property
    def task_type(self):
        return self.__task_type

    @task_type.setter
    def task_type(self, name):
        self.__task_type = gazu.task.get_task_type_by_name(name)

    @property
    def task(self):
        return self.__task

    @task.setter
    def task(self, name):
        self.task_type = name
        self.__task = gazu.task.get_task_by_name(self.__entity, self.task_type)


    # 나에게 할당된 모든 task 가져오기
    def get_my_all_task(self):
        tasks = gazu.user.all_tasks_to_do()

        self.comp_task_id = gazu.task.get_task_type_by_name('Compositing')['id']

        for i in tasks:
            # task_type이 compositing이 아닐 시 continue
            if i.get('task_type_id') != self.comp_task_id:
                continue
            project_name = i.get('project_name')
            # sequence name은 바로 가져올수 없는듯...?    => 있음,, 맨 마지막에 있었음,,,,,
            sequence_name = i.get('sequence_name')
            shot_name = i.get('entity_name')
            print(f'{project_name}/{sequence_name}/{shot_name}')

    def clicked_shot_detail_info(self):
        # clicked event 발생 시 선택된 객체로 setting
        # 지금은 일단 임의로 설정해줌
        gz.project = "avengers"
        gz.sequence = "SEQ01"
        gz.shot = "SH01"
        gz.task = "Compositing"

        shot_info = gz.shot.get('data')

        project_name = shot_info.get('project_name')
        sequence_name = shot_info.get('sequence_name')
        shot_name = shot_info.get('name')
        nb_frames = gz.shot.get('nb_frames')
        frame_in = shot_info.get('frame_in')
        frame_out = shot_info.get('frame_out')
        resolution = shot_info.get('resolution')
        fps = shot_info.get('fps')
        revision = shot_info.get('max_retakes')  # 이 데이터 맞는지 모르겠음
        created_at = shot_info.get('created_at')
        updated_at = shot_info.get('updated_at')
        preview_file_id = shot_info.get('preview_file_id')
        preview_file_url = gazu.files.get_preview_file_url(preview_file_id)

        print(f'PROJECT {project_name}')
        print(f'SEQUNECE {sequence_name}')
        print(f'SHOT {shot_name}')
        print(f'NUMBER OF FRAMES {nb_frames}')
        print(f'FRAME RANGE {frame_in}     {frame_out}')
        print(f'RESOLUTION {resolution}')
        print(f'FPS {fps}')
        print(f'REVISION {revision}')
        print(f'CREATED AT {created_at}')
        print(f'UPDATED AT {updated_at}')
        print(f'{gz.host}/{preview_file_url}')


if __name__ == "__main__":
    gz = MyGazu()
    gz.get_my_all_task()
    print("--------------")
    gz.clicked_shot_detail_info()
