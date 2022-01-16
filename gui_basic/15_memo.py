import os
from tkinter import *
root=Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("1020x580")

filename="mynote.txt"

def open_file():
    if os.path.isfile(filename):#파일 있으면 튜르 없으면 펄스
        with open(filename,"r",encoding="utf-8") as file:
            txt.delete("1.0",END)#텍스트 위젯 본문 삭제 
            txt.insert(END,file.read())#파일내용 본문에 입력
def save_file():
    with open(filename,"w",encoding="utf-8") as file:
        file.write(txt.get("1.0",END))#모든 내용을 가져와서 저장

menu=Menu(root)
menu_file=Menu(menu,tearoff=0)

menu_file.add_command(label="열기",command=open_file)
menu_file.add_command(label="저장",command=save_file)
menu_file.add_separator()
menu_file.add_command(label="종료",command=root.quit)
menu.add_cascade(label="파일",menu=menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")
root.config(menu=menu)#메뉴에다가 우리 메뉴를 집어넣는 과정 
#스크롤바
scrollbar=Scrollbar(root)
scrollbar.pack(side="right",fill="y")

#본문영역
txt=Text(root,yscrollcommand=scrollbar.set)
txt.pack(side="left",fill="both",expand=True)
scrollbar.config(command=txt.yview)#맵핑해주는과정

root.mainloop()