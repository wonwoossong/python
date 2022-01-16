from tkinter import *

root = Tk()
root.title("NADO GUI")#title
# root.geometry("640x480")# 가로 * 세로
root.geometry("640x480+300+100")# 가로 * 세로 + x 좌표 + y 좌표 나타나는 위치
root.resizable(True,True)#너비 높이 변경 불가 

root.mainloop()