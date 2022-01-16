import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("NADO GUI")#title
root.geometry("640x480")# 가로 * 세로

values=[str(i) + "일" for i in range(1,32)]#1~31 
combobox=ttk.Combobox(root,height=5,values=values)
combobox.pack()
combobox.set("카드 결제일 ")#최초 목록 제목 설정 

readonly_combobox=ttk.Combobox(root,height=5,values=values,state="readonly")
readonly_combobox.current(0)#0번째 인덱스값 선택
readonly_combobox.pack()
#최초 목록 제목 설정 

def btncmd():
    print(combobox.get())#선택된 값을 출력
    print(readonly_combobox.get())
btn=Button(root,text="선택",command=btncmd)
btn.pack()
root.mainloop() 