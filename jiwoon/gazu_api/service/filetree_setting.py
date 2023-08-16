import gazu
import os

class FileTreeSetting:
    def __init__(self):
        gazu.client.set_host("http://192.168.3.117/api")
        gazu.log_in("admin@netflixacademy.com", "netflixacademy")
        # gazu.log_in("tumemanque00@netflixacademy.com", "gjehrud1006")

        # project_name = 'movie'
        # seq_name = 'SQ01'
        # shot_name = 'SH03'
        #
        # self.project = gazu.project.get_project_by_name(project_name)
        # print(f'project : {self.project}')
        # self.sequence = gazu.shot.get_sequence_by_name(self.project, seq_name)
        # print(f'sequence : {self.sequence}')
        # self.shot = gazu.shot.get_shot_by_name(self.sequence, shot_name)
        # print(f'shot : {self.shot}')

    def user_tasks_filetree(self):
        tasks = gazu.user.all_tasks_to_do()
        print(tasks)
        for i in tasks:
            if i['task_type_name'] == 'Compositing': # 'Compositing' 으로 할당 된 것만
                project_name = i['project_name']
                print('project name : ', project_name)
                seq_name = i['sequence_name']
                shot_name = i['entity_name']
                self.task_name = i['task_type_name']

                self.project = gazu.project.get_project_by_name(project_name)
                print(f'project : {self.project}')
                self.sequence = gazu.shot.get_sequence_by_name(self.project, seq_name)
                print(f'sequence : {self.sequence}')
                self.shot = gazu.shot.get_shot_by_name(self.sequence, shot_name)
                print(f'shot : {self.shot}')

                self.create_workingfile()

    def create_workingfile(self):
        self.task_type = None
        task_types = gazu.task.all_task_types_for_project(self.project)
        for self.task_type in task_types:
            if self.task_type['name'] == self.task_name and self.task_type['for_entity'] == self.shot['type']:
                self.task_type = self.task_type
                # print(f'task_type : {self.task_type}')
                self.task = gazu.task.get_task_by_name(self.shot, self.task_type)
                # print(f'task : {self.task}')

                # workingfile path
                self.working_file = gazu.files.new_working_file(self.task, person=None)
                print(f'working_file : {self.working_file}')
                # ouputfile 경로 생성
                self.outputfile_path()
                # working 폴더 생성
                self.make_folder_tree_working('/home/rapa/nuki/nuki_project')

    def create_outputfile(self): # 한번만 실행
        output_list = ['mp4', 'exr', 'jpg']
        for out in output_list:
            self.output_type_name = out
            self.output_type_short_name = out
            self.output_type = gazu.files.new_output_type(self.output_type_name, self.output_type_short_name)
            # print(f'output_type : {self.output_type}')


    def outputfile_path(self):
        # output_list = ['mp4', 'exr', 'jpg']
        # for out in output_list:
        if self.task_type['name'] == 'Compositing': # 'Compositing' 만 output 폴더 생성
            output_type = gazu.files.get_output_type_by_name('exr')
            # print(f'output_type : {output_type}')
            self.output_file = gazu.files.new_entity_output_file(self.shot, output_type, self.task_type, 'publish', working_file=self.working_file, revision=self.working_file['revision'])
            # print(f'output_file : {self.output_file}')
            # output 폴더 생성
            self.make_folder_tree_output('/home/rapa/nuki/nuki_project')


    def make_folder_tree_working(self, path):
        if os.path.exists(self.working_file['path']) is False:
            os.makedirs(self.working_file['path'])
            # print(f'working_file["path"] : {self.working_file["path"]}')
        else:
            print("폴더가 이미 존재합니다.")


    def make_folder_tree_output(self, path):
        if os.path.exists(self.output_file['path']) is False:
            os.makedirs(self.output_file['path'])
            # print(f'output_file["path"] : {self.output_file["path"]}')
        else:
            print("폴더가 이미 존재합니다.")

nk = FileTreeSetting()
nk.user_tasks_filetree() # 함수 들이 연결 되어 있어서 이 함수만 실행 하면 됨

# nk.create_outputfile() # 한번만 실행