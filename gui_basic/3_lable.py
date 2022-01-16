#lable 글자나 이미지를 보여주는 거고 실제로 동작하는것은 아니야
from tkinter import *

root = Tk()
root.title("NADO GUI")#title
root.geometry("640x480")

lable1=Label(root,text="안녕하세요")
lable1.pack()

photo=PhotoImage(file="gui_basic/image.png")
lable2 = Label(root, image=photo)
lable2.pack()

def change():
    lable1.config(text="또 만나요")

    global photo2#전역변수를 안해주면 garbage collection 이라는 애가 가져가ㅠ
    photo2=PhotoImage(file="gui_basic/image2.png")
    lable2.config(image=photo2)

btn=Button(root,text="클릭",command=change)
btn.pack()
root.mainloop()