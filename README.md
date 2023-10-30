# NUKI
Nuki is a **Nuke-Kitsu** integration tool.

It is used to enhance the workflow of compositing artists by smoothly connecting **Nuke** tools with the **Kitsu** project management platform.

It supports compositing artists to automate work environment settings before starting, and export and publish after compositing.



NUKI allows compositers log in to Kitsu within Nuke, connect to Kitsu DB, access shot details, monitor job progress, import job via file path received from Kitsu, publish completed work to kitsu, and automatically convert to JPG and MOV.


![스크린샷, 2023-08-17 16-46-55](https://github.com/SongmiLim/Nuki/assets/99317323/561f2460-aa33-4db3-ae7b-4855a9add461)


## What's inside?
User Login: Kitsu ID를 사용하여 도구에 로그인합니다.


View Assigned Shots: 할당된 샷을 찾아보고 정렬할 수 있습니다.


Shot Details: 샷을 클릭하여 상세 정보를 조회합니다.


Import to Nuke: 작업물을 Nuke 노드로 변환하여 Nuke에 띄워줍니다.


Task Completion: 작업물을 mov, exr 또는 jpg 형식으로 내보내고 로컬에 저장합니다.


Publishing: 완료된 파일을 Kitsu에 바로 publish 합니다.



## Requirements
python 3.6, Pyside 2, Nuke API, Gazu API, ffmpeg


## Installation
`pip install pyside2`


`pip install gazu`


`pip install nuke`


`git clone https://github.com/SongmiLim/nuki_project.git`



## Run the tool
`python main.py`


## Development duration
06/07/2023 ~ 17/08/2023


## Technologies
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black">
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">


