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
    project = gazu.project.get_project_by_name('movie2')
    print(project)
    gazu.files.update_project_file_tree(project, tree)

update_filetree('/home/rapa/nuki', 'nuki project')

project = gazu.project.get_project_by_name('movie2')
print(project)