import gazu
import os

'''
task_types 중 컴프
{'name': 'Compositing', 'short_name': '', 'color': '#ff5252', 'priority': 7, 
'for_entity': 'Shot', 'allow_timelog': True, 'archived': False, 'shotgun_id': None, 
'department_id': '1a622adb-e5be-4664-ba82-bc5bbb63b092', 
'id': 'cf745bdb-7a15-484c-8298-64842624ae8e', 'created_at': '2023-06-21T19:02:07', 
'updated_at': '2023-06-21T19:02:07', 'type': 'TaskType'}
'''
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
        self.user_comment = 'do-kyung'
        self.status_name = 'wip'
        self.file_path = '/home/rapa/PycharmProjects/nuki/nuki_project/gazu/0020.jpg'

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

        gazu.files.new_entity_output_file(self.shot, output_type, self.task_type,
                                          'publish', working_file=self.working_file, revision=self.working_file['revision'])

    def get_status(self):
        # self.status = None # 안 써도 되는 듯?
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
        preview = gazu.task.publish_preview(self.task, self.task_status_id, comment='hi1', preview_file_path=self.file_path)
        print(f'preview : {preview}')

    def _make_folder_tree(self, path):
        if os.path.exists(self.working_file['path']) is False:
            os.makedirs(self.working_file['path'])
            print(f'working_file["path"] : {self.working_file["path"]}')
        else:
            print("폴더가 이미 존재합니다.")



gz = MyGazu()
gz.create_workingfile()
# gz.type_outputfile() # 한번만 실행
gz.get_status()
gz.comment_previewpublish()
gz._make_folder_tree('/home/rapa/kitsu/nuki')

# 로컬 폴더 구조 movie_sq01_sh02_compositing_010

