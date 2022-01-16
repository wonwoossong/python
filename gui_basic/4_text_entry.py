# from tkinter import *

# root = Tk()
# root.title("NADO GUI")#title
# root.geometry("640x480")# 가로 * 세로

# txt=Text(root,width=30,height=5)#텍스트 위젯이 만들어졌다
# txt.pack()
# txt.insert(END,"글자를 입력하세요")#기본값을 미리 지정해줄수있다

# e=Entry(root,width=30)#한줄로 입력받을때 엔터가 안돼
# e.pack()
# e.insert(0,"한줄만 입력해요")


# # button 을 클릭했을때 text와 entry 값을 가져온느 역할 
# def btncmd():
#     print(txt.get("1.0",END))#처음부터 끝까지라는 의미다
#     #1은 첫번쪠 라인 의미 0 은 0번째 컬럼 위치
#     print(e.get())

#     txt.delete("1.0",END)
#     e.delete(0,END)
# btn=Button(root,text="클릭",command=btncmd)
# btn.pack()
# root.mainloop()

from tkinter import *
root = Tk()
root.title("memo")
txt= Text(root,width=30,height=40)
txt.pack()
txt.insert(END,"글자를 입력하세요")

ent=Entry(root,width=30)
ent.pack()
ent.insert(0,"한줄만 입력하세요")

def btncmd():
    print(txt.get("1.0",END))
    print(ent.get())

    txt.delete("1.0",END)
    ent.delete(0,END)
btn = Button(root,text="클릭",command=btncmd)
btn.pack()
root.mainloop()