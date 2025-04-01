import sys #시스템 관련 기능을 사용하기 위한 모듈
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                                QMessageBox, QPlainTextEdit, QHBoxLayout) #필요한 위젯을 임포트


from PyQt5.QtGui import QIcon #아이콘 관련 클래스를 임포트


class Calculator(QWidget): #Calculator 클래스를 QWidget를 상속받아 정의


    def __init__(self): #생성자 (객체 초기화)
        super().__init__() #부모 클래스(QWidget)의 생성자를 호출하여 초기화
        self.initUI() #UI 초기화 함수 호출
        
    def initUI(self): #UI를 초기화하는 함수
        self.te1 = QPlainTextEdit() #읽기 전용 텍스트 입력 창 생성
        self.te1.setReadOnly(True) #텍스트 입력 창을 읽기전용으로 설정

        #"Message" 버튼 생성, 버튼 클릭 시 activatemessage 함수가 실행되도록 연결
        self.btn1 = QPushButton('Message', self)
        self.btn1.clicked.connect(self.activateMessage)

        #"Clear" 버튼 생성, 버튼 클릭 시 clearMessage 함수가 실행되도록 연결
        self.btn2 = QPushButton('Clear', self)
        self.btn2.clicked.connect(self.clearMessage)

        #버튼들을 수평으로 배치할 수 있는 레이아웃 생성
        hbox = QHBoxLayout()
        hbox.addStretch(1) #레이아웃에 여백 추가
        hbox.addWidget(self.btn1) #"Message" 버튼을 수평 레이아웃에 추가
        hbox.addWidget(self.btn2) #"clear" 버튼을 수평 레이아웃에 추가

        
        # 수직 레이아웃을 생성하고, 텍스트 입력창과 버튼 레이아웃을 추가
        vbox = QVBoxLayout()
        vbox.addWidget(self.te1) #텍스트 입력창을 수직 레이아웃에 추가
        vbox.addLayout(hbox) #수평 버튼 레이아웃을 수직 레이아웃에 추가
        vbox.addStretch(1) #레이아웃에 여백 추가

        self.setLayout(vbox) #수직 레이아웃을 윈도우의 레이아웃으로 설정

        self.setWindowTitle('Calculator') #윈도우의 제목 설정
        self.setWindowIcon(QIcon('icon.png')) #윈도우 아이콘 설정
        self.resize(256, 256) #윈도우 크기 설정
        self.show() # 윈도우를 화면에 표시

#"Message" 버튼 클릭 시 호출되는 함수

    def activateMessage(self):
        #텍스트 입력 창에 "Button clicked!"라는 메시지를 추가
        self.te1.appendPlainText("Button clicked!")

#"clear" 버튼 클릭 시 호출되는 함수
    def clearMessage(self):
        #텍스트 입력 창의 내용을 모두 삭제
        self.te1.clear()

#메인 함수
if __name__ == '__main__':
    app = QApplication(sys.argv) #QApplication 객체 생성 (애플리케이션을 실행하기 위해 필수)
    view = Calculator() #Calulator 클래스 객체 생성
    sys.exit(app.exec_()) #애플리케이션 실행, 종료 시 시스템 종료
     
