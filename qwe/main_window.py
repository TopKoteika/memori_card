from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout , QSpinBox , QHBoxLayout , QRadioButton, QGroupBox, QButtonGroup
menu_btn = QPushButton("Меню")
rest_btn  = QPushButton("Відрочинок")

time_spin = QSpinBox()
time_spin.setValue(3)
time_lb = QLabel("Хвилинка")

row1 = QHBoxLayout()
row1.addWidget(menu_btn)
row1.addStretch(1)
row1.addWidget(rest_btn)
row1.addWidget(time_spin)
row1.addWidget(time_lb)

question_lb = QLabel("Питаня")


btn2 = QRadioButton("Варіант1")
btn2 = QRadioButton("Варіант2")
btn2 = QRadioButton("Варіант3")
btn2 = QRadioButton("Варіант3")
btn2 = QRadioButton("Варіант4")
row2 = QHBoxLayout()
radio_group = QButtonGroup()
radio_group.appButton(btn1)
radio_group.appButton(btn2)
radio_group.appButton(btn3)
radio_group.appButton(btn4)


main_line =  QVBoxLayout()
main_line.addLayout(row1)