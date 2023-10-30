# NUKI
> Nuki is a **Nuke-Kitsu** integration tool.

> It streamlines compositing workflows by seamlessly connecting **Nuke** with **Kitsu** project management platform.


***


![스크린샷, 2023-08-17 16-46-55](https://github.com/SongmiLim/Nuki/assets/99317323/561f2460-aa33-4db3-ae7b-4855a9add461)
![1](https://github.com/SongmiLim/nuki_project/assets/64101533/7bdc2f5a-f292-4830-bae7-16750827ab18)


NUKI helps compositing artists automate work environment setup and manage the export and publishing of their compositions.


NUKI enables compositors to log in to Kitsu within Nuke, access shot details, monitor job progress, import jobs from Kitsu, publish completed work, and automatically convert it to JPG and MOV.





## What's inside?
1. User Login
  - Users can log in using their Kitsu ID within Nuke.
2. Viewing Shots Assigned to Compositing Artists
  - Artists can view all shots assigned to them.
3. Shot Sorting Function
  - Artists can sort their assigned shots by Name, Due Date, and Priority.
4. Providing Detailed Shot Information.
  - When artists click on a specific shot, they can view detailed information about the shot, such as Frame Range, Resolution, FPS, and Revision.
5. Checking Task Status for a Shot
  - Clicking on a shot allows users to check the progress of tasks related to that shot.
6. Importing Work for Each Task
  - Users can convert the work for each task into Nuke nodes and open them in Nuke files.
7. Exporting After Completing Work
  - After completing their work, artists can export it as JPG or MP4 files and save them in the local file tree.
8. Publishing Completed Work to Kitsu
  - Users can publish the exported files to Kitsu after completing the work.


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


