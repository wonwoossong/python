from tkinter import *

root = Tk()
root.title("NADO GUI")#title
root.geometry("640x480")# 가로 * 세로
#스크롤바랑 리스트랑 같은 프레임에 위치시키게 그래서 root 가 아니라 frame이야
frame=Frame(root)
frame.pack()

scrollbar=Scrollbar(frame)
scrollbar.pack(side="right",fill="y")
#set 이 없으면 스크롤을 내려도 ㅇ다시 올라온다
listbox=Listbox(frame,selectmode="extended",height=10,yscrollcommand=scrollbar.set)
                                                        # 스크롤바가 그대로 있게 
for i in range(1,32):
    listbox.insert(END,str(i)+"일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)#스크롤바랑 숫자랑 일치시키게-
root.mainloop()