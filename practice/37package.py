# # #모듈들을 모아둔것 
# # #travel "폴더를 만들었다"

# #import travel
# # import travel.thailand
# # trip_to = travel.thailand.ThailandPackage()
# # trip_to.detail()

# # from travel import vietnam
# # trip_to=vietnam.VietnmaPackage()
# # trip_to.detail()
# from travel import *

# # from travel import * # init 에 all 베트남 넣어서 쓸수 있는거래 
# trip_to=vietnam.VietnmaPackage()
# trip_to.detail()

# import inspect # 확인 하는방법 
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))