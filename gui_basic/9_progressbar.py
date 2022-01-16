import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk()
root.title("NADO GUI")#title
root.geometry("640x480")# 가로 * 세로
#프로그레스바란 진행 상태
#ex) 설치 몇프로 
# progressbar=ttk.Progressbar(root,maximum=100,mode="indeterminate")#모드 결정되지않음
# progressbar=ttk.Progressbar(root,maximum=100,mode="determinate")
# progressbar.start(10)#10 ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop()# 작동 중지 멈추면서 값이 사라짐

# btn=Button(root,text="중지",command=btncmd)
# btn.pack()

p_var2=DoubleVar()#실수값으로 설정
progressbar2=ttk.Progressbar(root,maximum=100,length=150,variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(101):#0~100
        time.sleep(0.01)#0.01 초 대기

        p_var2.set(i)#progress_var 값 설정
        progressbar2.update()# for 문 동작마다 업데이트가 된다
        print(p_var2.get())
btn=Button(root,text="시작",command=btncmd2)
btn.pack()
root.mainloop()