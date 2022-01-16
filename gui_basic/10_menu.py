from tkinter import *

root = Tk()
root.title("NADO GUI")#title
root.geometry("640x480")# 가로 * 세로

def create_new_file():
    print("새 파일을 만듭니다")
menu=Menu(root)
#File menu
menu_file=Menu(menu,tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="save all", state="disable")#비 활성화
menu_file.add_separator()
menu_file.add_command(label="Exit",command=root.quit)
menu.add_cascade(label="File",menu=menu_file)# 처음 메뉴에 메뉴 파일이 들어가고 
#이름이 File 이 된다
#Edit menu( 빈 값)
menu.add_cascade(label="Edit")
#language menu 추가 라디오 버튼 이용한다 
menu_lang=Menu(menu,tearoff=0)
menu_lang.add_radiobutton(label="phyton")
menu_lang.add_radiobutton(label="java")
menu_lang.add_radiobutton(label="c++")
menu.add_cascade(label="Language",menu=menu_lang)
root.config(menu=menu)
#check box 사용 
menu_view=Menu(menu,tearoff=0)
menu_view.add_checkbutton(label="show minimap")
menu.add_cascade(label="View",menu=menu_view)
root.mainloop()