import gazu
import glob
from nukitsu.gazu_api.service.comp_task import CompTask
from nukitsu.gazu_api.service.exceptions import WorkingFileExistsError
from nukitsu.gazu_api.service.nuke_function import *
from nukitsu.gazu_api.service.logger import Logger
from nukitsu.gazu_api.service.utils import construct_full_path

class Loader:

    def __init__(self):
        self.logger = Logger()
        self.working_file_path = None
        self.user = gazu.client.get_current_user()

    def open_nuke_working_file(self, comptask):
        """
        입력받은 CompTask의 task에 해당하는 working file(nuke)을 찾아 nuke window에 open 하는 함수.
        즉, 마지막 revision의 working nuke file 경로를 반환한다.
        만약 없다면 new_nuke_working_file을 실행시켜 새로 만든다.

        Args:
            comptask(CompTask): open하고자 하는 compositing task의 CompTask 객체
        """
        # clear_current_nuke_file()
        comptask = CompTask(comptask[0])
        last_working_file = gazu.files.get_last_working_file_revision(comptask.task_dict)
        print('last_working_file', last_working_file)
        return self.new_nuke_working_file(comptask)
        # if last_working_file:
        #     return self.new_nuke_working_file(comptask)
        self.working_file_path = construct_full_path(last_working_file)
        print('working_file', self.working_file_path)

        # nuke.scriptOpen('/home/rapa/jw_test/kitsu/glass_onion_a_knives_out_mystery/shots/sq01/sh01/sh01.nknc')
        # nuke.scriptReadFile('/home/rapa/jw_test/kitsu/glass_onion_a_knives_out_mystery/shots/sq01/sh01/layout/working/v018/glass_onion_a_knives_out_mystery_sq01_sh01_layout_0018.nk')
        # open_current_nuke_file(self.working_file_path)

        return last_working_file

    def new_nuke_working_file(self, comptask, name='main', comment='') -> dict:
        """
        입력받은 CompTask의 task에 대해 Kitsu DB상에 새로운 working file을 생성하는 함수.
        outputfile 만들 때 쓰일 dictionary 형태 working file을 반환한다.
        open_new_nuke_working_file()를 실행시켜 실제 nuke script를 저장한다.

        Args:
            comptask(nuki.CompTask): 생성하고자 하는 compositing task의 CompTask 객체
            name(str, optional): working file dict의 이름, 기본값 "main"
            comment(str, optional): working file dict의 설명

        Returns:
            working_file (dict)
        """
        # nuke = gazu.files.get_software_by_name('nuke')
        # gazu.files.new_software('nuki','nk','nk')
        nukenc = gazu.files.get_software_by_name('nuki')
        working_file = gazu.files.new_working_file(comptask.task_dict, name=name, comment=comment,
                                                   software=nukenc, person=self.user)
        self.working_file_path = construct_full_path(working_file)  # arg : working_file or output_file
        root_dir = os.path.dirname(self.working_file_path)
        file_name = os.path.basename(self.working_file_path)

        if not os.path.isdir(root_dir):
            os.makedirs(root_dir)

        for file in os.listdir(root_dir):
            if file == file_name:
                raise WorkingFileExistsError("Already exists working file")

        print('root_dir', root_dir)
        print('file_name', file_name)

        project_setting(comptask)
        save_script(self.working_file_path)
        self.logger.create_working_file_log(self.user.get('full_name'), self.working_file_path)

        return working_file

    def create_nodes(self, info_dict):
        create_nodes(info_dict,
                     lambda task_path: self.logger.load_output_file_log(self.user.get('full_name'), task_path))

    def update_nodes(self, info_dict):
        update_nodes(info_dict,
                     lambda task_path: self.logger.load_output_file_log(self.user.get('full_name'), task_path))

    def set_nuke_command(self, version, nuke_command, nc, nukex):
        """
        Returns the Nuke comment currently installed inside the opt folder.
        nuke_path가 있으면 그대로 실행, 없다면 찾아서 실행

        Args:
            nc (bool): Use non-commercial
            nukex (bool): Use nukeX

        Raises:
            Exception: Can not find nuke path

        Returns:
            str: nuke_command
        """

        # version이 float인지 아닌지 확인
        if isinstance(version, float):
            # 해당 버전의  Nuke 실행 파일 리스트에 추가됨
            nuke_path = glob.glob('/opt/**/Nuke{0}'.format(version))
        # 직접 입력했으면 nuke_path 설정
        elif nuke_command:
            nuke_path = []
            if os.path.isfile(nuke_command):
                nuke_path.append(nuke_command)
        else:
            raise InvalidNukePathError('Can not find nuke path')

        # 해당 버전 누크가 없으면 에러 발생
        if not nuke_path:
            raise InvalidNukePathError('Can not find nuke path')
        # 실행문 완성
        if nc:
            nuke_path.append('--nc')
        if nukex:
            nuke_path.append('--nukex')
        self.nuke_command = ' '.join(nuke_path)

        return self.nuke_command
