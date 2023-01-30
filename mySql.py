import pymysql
from PySide6.QtWidgets import (QApplication, QMessageBox, QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
QTableWidget, QTableWidgetItem, QHeaderView)
import timeit

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.connect_button = QPushButton("Connect to Database")
        self.connect_button.clicked.connect(self.connect_to_database)
        self.layout.addWidget(self.connect_button)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)

    def connect_to_database(self):
        try:
            conn = pymysql.connect(host='178.159.160.204', port=29650, user='root', password='jakisserwerdlapk',
                                   db='airportdb')
            cur = conn.cursor()
            start_time = timeit.default_timer()
            cur.execute("SELECT identifier FROM airplane_type WHERE type_id='70' LIMIT 50000")
            records = cur.fetchall()
            end_time = timeit.default_timer()
            query_time = end_time - start_time
            QMessageBox.information(self, "Czas spędzony na wykonanie zapytania SELECT",
                                    "{:.2f} sekund".format(query_time), QMessageBox.Ok)

            self.table.setColumnCount(len(records[0]))
            self.table.setHorizontalHeaderLabels([i[0] for i in cur.description])
            self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.table.setRowCount(len(records))
            for i, record in enumerate(records):
                for j, value in enumerate(record):
                    item = QTableWidgetItem(str(value))
                    self.table.setItem(i, j, item)
            buttons_layout = QHBoxLayout()
            for i in range(10):
                button = QPushButton(f"Button {i+1}")
                buttons_layout.addWidget(button)
            self.layout.addLayout(buttons_layout)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e), QMessageBox.Ok)
            exit_button = QPushButton("Exit")
            exit_button.clicked.connect(app.exit)
            self.layout.addWidget(exit_button)

if __name__ == '__main__':
    app = QApplication([])
    window = GUI()
    window.show()
    app.exec()

