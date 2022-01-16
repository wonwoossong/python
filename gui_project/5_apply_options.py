#사용자가 주는 옵션값에 맞춰서 이미지 만드는것 
import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog#파일 가져올때 서브 모듈이기 때문에
from PIL import Image

root = Tk()
root.title("NADO GUI")#title
#파일 추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",\
        filetypes=(("PNG 파일","*.png"),("모든파일","*.*")),\
        initialdir=r"C:\Users\wonwoo song\Desktop\pythonworkspace")#최초에 C:/ 경로를 보여줌
    #사용자가 선택한 파일목록 
    for file in files:
        list_file.insert(END,file)
#선택 삭제 
def del_file():
    # print(list_file.curselection())
    for index in reversed(list_file.curselection()):#순서가 뒤집힌다 그러나 실제 값에는 영향 순서가 바뀐 값만 던져준다
        list_file.delete(index)

#저장 경로 (폴더)
def browse_dest_path():
    folder_selected=filedialog.askdirectory()
    if folder_selected=="": #t사용자가 취소를 누를때
        return
    # print(folder_selected)
    txt_dest_path.delete(0,END)
    txt_dest_path.insert(0,folder_selected)
#이미지 통합
def merge_image():
    
    # print("가로넓이:",cmd_width.get())
    # print("간격:",cmd_space.get())
    # print("파일포멧:",cmd_format.get())
    try:
        #가로넓이 
        img_width = cmd_width.get()
        if img_width == "원본유지":
            img_width = -1 #-1 일 때는 원본 기준으로 
        else:
            img_width = int(img_width)
        
        # 간격
        img_space = cmd_space.get()
        if img_space == "좁게":
            img_space = 30 
        elif img_space == "보통":
            img_space = 60
        elif img_space == "넓게":
            img_space = 90
        else:#없음
            img_space=0

        #포맷
        img_format = cmd_format.get().lower()#PNG,JPG,BMP 값을 받아와서 소문자로 변경

        ######################################################### 



        images = [Image.open(x) for x in list_file.get(0,END)]
        # 이미지 사이즈를 리스트에 넣어서 하나씩 처리
        image_sizes = [] #(width1,height1) (width2,height2) (width3,height3)...
        if img_width >-1:
            #width 값 변경 해야된다
            image_sizes = [(int(img_width),int(img_width * x.size[1] / x.size[0]))for x in images]  
        else:
            image_sizes = [(x.size[0], x.size[1]) for x in images] #원본 사이즈 사용

        #이미지를 변경 할려면 넓이라 높이 둘다 변경시켜야 된다
        #계산식
        #100 * 60 이미지가 있음 --> width 를 80 으로 줄이면 height? 
        #(원본 width) : (원본 height) = (변경 widht) : (변경 height)
        # 100               60        =    80               ?
        # x          :      y          =     x'     :       y'
        # xy' = x'y 
        # y' = x'y/x 이 식을 적용 하면 되는거 
        # 100:60 = 80:48
        # 우리 코드에 대입하려면 
        # x=widht=size[0]
        # y=height=size[1]
        # x'= img_width # 이값으로 변경 해야되는거고 
        # y'= x'y/x = img_width * size[1] / size[0] 


        widths,heights = zip(*(image_sizes))
        
        #최대 넓이, 전체 높이 구해옴
        max_width, total_height=max(widths),sum(heights)

        #스케치북 준비

        if img_space > 0 : #이미지 간격 옵션 적용
            total_height += (img_space*(len(images)-1)) # 전체 높이 설정

        result_img=Image.new("RGB",(max_width,total_height),(255,255,255))#배경 흰색
        y_offset=0 # y 위치 정보

        for idx, img in enumerate(images):
            # width 가 원본 유지가  아닐때 이미지 크기 조정
            if img_width > -1:
                img = img.resize(image_sizes[idx])
    
            result_img.paste(img, (0,y_offset))
            y_offset += (img.size[1] + img_space) # height 값 + 사용자가 지정한 간격

            progress = (idx + 1) /len(images) *100 #실제 퍼센트 정보를 계산해 오기
            p_var.set(progress)
            progress_bar.update()
        # 포맷 옵션 처리 
        file_name = "nado_photo." + img_format

        dest_path = os.path.join(txt_dest_path.get(),file_name)
        result_img.save(dest_path)
        msgbox.showinfo("알림", "작업이 완료되었습니다")
    except Exception as err: #예외처리
        msgbox.showerror("에러",err)
