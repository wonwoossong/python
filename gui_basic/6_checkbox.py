from tkinter import *

root = Tk()
root.title("NADO GUI")#title
root.geometry("640x480")# 가로 * 세로
#ex) 오늘하루 보지않기 , 일주일동안 보지않기
chkvar=IntVar()#chkvar 에 int 형으로 저장한다 
chkbox=Checkbutton(root,text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select()#처음부터 선택이 되어있다
# chkbox.deselect()#당연히 처음부터 선택이 안되어있당 
chkbox.pack()#이거를 안넣으면 구현이 안돼 

chkvar2=IntVar()
chkbox2=Checkbutton(root,text="일주일동안 보지않기",variabl=chkvar2)
chkbox2.pack()
def btncmd():
    print(chkvar.get())#0: 체크해제 1: 체크
    print(chkvar2.get())
btn=Button(root,text="클릭",command=btncmd)
btn.pack()
root.mainloop()

