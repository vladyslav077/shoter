import json

import PyQt5
from PyQt5.QtWidgets import *

from main import start_game

app = QApplication([])
window = QWidget()
window.resize(800,600)
setings = {}
def read_data():
    global setings
    with open("setings.json","r", encoding="utf-8") as file:
        setings = json.load(file)



def write_data():
    global setings
    with open("setings.json", "w", encoding="utf-8") as file:
       json.dump(file, setings)


read_data()
print(setings)




porox = QPushButton("CТАРТУЄМ")
change_btn = QPushButton("Change")
line_edit = QLineEdit(setings["skin"])
mainLine = QHBoxLayout()
mainLine.addWidget(porox)
mainLine.addWidget(change_btn)
mainLine.addWidget(line_edit)

window.setLayout(mainLine)

def change_data():
    setings["skin"] = line_edit.text()
    write_data()




porox.clicked.connect(start_game)
change_btn.clicked.connect(change_data)
window.show()
app.exec()
