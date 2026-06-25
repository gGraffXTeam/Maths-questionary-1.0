from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QButtonGroup, QRadioButton,
        QPushButton, QLabel)
from random import shuffle, randint


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


question_list = []
question_list.append(Question('what π * 2 is equal to?', "6.283185" , "6.384518" , "6.157812" , "6.959815" ))
question_list.append(Question('what 5( 40 / 8 ) is equal to?', "25", "52" , "63", "11"))
question_list.append(Question('what 10 / 6 is equal to?', "1.6666666666" , "1.65555555555555", "1.36666666666666", "1.65656565656"))
question_list.append(Question('what is 5 * 6  *5 / 30 equal to?', "5", "6", "5.6", "6.6"))
question_list.append(Question('what 5! / 45 is equal to?' , "2.6666666666666", "3" , "2.5555555555555" , "2.33333336333"))
question_list.append(Question('what 5!! is equal to?' , "6.689502913449127058e198" , "HELL HAH!!!!!!" , "6.689502... I DON4T KNOW!!" , "6.5645562974855629672314674e62645"))
question_list.append(Question('what 10! is equal to?', "3628800" , "35280880" , "758015" , "33680880" ))
question_list.append(Question('what 5^5 is equal to?', "3125" , "3185" , "2965" , "6954" ))
question_list.append(Question('what √45 is equal to?', "6.7082" , "6.6082" , "6.581" , "6.198" ))
question_list.append(Question('what 64² is equal to?', "4096" , "4095" , "4086" , "5686" ))

question_list.append(Question('what  is equal to?', "" , "" , "" , "" ))


# signs for questions:
#( √                       )




app = QApplication([])

button = QPushButton("Відповісти")
label_question = QLabel("Питання")

RadioButtonGroup = QGroupBox("Варіанти відповідей")
radiobutton1 = QRadioButton("Варіант 1")
radiobutton2 = QRadioButton("Варіант 2")
radiobutton3 = QRadioButton("Варіант 3")
radiobutton4 = QRadioButton("Варіант 4")

RadioGroup = QButtonGroup()
RadioGroup.addButton(radiobutton1)
RadioGroup.addButton(radiobutton2)
RadioGroup.addButton(radiobutton3)
RadioGroup.addButton(radiobutton4)

layoutH = QHBoxLayout()
layout1V = QVBoxLayout()
layout2V = QVBoxLayout()

layout1V.addWidget(radiobutton1)
layout1V.addWidget(radiobutton2)
layout2V.addWidget(radiobutton3)
layout2V.addWidget(radiobutton4)

layoutH.addLayout(layout1V)
layoutH.addLayout(layout2V)
RadioButtonGroup.setLayout(layoutH)

AnsGroupBox = QGroupBox("Результат!")
label_result = QLabel("Правильно чи ні ?")
label_correct = QLabel("Правильна відповідь!")
label_stats = QLabel("")  # НОВЕ: мітка для статистики

line_res = QVBoxLayout()
line_res.addWidget(label_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
line_res.addWidget(label_correct, alignment=Qt.AlignHCenter, stretch=2)
line_res.addWidget(label_stats, alignment=Qt.AlignHCenter)  # НОВЕ: додали мітку в панель
AnsGroupBox.setLayout(line_res)

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

line1.addWidget(label_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
line2.addWidget(RadioButtonGroup)
line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

line3.addStretch(1)
line3.addWidget(button, stretch=2)
line3.addStretch(1)

main_line = QVBoxLayout()
main_line.addLayout(line1, stretch=2)
main_line.addLayout(line2, stretch=8)
main_line.addStretch(1)
main_line.addLayout(line3, stretch=1)
main_line.addStretch(1)
main_line.setSpacing(5)


def show_result():
    RadioButtonGroup.hide()
    AnsGroupBox.show()
    button.setText("Наступне питання")


def show_question():
    RadioButtonGroup.show()
    AnsGroupBox.hide()
    button.setText("Відповісти")

    RadioGroup.setExclusive(False)
    radiobutton1.setChecked(False)
    radiobutton2.setChecked(False)
    radiobutton3.setChecked(False)
    radiobutton4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [radiobutton1, radiobutton2, radiobutton3, radiobutton4]


def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

    label_question.setText(q.question)
    label_correct.setText(q.right_answer)
    show_question()


# ====== ЗМІНЕНО: додали оновлення статистики ======
def show_correct(res):
    label_result.setText(res)
    rating = round(window.score / window.total * 100)
    label_stats.setText(f"Питань: {window.total}  |  Правильно: {window.score}  |  Рейтинг: {rating}%")
    show_result()
# ====== КІНЕЦЬ ЗМІНЕНОГО ======


# ====== ЗМІНЕНО: window.score += 1 перенесено до check_answer ======
def check_answer():
    if answers[0].isChecked():
        window.score += 1
        show_correct("Круто! Молодець!")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Неправильно! Спробуй ще раз")
# ====== КІНЕЦЬ ЗМІНЕНОГО ======


def next_question():
    window.total += 1
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)


def click_OK():
    if button.text() == "Відповісти":
        check_answer()
    else:
        next_question()


window = QWidget()
window.score = 0
window.total = 0

window.setLayout(main_line)
window.setWindowTitle("Memory Card")

button.clicked.connect(click_OK)

next_question()
window.resize(400, 300)
window.show()
app.exec_()
