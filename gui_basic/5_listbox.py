from tkinter import *

root = Tk()
root.title("NADO GUI")#title
root.geometry("640x480")# 가로 * 세로

listbox=Listbox(root,selectmode="extended",height=0)#height 값이 0 이면 다보여줘
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END,"수박")
listbox.insert(END,"포도")
listbox.pack()
# button 을 클릭했을때 text와 entry 값을 가져온느 역할 
def btncmd():
    # 삭제
    #listbox.delete(END)#맨 뒤에 항목을 삭제하는거 / 0 이면 맨앞부터 
    #갯수 확인 
    #print("리스트에는",listbox.size(),"개가 있어요")
    #항목 확인 (시작 idx , 끝 idx)
    print("1번째 부터 3번재 까지의 항목",listbox.get(0,2))
    print("2번째 부터 5번째 까지의 항목",listbox.get(2,4))
    #선택된 항목 확인(idx값으로 반환)
    print("선택된 항목",listbox.curselection())
btn=Button(root,text="클릭",command=btncmd)
btn.pack()
root.mainloop()