import gazu.task
import os
import json

from PySide2 import QtWidgets, QtGui, QtCore

from .exceptions import *


def print_align(content, keys=None):
    if type(content) == dict:
        if not keys:
            keys = content.keys()
        print('   {')
        for key, value in content.items():
            if key in keys:
                print(f'\t"{key}":{value}')
        print('   }')
        return
    if type(content) == list:
        print('[')
        for i in content:
            print(f'index-{content.index(i)}')
            print_align(i, keys)
        print(']')
        return


def print_info(content):
    if type(content) == list:
        print(f"dict_count: {len(content)}")
        if len(content):
            print(f"dict_len: {len(content[0])}")
        return


def user_info_tree(comptasks):
    """
    list : 로그인 된 'user'를 기준으로 정렬된 프로젝트, 시퀀스, 테스크

    user를 기준으로 CompTask를 활용해서 사용자(아티스트)가 할당 되어 있는 task를 tree형태로 보여 준다.

    """
    result_dict = {}
    for comp_task in comptasks:
        proj_name = comp_task.proj_name
        seq_name = comp_task.seq_name
        if proj_name not in result_dict:
            result_dict[proj_name] = {}
        if seq_name not in result_dict[proj_name]:
            result_dict[proj_name][seq_name] = []
        result_dict[proj_name][seq_name].append(comp_task.shot_name)

    return result_dict


def construct_full_path(file: dict):
    """
    output file이나 working file의 딕셔너리를 받아서 확장자까지 연결된 full path를 반환

    Args:
        file(dict):working file 혹은 output file dict

    Returns:
        str: file의 실제 절대경로
                {dir_name}/{file_name}.{extension}
            확장자가 레스터 이미지 확장자인 경우, padding을 포함
                {dir_name}/{file_name}.####.{extension}
    """
    path = file.get('path')
    file_type = file.get('type')
    padding = '.'
    if file_type == 'WorkingFile':
        software_id = file.get('software_id')
        ext = gazu.files.get_software(software_id).get('file_extension')
    elif file_type == 'OutputFile':
        output_type = file.get('output_type_id')
        ext = gazu.files.get_output_type(output_type).get('short_name')
        if ext in ['exr', 'dpx', 'jpg', 'jpeg', 'png', 'tga']:
            padding = '_####.'
    else:
        raise Exception('파일 딕셔너리가 아님')
    return path + padding + ext


def construct_initials(full_name: str):
    """
    full name을 입력받아 last name을 제외한 나머지를 축약해 반환
    반환되는 initials의 첫 글자는 대문자로 변환되며, '.'으로 구분됨

    Args:
        full_name(str): 띄어쓰기로 구분되는 전체 이름
            "Mohandas Karamchand gandhi"

    Returns:
        str: 축약된 initials
            "M.K.Gandhi"

    """
    if len(full_name) == 0:
        return
    initials = ""
    split_name = full_name.split(" ")
    for i in range(len(split_name)-1):
        initials += split_name[i][0].upper() + "."
    initials += split_name[-1][0].upper() + split_name[-1][1:]
    return initials

class OutlineDelegate(QtWidgets.QItemDelegate):
    """
    해당 delegate는 QTableView 또는 QTreeView 에서 선택된 item 의 테두리를 그리는 역할을 한다.

    Attributes:
        margin (int): 셀 상단과 테두리 사이의 거리
        radius (int): 둥근 모서리의 반
        border_color (QColor): 테두리 색상
        border_width (int): 테두리 너비

    Args:
        parent (QObject): delegate의 parent 객체
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.margin = 2
        self.radius = 10
        self.border_color = QtGui.QColor(238, 173, 83)
        self.border_width = 2

        parent.setItemDelegate(self)

    def sizeHint(self, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex):
        """
        테두리를 포함한 item의 size hint를 반환한다.
        """
        size = super().sizeHint(option, index)
        size = size.grownBy(QtCore.QMargins(0, self.margin, 0, self.margin))
        return size

    def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex):
        """
        item이 선택되었을 때 item에 테두리를 그린다.
        """
        painter.save()
        painter.setRenderHint(painter.Antialiasing)

        # Painter에 clipping rect 을 설정하여 테두리 밖에 그리는 것을 방지
        painter.setClipping(True)
        painter.setClipRect(option.rect)

        # 테두리를 고려하여 option.rect 을 조정한 뒤, 원래의 paint 메서드 호출
        option.rect.adjust(0, self.margin, 0, -self.margin)
        super().paint(painter, option, index)

        if option.state & QtWidgets.QStyle.State_Selected:
            pen = painter.pen()
            pen.setColor(self.border_color)
            pen.setWidth(self.border_width)
            painter.setPen(pen)

            rect = option.rect.adjusted(-self.border_width, 0, self.border_width, 0)
            painter.drawRect(rect)


        painter.restore()

