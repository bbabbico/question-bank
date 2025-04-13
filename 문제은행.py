from faulthandler import disable
from tkinter import *
import os , sys

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

################################################################################################### 여기까지 tkinter 설정
문제 = open(f"{path}/문제.txt", 'r',encoding='utf-8')
정답 = open(f"{path}/정답.txt", 'r',encoding='utf-8')

ppp = 문제.readlines()
qqq =정답.readlines()
문제.close()
정답.close()

for i in range(len(ppp)): #개행 문자 삭제
    ppp[i]=ppp[i].replace("\n",'')
for i in range(len(qqq)): #개행 문자 삭제
    qqq[i]=qqq[i].replace("\n",'')

maxnum = len(ppp)-1 #최대 문제+정답 인덱스

################################################################################################### 여기까지 기본 변수 설정


num=0 #문제 순서
good =0 #정답 개수
bed =0 #오답 개수

def next():
    문제.delete(1.0,END) #내용삭제

    global num
    global maxnum
    global gold

    if (num+1 <= maxnum): #남은 문제 수 확인
        num+=1
        입력버튼.config(state='normal')
        다음버튼.config(state='normal')
    else:
        문제.insert(1.0,f'문제끝. 문제수 :{maxnum+1} 정답수 :{good} 오답수 :{bed} 포기한 문제 :{(maxnum+1)-(good+bed)}')
        입력버튼.config(state='disable')
        다음버튼.config(state='disable')
        return
    
    ppp[num] = ppp[num].replace('_n_','\n') #이스케이프 문자 변환
    ppp[num] = ppp[num].replace('_space_',' ')
   
    문제.insert(1.0,ppp[num])
    문제번호.config(text=f'{int(num/2+1)}번 문제')

def submit():
    문제.delete(1.0,END) #내용삭제
    global good
    global bed

    if (답안입력.get() == qqq[num]):
        문제.insert(1.0,'정답')
        good+=1
        입력버튼.config(state='disable')
        return
    else:
        문제.insert(1.0,'오답')
        bed +=1
        입력버튼.config(state='disable')
        return

def replay():
    global num
    global good
    global bed

    num=0
    good =0
    bed =0

    입력버튼.config(state='normal')
    다음버튼.config(state='normal')

    문제.delete(1.0,END) #내용삭제
    문제.insert(1.0,ppp[num])

################################################################################################### 여기까지 기능 함수 설정

제1구역 = Frame(win)
제1구역.pack(expand=1,ipady=130)

문제번호 = Label(제1구역,text='1번 문제')
문제번호.pack()

문제 = Text(제1구역,width=100,height=5,relief="solid",)
문제.insert(1.0,ppp[num])
문제.pack()

답안입력 = Entry(제1구역,width=20,relief="solid")
답안입력.pack(pady=30,ipady=10)

입력버튼 = Button(제1구역,command=submit,text = "입력",width=20, height=5,relief="solid",)
입력버튼.pack()

다음버튼 = Button(제1구역,command=next,text = "다음",width=20, height=5,relief="solid",)
다음버튼.pack()

재시작 = Button(제1구역,command=replay,text = "재시작",width=20, height=5,relief="solid",)
재시작.pack(side='bottom')

win.mainloop()  # tkinter 실행