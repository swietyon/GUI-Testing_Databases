from PySide6.QtWidgets import (
    QApplication
    ,QMessageBox
    ,QWidget
    ,QLabel
    ,QPushButton
    ,QVBoxLayout
)

app         = QApplication([])
app.setStyle('macos')
window      = QWidget()
v_layout    = QVBoxLayout()

btn1 = QPushButton('button 1')
btn2 = QPushButton('button 2')
btn3 = QPushButton('button 3')
btn4 = QPushButton('button 4')
btn5 = QPushButton('button 5')
btn6 = QPushButton('button 6')
btn7 = QPushButton('button 7')
btn8 = QPushButton('button 8')
btn9 = QPushButton('button 9')
btn10 = QPushButton('button 10')

v_layout.addWidget(QLabel('GUI APP'))
v_layout.addWidget(btn1)
v_layout.addWidget(btn2)
v_layout.addWidget(btn3)
v_layout.addWidget(btn4)
v_layout.addWidget(btn5)
v_layout.addWidget(btn6)
v_layout.addWidget(btn7)
v_layout.addWidget(btn8)
v_layout.addWidget(btn9)
v_layout.addWidget(btn10)



def mongo1_clicked():
    alert = QMessageBox()
    alert.setText('btn1')
    alert.exec()

def mongo2_clicked():
    alert = QMessageBox()
    alert.setText('btn2')
    alert.exec()

def mongo3_clicked():
    alert = QMessageBox()
    alert.setText('btn3')
    alert.exec()

def mongo4_clicked():
    alert = QMessageBox()
    alert.setText('btn4')
    alert.exec()

def mongo5_clicked():
    alert = QMessageBox()
    alert.setText('btn5')
    alert.exec()

def mongo6_clicked():
    alert = QMessageBox()
    alert.setText('btn6')
    alert.exec()

def mongo7_clicked():
    alert = QMessageBox()
    alert.setText('btn7')
    alert.exec()

def mongo8_clicked():
    alert = QMessageBox()
    alert.setText('btn8')
    alert.exec()

def mongo9_clicked():
    alert = QMessageBox()
    alert.setText('btn9')
    alert.exec()

def mongo10_clicked():
    alert = QMessageBox()
    alert.setText('btn10')
    alert.exec()

btn1.clicked.connect(mongo1_clicked)
btn2.clicked.connect(mongo2_clicked)
btn3.clicked.connect(mongo3_clicked)
btn4.clicked.connect(mongo4_clicked)
btn5.clicked.connect(mongo5_clicked)
btn6.clicked.connect(mongo6_clicked)
btn7.clicked.connect(mongo7_clicked)
btn8.clicked.connect(mongo8_clicked)
btn9.clicked.connect(mongo9_clicked)
btn10.clicked.connect(mongo10_clicked)


window.setLayout(v_layout)
window.show()
app.exec()