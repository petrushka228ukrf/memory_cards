from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton,
    QPushButton, QLabel)
from random import randint, shuffle
app = QApplication([])
class Question():
    def  __init__(self, question, right_answer, wrongl, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrongl = wrongl
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = [] 
 
questions_list.append(Question('холм', 'pagorek', 'bugor', 'kopcow', 'helm')) 
questions_list.append(Question('деревня', 'wioska', 'woiska', 'woinstva', 'wilena')) 
questions_list.append(Question('город', 'miasto', 'miejsce', 'grad', 'gurat')) 
questions_list.append(Question('ель', 'swierk', 'sosna', 'cholka', 'picea'))


btn_OK = QPushButton ('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!') 

RadioGroupBox = QGroupBox("Baрианты ответов") 
rbtn_l = QRadioButton('Вариант 1') 
rbtn_2 = QRadioButton('Вариант 2') 
rbtn_3 = QRadioButton('Вариант 3') 
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ansl = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_l)  
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)

layout_ansl.addLayout(layout_ans2)
layout_ansl.addLayout(layout_ans3) 

RadioGroupBox.setLayout(layout_ansl) 

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('npaB ты или нет?')  
lb_Correct = QLabel('ответ будет тут!') 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop)) 
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
	
layout_linel = QHBoxLayout()
layout_line2 = QHBoxLayout()  
layout_line3 = QHBoxLayout()
layout_linel.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(RadioGroupBox) 
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide() 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)  
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_linel, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1) 
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1) 
layout_card.setSpacing(5) 
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide() 
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_l.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 

answers = [rbtn_l, rbtn_2, rbtn_3, rbtn_4] 

def ask(q: Question):
    shuffle(answers) 
    answers[0].setText(q.right_answer) 
    answers[1].setText(q.wrongl)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked:
        show_correct('Правильно!') 
    else:
        show_correct('Неверно!') 

def next_question():
    cur_question = randint(0, len(questions_list) - 1)	
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
	
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
btn_OK.clicked.connect(click_OK) 

next_question()
window.resize(400, 390)
window.show()
app.exec()