#시작
def start():
    # #각 옵션들 값 을 확인
    # print("가로넓이:",cmd_width.get())
    # print("간격:",cmd_space.get())
    # print("파일포멧:",cmd_format.get())

    #파일 목록 확인 
    if list_file.size()==0:#하나의 파일도 선택 안됐을때
        msgbox.showwarning("경고","이미지 파일을 추가하세요")
        return
    #저장 경로 확인
    if len(txt_dest_path.get())==0:
        msgbox.showwarning("경고","저장 경로를 선택하세요")
        return
    #이미지 통합 작업
    merge_image()
#파일 프레임 ( 파일 추가, 선택 삭제 )
file_frame=Frame(root)
file_frame.pack(fill="x",padx=5,pady=5)

btn_add_file=Button(file_frame, padx= 5 , pady=5 ,width = 12,text="파일추가",command=add_file)
btn_add_file.pack(side="left")

btn_delete_file = Button(file_frame,  padx= 5 , pady=5 ,width = 12,text="선택삭제",command=del_file)
btn_delete_file.pack(side="right")

#리스트 프레임(리스트박스, 스크롤바 )
list_frame=Frame(root)
list_frame.pack(fill="both",padx=5,pady=5)#리스트가 좌우로 붙을수 있게

scrollbar=Scrollbar(list_frame)
scrollbar.pack(side="right",fill="y")

list_file=Listbox(list_frame,selectmode="extended",height=15,yscrollcommand=scrollbar.set)
list_file.pack(side="left",fill="both",expand=True)
scrollbar.config(command=list_file.yview)

#저장경로 프레임
path_frame=LabelFrame(root,text="저장경로")
path_frame.pack(fill="x",padx=5,pady=5,ipady=5)

txt_dest_path=Entry(path_frame)#한줄이니까 
txt_dest_path.pack(side="left",fill="x",expand=True,padx=5,pady=5,ipady=4)#높이변경

btn_dest_path=Button(path_frame,text="찾아보기",width=10,command=browse_dest_path)
btn_dest_path.pack(side="right",padx=5,pady=5)

#옵션 프레임
frame_option=LabelFrame(root,text="옵션")
frame_option.pack(padx=5,pady=5,ipady=5)
#1.가로 넓이 옵션
#가로 넓이 레이블
lbl_width=Label(frame_option,text="가로넓이",width=8)
lbl_width.pack(side="left",padx=5,pady=5)
#가로 넓이 콤보
opt_width=["원본유지","1024","800","640"]
cmd_width=ttk.Combobox(frame_option,state="readonly",values=opt_width,width=10)
cmd_width.current(0)#첫번쩨 값을 자동으로 설정 
cmd_width.pack(side="left",padx=5,pady=5)
#2.간격옵션
# 간격 옵션 레이블 
lbl_space=Label(frame_option,text="간격",width=8)
lbl_space.pack(side="left",padx=5,pady=5)
# 간격 옵션 콤보
opt_space=["없음","좁게","보통","넓게"]
cmd_space=ttk.Combobox(frame_option,state="readonly",values=opt_space,width=10)
cmd_space.current(0)#첫번쩨 값을 자동으로 설정 
cmd_space.pack(side="left",padx=5,pady=5)

#3.파일 포멧 옵션
# 파일 포멧 옵션 레이블 
lbl_format=Label(frame_option,text="포멧",width=8)
lbl_space.pack(side="left",padx=5,pady=5)
# 파일 포멧 옵션 콤보
opt_format=["PNG","JPG","BMP"]
cmd_format=ttk.Combobox(frame_option,state="readonly",values=opt_format,width=10)
cmd_format.current(0)#첫번쩨 값을 자동으로 설정 
cmd_format.pack(side="left",padx=5,pady=5)

#진행 상황 progress bar 
frame_progress = LabelFrame(root,text="진행상황")
frame_progress.pack(fill="x",padx=5,pady=5,ipady=5)

p_var=DoubleVar()
progress_bar=ttk.Progressbar(frame_progress,maximum=100,variable=p_var)
progress_bar.pack(fill="x",padx=5,pady=5)

#실행 프레임
frame_run=Frame(root)
frame_run.pack(fill="x",padx=5,pady=5)

btn_close=Button(frame_run,padx=5,pady=5,text="닫기",width=12,command=root.quit)
btn_close.pack(side="right",padx=5,pady=5)

btn_start=Button(frame_run,padx=5,pady=5,text="시작",width=12,command=start)
btn_start.pack(side="right",padx=5,pady=5)


root.resizable(False,False)#너비 높이 변경 불가 
root.mainloop()
