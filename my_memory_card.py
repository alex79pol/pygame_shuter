
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox
 

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс от Crazy People')
main_win.resize(400, 200)

RadioGroubox = QGroupBox ('Варианты ответов')
question = QLabel('Какой нацыональности не существует?')
btn_answer1 = QRadioButton('Энцы')
btn_answer2 = QRadioButton('Смурфы')
btn_answer3 = QRadioButton('Чулымцы')
btn_answer4 = QRadioButton('Алеуты')
bruh = QPushButton('Ответить')
layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QVBoxLayout()
layoutH3 = QVBoxLayout()
layoutH2.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment = Qt.AlignCenter)

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
layout_main.addWidget(bruh)
main_win.setLayout(layout_main)
 
main_win.show()
app.exec_()
