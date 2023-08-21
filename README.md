# Kitsu-Nuke Integration Tool
개발 기간: 2023/07/06 ~ 2023/08/17


![스크린샷, 2023-08-17 16-46-55](https://github.com/SongmiLim/Nuki/assets/99317323/561f2460-aa33-4db3-ae7b-4855a9add461)


# 프로젝트 소개

Kitsu-Nuke 통합 도구는 누크(Nuke)와 키츄(Kitsu) 프로젝트 관리 플랫폼을 원활하게 연결하여 컴포지팅 아티스트의 작업 흐름을 강화하는 데 사용됩니다.


이 도구를 통해 작업자는 작업을 효율적으로 관리하고, 샷의 세부 정보에 접근하며, 작업 진행 상황을 모니터링하며, 작업물을 누크로 가져오고 완료된 작업물을 쉽게 내보내고 Kitsu에 게시할 수 있습니다.



## Features
User Login: Kitsu ID를 사용하여 도구에 로그인합니다.


View Assigned Shots: 할당된 샷을 찾아보고 정렬할 수 있습니다.


Shot Details: 샷을 클릭하여 상세 정보를 조회합니다.


Import to Nuke: 작업물을 Nuke 노드로 변환하여 Nuke에 띄워줍니다.


Task Completion: 작업물을 mov, exr 또는 jpg 형식으로 내보내고 로컬에 저장합니다.


Publishing: 완료된 파일을 Kitsu에 바로 publish 합니다.



# Requirements
python 3.6


# Installation
`pip install pyside2`


`pip install gazu`


`pip install nuke`


`git clone https://github.com/SongmiLim/nuki_project.git`



## Run the tool
`python main.py`


## 기술 스택
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black">
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">


