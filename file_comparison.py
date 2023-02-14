import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog

class FileComparisonWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Comparison Tool")
        self.setWindowIcon(QtGui.QIcon("files.png"))

        self.file1_label = QtWidgets.QLabel("")
        self.file2_label = QtWidgets.QLabel("")

        self.file1_button = QtWidgets.QPushButton("Select File 1")
        self.file1_button.clicked.connect(self.select_file1)
        self.file2_button = QtWidgets.QPushButton("Select File 2")
        self.file2_button.clicked.connect(self.select_file2)
        self.compare_button = QtWidgets.QPushButton("Compare Files")
        self.compare_button.clicked.connect(self.compare_files)

        self.result_label = QtWidgets.QLabel("")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.file1_label)
        layout.addWidget(self.file1_button)
        layout.addWidget(self.file2_label)
        layout.addWidget(self.file2_button)
        layout.addWidget(self.compare_button)
        layout.addWidget(self.result_label)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def select_file1(self):
        file_path, _ = QFileDialog.getOpenFileName()
        self.file1_label.setText(file_path)

    def select_file2(self):
        file_path, _ = QFileDialog.getOpenFileName()
        self.file2_label.setText(file_path)

    def compare_files(self):
        file1 = self.file1_label.text()
        file2 = self.file2_label.text()

        with open(file1, "r", encoding="ISO-8859-1") as f1, open(file2, "r", encoding="ISO-8859-1") as f2:
            contents1 = f1.read()
            contents2 = f2.read()

            match_percentage = self.compare_contents(contents1, contents2)
            if match_percentage >= 80:
                self.result_label.setText("Files match ({}%)".format(match_percentage))
            else:
                self.result_label.setText("Files do not match ({}%)".format(match_percentage))

    def compare_contents(self, contents1, contents2):
        common_words = 0
        words1 = contents1.split()
        words2 = contents2.split()
        for word in words1:
            if word in words2:
                common_words += 1

        match_percentage = (common_words / len(words1)) * 100
        return match_percentage

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FileComparisonWindow()
    window.show()
    sys.exit(app.exec_())

