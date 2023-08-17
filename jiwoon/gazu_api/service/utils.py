import gazu.task
import os
import json
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



