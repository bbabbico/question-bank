from tkinter import *
import os , sys
import datetime
import shutil



win = Tk()  # tkinter 객체 생성
win.geometry("800x500")  # 화면 크기 설정
win.title("키로거")  # 화면 이름 설정
win.resizable(True,True) # 창크기 조절 가능여부 상하,좌우

#path = os.path.dirname(__file__) # py로 실행할때만 가능 exe에선 경로 오류남
if getattr(sys, 'frozen', False):
    #exe로 실행한 경우,exe를 보관한 디렉토리의 full path를 취득
    path = os.path.dirname(os.path.abspath(sys.executable))
else:
    #python py로 실행한 경우,py를 보관한 디렉토리의 full path를 취득
    path = os.path.dirname(os.path.abspath(__file__))

def backup():
    now =datetime.datetime.now() # 현재 날짜 시간 마이크로초까지 반환
    now =now.strftime('%Y-%m-%d %H-%M-%S') # 마이크로초 제외 표시

    if os.path.isfile(f"{path}/문제.txt"):
        shutil.copy(f'{path}/문제.txt',path+"/백업파일/문제 "+now+".txt")

        if os.path.isfile(path+"/백업파일/문제 "+now+".txt"):
         ext=Label(win, text="문제"+now+".txt\n로 백업됨", width=27, height=5,relief="solid") 
         ext.pack() 
    else :
        ext1=Label(win, text="복사실패 문제파일 없음", width=27, height=5,relief="solid") 
        ext1.pack() 

    if os.path.isfile(f"{path}/정답.txt"):
        shutil.copy(f'{path}/정답.txt',path+"/백업파일/정답 "+now+".txt")

        if os.path.isfile(path+"/백업파일/정답 "+now+".txt"):
         ext=Label(win, text="정답"+now+".txt\n로 백업됨", width=27, height=5,relief="solid") 
         ext.pack() 
    else :
        ext1=Label(win, text="복사실패 정답파일 없음", width=27, height=5,relief="solid") 
        ext1.pack() 

def 데이터정제():
   입력된문제 = 문제입력.get('1.0','end')
   입력된정답 = 정답입력.get('1.0','end')

   입력된문제 =입력된문제.replace("\n",'_n_')
   입력된정답 =입력된정답.replace("\n",'_n_')

   입력된문제 =입력된문제.replace(" ",'_space_')
   입력된정답 =입력된정답.replace(" ",'_space_')
   return [입력된문제+'\n' , 입력된정답+'\n']


def insert():
    result =데이터정제()
    print(result)
    문제 = open(f"{path}/문제.txt", 'a',encoding='utf-8')
    정답 = open(f"{path}/정답.txt", 'a',encoding='utf-8')

    문제.write(result[0])
    정답.write(result[1])

문제입력 = Text(win,width=100,height=3,relief="solid")
문제입력.pack(pady=5,ipady=1)

정답입력 = Text(win,width=100,height=3,relief="solid")
정답입력.pack(pady=5,ipady=1)

삽입 = Button(win,command=insert,text = "문제/정답 삽입",width=20, height=2,relief="solid",)
삽입.pack(pady=5)

백업 = Button(win,command=backup,text = "문제/정답 백업",width=20, height=5,relief="solid",)
백업.pack()

win.mainloop()  # tkinter 실행