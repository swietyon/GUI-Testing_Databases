from PySide6.QtWidgets import (QApplication, QMessageBox, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView)
from pymongo import MongoClient
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
            start_time = timeit.default_timer()
            client = MongoClient("mongodb://178.159.160.204:29651/")
            db = client["airportdb"]
            weatherdata = db.weatherdata
            records = db.passengerdetails.find({"passenger_id": {"$lt": 30000}}, {"city": 1, "birthdate": 1}).limit(50000)
            end_time = timeit.default_timer()
            query_time = end_time - start_time
            QMessageBox.information(self, "Czas spędzony na wykonanie zapytania SELECT",
                                    "{:.2f} sekund".format(query_time), QMessageBox.Ok)

            for record in records:
                print(record)

            self.table.setColumnCount(len(records[0]))
            self.table.setHorizontalHeaderLabels(records[0].keys())
            self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.table.setRowCount(len(list(records)))

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
