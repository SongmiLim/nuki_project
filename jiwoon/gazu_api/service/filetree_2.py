import gazu
import os

class MyGazu:
    def __init__(self):
        gazu.client.set_host("http://192.168.3.117/api")
        gazu.log_in("admin@netflixacademy.com", "netflixacademy")

        project_name = 'movie2'
        seq_name = 'SQ01'
        shot_name = 'SH01'
        self.task_name = 'Compositing'
        self.output_type_name = 'EXR'
        self.output_type_short_name = 'EXR'
        self.user_comment = 'nuki1'
        self.status_name = 'wip'
        self.file_path = '/home/rapa/nuki/jiwoon/gazu_api/image/preview.jpg'

        self.project = gazu.project.get_project_by_name(project_name)
        print(f'project : {self.project}')
        self.sequence = gazu.shot.get_sequence_by_name(self.project, seq_name)
        print(f'sequence : {self.sequence}')
        self.shot = gazu.shot.get_shot_by_name(self.sequence, shot_name)
        print(f'shot : {self.shot}')


    def create_workingfile(self):
        self.task_type = None
        task_types = gazu.task.all_task_types_for_project(self.project)
        for self.task_type in task_types:
            if self.task_type['name'] == self.task_name and self.task_type['for_entity'] == self.shot['type']:
                self.task_type = self.task_type
                break
        self.task = gazu.task.get_task_by_name(self.shot, self.task_type)
        self.task_status_id = self.task['task_status_id']
        print(f'task : {self.task}')
        self.working_file = gazu.files.new_working_file(self.task)
        print(f'working_file : {self.working_file}')


    def type_outputfile(self):
        output_type = gazu.files.new_output_type(self.output_type_name, self.output_type_short_name)
        print(f'output_type : {output_type}')
        output_type = gazu.files.get_output_type_by_name('EXR')
        print(f'output_type : {output_type}')

        self.output_file = gazu.files.new_entity_output_file(self.shot, output_type, self.task_type,
                                          'publish', working_file=self.working_file, revision=self.working_file['revision'])
        print(f'output_file : {self.output_file}')

    def get_status(self):
        # self.status = None # 안 써도 되는 듯
        all_status = gazu.task.all_task_statuses()
        for st in all_status:
            if st.get('name') == self.status_name:
                out = st
                print(out)
                break
            if st.get('short_name') == self.status_name:
                out = st
                print(out)
                break

    def comment_previewpublish(self): # 두번째 self.task 에 task_status_id
        # comment = gazu.task.add_comment(self.task, self.task_status_id, comment=self.user_comment)
        # print(f'comment : {comment}')
        # preview = gazu.task.add_preview(self.task, comment, preview_file_path=self.file_path)
        preview = gazu.task.publish_preview(self.task, self.task_status_id, comment='hi3', preview_file_path=self.file_path)
        print(f'preview : {preview}')

    def make_folder_tree_working(self, path):
        if os.path.exists(self.working_file['path']) is False:
            os.makedirs(self.working_file['path'])
            print(f'working_file["path"] : {self.working_file["path"]}')
        else:
            print("폴더가 이미 존재합니다.")

    def make_folder_tree_output(self, path):
        if os.path.exists(self.output_file['path']) is False:
            os.makedirs(self.output_file['path'])
            print(f'output_file["path"] : {self.output_file["path"]}')
        else:
            print("폴더가 이미 존재합니다.")



gz = MyGazu()
gz.create_workingfile()
gz.type_outputfile()
gz.get_status()
gz.comment_previewpublish()
gz.make_folder_tree_working('/home/rapa/kitsu/nuki')
gz.make_folder_tree_output('/home/rapa/kitsu/nuki')