import json

from PyQt5.QtWidgets import *
import pygame
import time
import ufoner
import shoot

app = QApplication([])

window = QWidget()
settings = {}
window.resize(400, 300)



def read_data():
    global settings
    with open("settings.json", "r", encoding="utf-8") as file:
        settings = json.load(file)

def write_data():
    global settings
    with open("settings.json", "m", encoding="utf-8") as file:
        settings = json.load(file)
read_data()
print(settings)
menubut = QPushButton('старт')
change_btn = QPushButton("Change")
line_edit = QLineEdit(settings["skin"])

main_line = QVBoxLayout()
main_line.addWidget(line_edit)
main_line.addWidget(change_btn)
main_line.addWidget(menubut)

window.setLayout(main_line)

def change_data():
    settings["skin"] = line_edit.text()
    write_data()

change_btn.clicked.connect(change_data)

menubut.clicked.connect(change_data)

main_line = QVBoxLayout()


main_line.addWidget(menubut)

window.setLayout(main_line)

menubut.clicked.connect(menubut)





window.show()
app.exec()