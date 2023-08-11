import gazu

gazu.client.set_host("http://192.168.3.117/api")
gazu.log_in("admin@netflixacademy.com", "netflixacademy")

def update_filetree(mountpoint, root):
    # 파일 트리를 업데이트 하는 매서드
    tree = {
        "working": {
            "mountpoint": mountpoint,
            "root": root,
            "folder_path": {
                "shot": "<Project>/<Sequence>/<Shot>/<TaskType>/working/v<Revision>",
                "asset": "<Project>/assets/<AssetType>/<Asset>/<TaskType>/working/v<Revision>",
                "style": "lowercase"
            },
            "file_name": {
                "shot": ""
                # "asset": "<Project>_<AssetType>_<Asset>_<TaskType>_<Revision>",
                # "style": "lowercase"
            }
        },
        "output": {
            "mountpoint": mountpoint,
            "root": root,
            "folder_path": {
                "shot": "<Project>/<Sequence>/<Shot>/<TaskType>/output/v<Revision>/<OutputType>",
                "asset": "<Project>/assets/<AssetType>/<Asset>/<TaskType>/output/<OutputType>/v<Revision>",
                "style": "lowercase"
            },
            "file_name": {
                "shot": ""
                # "asset": "<Project>_<AssetType>_<Asset>_<OutputType>_v<Revision>",
                # "style": "lowercase"
            }
        }
    }
    # open project 함수를 써서 전부 다 파일 트리를 생성할 수 있지만, 다른팀과 같이 써야하므로 각각 프로젝트명으로 파일트리 생성해줌
    project = gazu.project.get_project_by_name('movie')
    # print(project)
    gazu.files.update_project_file_tree(project, tree)

update_filetree('/home/rapa/nuki', 'nuki_project')

# 파일트리가 잘 생성 되었는지 확인하는 코드
project = gazu.project.get_project_by_name('movie')
# print(project)