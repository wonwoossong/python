#자동 스크린샷 캠쳐하는법
import time
from PIL import ImageGrab

time.sleep(5)#5초 대기 사용자가 준비하는 시간 

for i in range(1,11): #2초 간격으로 10 개 이미지 저장
    img=ImageGrab.grab()#현제 스크린 이미지를 가져옴 
    img.save("iamge{}.png".format(i))#파일로 저장 (image1.png~image10.png)
    time.sleep(2)#2초 단위 