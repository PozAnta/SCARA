import time

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QProgressBar

from API import SQL
from Tests import VariableGains


class MyThread(QThread):
    change_value = pyqtSignal(int)

    def run(self):
        cnt = 0
        while cnt < 100:
            cnt += 1
            time.sleep(0.3)


class App(QWidget):

    def __init__(self):
        super(App, self).__init__()
        self.sql = SQL.Data()
        self.thread = MyThread()
        self.combobox = QComboBox(self)

        self.selected_tests = []
        self.tests = []
        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(10, 100, 75, 10)
        self.progressbar.setValue(0)

        # -- Buttons declaration
        self.start_button = QPushButton(self)
        self.show_button = QPushButton(self)
        self.start_button.setGeometry(10, 250, 75, 30)
        self.start_button.setText("START")
        self.show_button.setGeometry(10, 50, 75, 30)
        self.show_button.setText("Show Tests")

        self.combobox.move(10, 10)
        tests = [' ']
        self.listwidget = QListWidget(self)
        self.listwidget.setGeometry(150, 10, 120, 200)
        self.grid_layout = QGridLayout()
        dic = {-1: "", 0: tests}

        self.sql.table = 'Features'
        self.sql.read_column_data()

        self.combobox.addItems(self.sql.read_column_data())
        self.checkbox = []
        self.number_of_tests = len(tests)
        box_id = self.combobox.currentIndex()
        self.listwidget.addItems(dic.get(box_id))
        self.grid_layout.addWidget(self.listwidget)

        y = 15
        for i in range(10):
            self.checkbox.append(QCheckBox(self))
            self.checkbox[i].move(135, y)

            y += 17

        for j in range(10):
            self.index = j
            self.checkbox[j].stateChanged.connect(self.asd)

        self.setFixedSize(300, 300)

        self.start_button.clicked.connect(self.start)
        self.show_button.clicked.connect(self.show_tests)

    def start_progressbar(self):
        self.thread.change_value.connect(self.set_progressbar)

    def set_progressbar(self, val):
        pass

    def start(self):
        count = 0
        # print(self.selected_tests)
        dic = {0: VariableGains.GainSckeduling.Test("Post Factor").posfactor_test(),
               1: VariableGains.GainSckeduling.Test("Coupling").cplg_test()}
        for test in self.selected_tests:
            if bool(test):
                print("Selected test: ", self.tests[count])
                print(dic.get(count))
            count += 1

    def show_tests(self):
        box_text = self.combobox.currentText()
        box_id = self.combobox.currentIndex()
        self.sql.table = 'Tests'
        self.tests = self.sql.read_by_id(str(box_id))
        # print("Test found: ", self.tests)
        self.number_of_tests = len(self.tests)
        QListWidget.clear(self.listwidget)
        try:
            self.listwidget.addItems(self.tests)

        except TypeError:
            print("NO tests")

        # print(box_text)
        # print(box_id)

    def asd(self):
        box_text = self.combobox.currentText()
        box_id = self.combobox.currentIndex()
        # print(box_text)
        # print(box_id)
        self.selected_tests = []

        for st in range(len(self.checkbox)):
            self.selected_tests.append(self.checkbox[st].isChecked())
            # print(self.checkbox[st].isChecked())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    EX = App()
    EX.show()
    sys.exit(app.exec_())
