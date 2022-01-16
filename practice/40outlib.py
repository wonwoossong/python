#list of python modules 어떠한 외장함수가 있는지 알수있다 
# glob : 경로 내의 폴더 파일 목록 조회
# import glob 
# print(glob.glob("*.py"))

#os : 운영 체제에서 제공하는 기본 기능 
# import os 
# print(os.getcwd())#현재 디렉토리 표시

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다")
#     os.rmdir(folder)
#     print(folder,"폴더를 삭제하였습니다")
# else:
#     os.makedirs(folder)
#     print("폴더를 생성하였습ㄴ디ㅏ")

# print(os.listdir())

#시간을 표시하는 함수
# import time 
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%m:%S"))

import datetime
print("오늘 날짜는",datetime.date.today())

#timedelta : 두 날짜 사이에 간격
today=datetime.date.today()
td=datetime.timedelta(days=100)
print("우리가 만난지 100일은",today+td)