'''
project : {'name': 'movie', 'code': None, 'description': None, 'shotgun_id': None, 'file_tree': {'output': {'root': 'nuki', 'file_name': {'shot': '<Project>_<Sequence>_<Shot>_<OutputType>_v<Revision>', 'asset': '<Project>_<AssetType>_<Asset>_<OutputType>_v<Revision>', 'style': 'lowercase'}, 'mountpoint': '/home/rapa/kitsu', 'folder_path': {'shot': '<Project>/shots/<Sequence>/<Shot>/<TaskType>/output/<OutputType>/v<Revision>', 'asset': '<Project>/assets/<AssetType>/<Asset>/<TaskType>/output/<OutputType>/v<Revision>', 'style': 'lowercase'}}, 'working': {'root': 'nuki', 'file_name': {'shot': '<Project>_<Sequence>_<Shot>_<TaskType>_<Revision>', 'asset': '<Project>_<AssetType>_<Asset>_<TaskType>_<Revision>', 'style': 'lowercase'}, 'mountpoint': '/home/rapa/kitsu', 'folder_path': {'shot': '<Project>/shots/<Sequence>/<Shot>/<TaskType>/working/v<Revision>', 'asset': '<Project>/assets/<AssetType>/<Asset>/<TaskType>/working/v<Revision>', 'style': 'lowercase'}}}, 'data': None, 'has_avatar': False, 'fps': '25', 'ratio': '16:9', 'resolution': '1920x1080', 'production_type': 'short', 'production_style': '2d', 'start_date': '2023-07-04', 'end_date': '2023-08-23', 'man_days': None, 'nb_episodes': 0, 'episode_span': 0, 'max_retakes': 0, 'is_clients_isolated': False, 'project_status_id': 'a98c1bcf-eed1-441a-b9ec-8d9868cd542d', 'id': '6f1f4eb5-23aa-4ebe-aad6-6be1f11bd334', 'created_at': '2023-07-27T07:45:24', 'updated_at': '2023-07-28T08:27:48', 'type': 'Project'}
sequence : {'id': 'ca1b5067-ab73-4d9d-8e27-75828e05f4a1', 'name': 'SQ01', 'code': None, 'description': '', 'shotgun_id': None, 'canceled': False, 'nb_frames': None, 'nb_entities_out': 0, 'is_casting_standby': False, 'status': 'running', 'project_id': '6f1f4eb5-23aa-4ebe-aad6-6be1f11bd334', 'entity_type_id': 'e235f927-bc65-40a5-89f6-6acd734d5f3e', 'parent_id': None, 'source_id': None, 'preview_file_id': None, 'data': {}, 'ready_for': None, 'created_at': '2023-07-27T07:45:45', 'updated_at': '2023-07-27T07:45:45', 'type': 'Sequence'}
shot : {'id': '17c2f9fd-d51c-4eae-8ba8-296e7776a1d9', 'name': 'SH02', 'code': None, 'description': None, 'shotgun_id': None, 'canceled': False, 'nb_frames': None, 'nb_entities_out': 0, 'is_casting_standby': False, 'status': 'running', 'project_id': '6f1f4eb5-23aa-4ebe-aad6-6be1f11bd334', 'entity_type_id': '1409f077-58e3-4457-93c9-3c47d9377da4', 'parent_id': 'ca1b5067-ab73-4d9d-8e27-75828e05f4a1', 'source_id': None, 'preview_file_id': None, 'data': None, 'ready_for': None, 'created_at': '2023-07-28T07:31:04', 'updated_at': '2023-07-28T07:31:04', 'type': 'Shot', 'project_name': 'movie', 'sequence_name': 'SQ01'}
task : {'name': 'main', 'description': None, 'priority': 0, 'duration': 0.0, 'estimation': 0.0, 'completion_rate': 0, 'retake_count': 0, 'sort_order': 0, 'start_date': None, 'due_date': None, 'real_start_date': '2023-07-28T07:31:17', 'end_date': None, 'last_comment_date': '2023-08-01T01:47:51', 'nb_assets_ready': 0, 'data': None, 'shotgun_id': None, 'project_id': '6f1f4eb5-23aa-4ebe-aad6-6be1f11bd334', 'task_type_id': 'cf745bdb-7a15-484c-8298-64842624ae8e', 'task_status_id': '88f0026b-0f5e-4c91-b89a-cc103a30a049', 'entity_id': '17c2f9fd-d51c-4eae-8ba8-296e7776a1d9', 'assigner_id': '8f70afe0-2227-463f-b056-262c5239b502', 'id': '3b852e35-46a8-4cd4-bc01-ab54bd0e0dbf', 'created_at': '2023-07-28T07:31:04', 'updated_at': '2023-08-01T01:47:51', 'type': 'Task'}
working_file : {'shotgun_id': None, 'name': 'main', 'description': None, 'comment': '', 'revision': 15, 'size': None, 'checksum': None, 'path': '/home/rapa/kitsu/nuki/movie/shots/sq01/sh02/compositing/working/v015/movie_sq01_sh02_compositing_015', 'data': None, 'task_id': '3b852e35-46a8-4cd4-bc01-ab54bd0e0dbf', 'entity_id': '17c2f9fd-d51c-4eae-8ba8-296e7776a1d9', 'person_id': '8f70afe0-2227-463f-b056-262c5239b502', 'software_id': 'd98ff7bd-b6f8-4a3f-ba96-991179c371e4', 'id': '1f86a35d-4cc7-4eb5-8d86-64cde9a01649', 'created_at': '2023-08-01T02:12:28', 'updated_at': '2023-08-01T02:12:28', 'type': 'WorkingFile'}
output_type : {'name': 'EXR', 'short_name': 'EXR', 'id': '2cd89ec0-87e2-4652-bda8-113aa7492741', 'created_at': '2023-07-28T08:30:58', 'updated_at': '2023-07-28T08:30:58', 'type': 'OutputType'}
output_type : {'name': 'EXR', 'short_name': 'EXR', 'id': '2cd89ec0-87e2-4652-bda8-113aa7492741', 'created_at': '2023-07-28T08:30:58', 'updated_at': '2023-07-28T08:30:58', 'type': 'OutputType'}
out : {'name': 'Work In Progress', 'archived': False, 'short_name': 'wip', 'color': '#3273dc', 'is_done': False, 'is_artist_allowed': True, 'is_client_allowed': True, 'is_retake': False, 'is_feedback_request': False, 'is_default': False, 'shotgun_id': None, 'id': '88f0026b-0f5e-4c91-b89a-cc103a30a049', 'created_at': '2023-06-21T19:02:07', 'updated_at': '2023-06-21T19:02:07', 'type': 'TaskStatus'}
comment : {'previews': [], 'mentions': [], 'acknowledgements': [], 'attachment_files': [], 'shotgun_id': None, 'object_id': '3b852e35-46a8-4cd4-bc01-ab54bd0e0dbf', 'object_type': 'Task', 'text': 'do-kyung', 'data': None, 'replies': [], 'checklist': [], 'pinned': None, 'task_status_id': '88f0026b-0f5e-4c91-b89a-cc103a30a049', 'person_id': '8f70afe0-2227-463f-b056-262c5239b502', 'preview_file_id': None, 'id': '3c33489b-81c7-4cc3-a8ee-3e214fb9b613', 'created_at': '2023-08-01T02:12:28', 'updated_at': '2023-08-01T02:12:28', 'type': 'Comment', 'task_status': {'name': 'Work In Progress', 'archived': False, 'short_name': 'wip', 'color': '#3273dc', 'is_done': False, 'is_artist_allowed': True, 'is_client_allowed': True, 'is_retake': False, 'is_feedback_request': False, 'is_default': False, 'shotgun_id': None, 'id': '88f0026b-0f5e-4c91-b89a-cc103a30a049', 'created_at': '2023-06-21T19:02:07', 'updated_at': '2023-06-21T19:02:07', 'type': 'TaskStatus'}, 'person': {'first_name': 'netflix', 'last_name': 'academy', 'email': 'admin@netflixacademy.com', 'phone': '', 'active': True, 'archived': False, 'last_presence': None, 'desktop_login': '', 'login_failed_attemps': 0, 'last_login_failed': '2023-07-31T02:00:54', 'totp_enabled': False, 'email_otp_enabled': False, 'fido_enabled': False, 'preferred_two_factor_authentication': None, 'shotgun_id': None, 'timezone': 'Europe/Paris', 'locale': 'en_US', 'data': None, 'role': 'admin', 'has_avatar': False, 'notifications_enabled': False, 'notifications_slack_enabled': False, 'notifications_slack_userid': '', 'notifications_mattermost_enabled': False, 'notifications_mattermost_userid': '', 'notifications_discord_enabled': False, 'notifications_discord_userid': '', 'is_generated_from_ldap': False, 'id': '8f70afe0-2227-463f-b056-262c5239b502', 'created_at': '2023-07-20T01:06:14', 'updated_at': '2023-07-31T02:00:58', 'type': 'Person', 'full_name': 'netflix academy', 'fido_devices': []}}
preview : {'name': 'e1d90013-d816', 'original_name': '0010', 'revision': 6, 'position': 1, 'extension': 'png', 'description': None, 'path': None, 'source': 'webgui', 'file_size': 9621190, 'status': 'ready', 'validation_status': 'neutral', 'annotations': None, 'task_id': '3b852e35-46a8-4cd4-bc01-ab54bd0e0dbf', 'person_id': '8f70afe0-2227-463f-b056-262c5239b502', 'source_file_id': None, 'shotgun_id': None, 'is_movie': False, 'url': None, 'uploaded_movie_url': None, 'uploaded_movie_name': None, 'id': 'b0de8989-ade7-4889-9e31-d967f119d5ec', 'created_at': '2023-08-01T02:12:28', 'updated_at': '2023-08-01T02:12:29', 'type': 'PreviewFile'}
working_file["path"] : /home/rapa/kitsu/nuki/movie/shots/sq01/sh02/compositing/working/v015/movie_sq01_sh02_compositing_015
'''