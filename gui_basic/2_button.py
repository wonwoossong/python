from tkinter import *

root = Tk()
root.title("NADO GUI")#title

btn1=Button(root, text="버튼1")#버튼을만들고
btn1.pack()#pack 을 통해서 우리 프로그램에 포함 시켰다

btn2=Button(root, padx=5,pady=10, text="버튼22222222")#유동가능 크기
btn2.pack()

btn3=Button(root, padx=10,pady=5, text="버튼3")
btn3.pack()

btn4=Button(root,width=10, height=3, text="버튼4444444444444444")#고정크기 글자가 잘려
btn4.pack()

btn5=Button(root,fg="red", bg="yellow" ,text="버튼5")
btn5.pack()

photo = PhotoImage(file="gui_basic/image.png")
btn6 = Button(root,image=photo)
btn6.pack()

def btncmd1():
    print("잠시만 기다려 주십시오")
btn7 = Button(root,width=30,height=15,command=btncmd1,text="그만 눌러")
btn7.pack()

def btncmd():
    print("버튼이 클릭되었습니다")
btn7=Button(root,text="클릭하는 버튼",command=btncmd)
btn7.pack()


root.mainloop()

