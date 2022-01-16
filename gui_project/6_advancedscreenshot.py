#사용자가 키 입력을 하면 낚아 채는것
import time
import keyboard
from PIL import ImageGrab
def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

keyboard.add_hotkey("F9", screenshot) # 사용자가 F9 키를 누르면 스크린샷 저장

keyboard.wait("esc") #esc키 누를때 까지 이걸 수행한다