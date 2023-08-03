import gazu

gazu.client.set_host("http://192.168.3.117/api")
gazu.log_in("admin@netflixacademy.com", "netflixacademy")

def update_filetree(mountpoint, root):
    """
    파일 트리를 업데이트하는 매서드

    Args:
        mountpoint(str/path): 폴더 트리를 생성할 위치의 전체 경로
        root(str/folder name): 폴더 트리를 생성할 mountpoint의 자식 폴더 이름
    """


    tree = {
        "working": {
            "mountpoint": mountpoint,
            "root": root,
            "folder_path": {
                "shot": "<Project>/shots/<Sequence>/<Shot>/<TaskType>/working/v<Revision>",
                "asset": "<Project>/assets/<AssetType>/<Asset>/<TaskType>/working/v<Revision>",
                "style": "lowercase"
            },
            "file_name": {
                "shot": "<Project>_<Sequence>_<Shot>_<TaskType>_<Revision>",
                "asset": "<Project>_<AssetType>_<Asset>_<TaskType>_<Revision>",
                "style": "lowercase"
            }
        },
        "output": {
            "mountpoint": mountpoint,
            "root": root,
            "folder_path": {
                "shot": "<Project>/shots/<Sequence>/<Shot>/<TaskType>/output/<OutputType>/v<Revision>",
                "asset": "<Project>/assets/<AssetType>/<Asset>/<TaskType>/output/<OutputType>/v<Revision>",
                "style": "lowercase"
            },
            "file_name": {
                "shot": "<Project>_<Sequence>_<Shot>_<OutputType>_v<Revision>",
                "asset": "<Project>_<AssetType>_<Asset>_<OutputType>_v<Revision>",
                "style": "lowercase"
            }
        }
    }
    project = gazu.project.get_project_by_name('movie2')
    print(project)
    gazu.files.update_project_file_tree(project, tree)


update_filetree('/home/rapa/kitsu', 'nuki')

project = gazu.project.get_project_by_name('movie2')
print(project)

'''
{'name': 'movie2', 'code': None, 'description': None, 'shotgun_id': None, 'file_tree': None, 
'data': None, 'has_avatar': False, 'fps': '25', 'ratio': '16:9', 'resolution': '1920x1080', 
'production_type': 'short', 'production_style': '2d', 'start_date': '2023-08-01', 'end_date': '2023-08-26', 
'man_days': None, 'nb_episodes': 0, 'episode_span': 0, 'max_retakes': 0, 'is_clients_isolated': False, 
'project_status_id': 'a98c1bcf-eed1-441a-b9ec-8d9868cd542d', 'id': '75340333-e486-40f1-b132-5c3740a016f8', 
'created_at': '2023-08-03T06:20:48', 'updated_at': '2023-08-03T06:20:49', 'type': 'Project'}


{'name': 'movie2', 'code': None, 'description': None, 'shotgun_id': None, 
'file_tree': {'output': {'root': 'nuki', 'file_name': {'shot': '<Project>_<Sequence>_<Shot>_<OutputType>_v<Revision>', 
'asset': '<Project>_<AssetType>_<Asset>_<OutputType>_v<Revision>', 'style': 'lowercase'}, 'mountpoint': '/home/rapa/kitsu', 
'folder_path': {'shot': '<Project>/shots/<Sequence>/<Shot>/<TaskType>/output/<OutputType>/v<Revision>', 
'asset': '<Project>/assets/<AssetType>/<Asset>/<TaskType>/output/<OutputType>/v<Revision>', 'style': 'lowercase'}}, 
'working': {'root': 'nuki', 'file_name': {'shot': '<Project>_<Sequence>_<Shot>_<TaskType>_<Revision>', 
'asset': '<Project>_<AssetType>_<Asset>_<TaskType>_<Revision>', 'style': 'lowercase'}, 'mountpoint': '/home/rapa/kitsu', 
'folder_path': {'shot': '<Project>/shots/<Sequence>/<Shot>/<TaskType>/working/v<Revision>', 
'asset': '<Project>/assets/<AssetType>/<Asset>/<TaskType>/working/v<Revision>', 'style': 'lowercase'}}}, 
'data': None, 'has_avatar': False, 'fps': '25', 'ratio': '16:9', 'resolution': '1920x1080', 
'production_type': 'short', 'production_style': '2d', 'start_date': '2023-08-01', 'end_date': '2023-08-26', 
'man_days': None, 'nb_episodes': 0, 'episode_span': 0, 'max_retakes': 0, 'is_clients_isolated': False, 
'project_status_id': 'a98c1bcf-eed1-441a-b9ec-8d9868cd542d', 'id': '75340333-e486-40f1-b132-5c3740a016f8', 
'created_at': '2023-08-03T06:20:48', 'updated_at': '2023-08-03T06:23:09', 'type': 'Project'}
'''