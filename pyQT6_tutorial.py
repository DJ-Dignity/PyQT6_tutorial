import sys
from random import choice

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QMenu


window_titles = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "What on earth?",
    "What on earth?",
    "This is surpring!",
    "This is surpring!",
    "Something went wrong"
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        #button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        #button.clicked.connect(self.the_button_was_toggled)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.label1 = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label1.setText)

        self.label2 = QLabel("Click in this window.")
        self.label3 = QLabel("Additional click details.")

        self.setFixedSize(QSize(400, 300))
        #self.setCentralWidget(self.button)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        #self.button.setText("You already clicked me.")
        #self.button.setEnabled(False)
        # self.setWindowTitle("My Oneshot App")
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print("Checked?", self.button_is_checked)

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)

        if window_title == "Something went wrong":
            self.button.setDisabled(True)

    def mouseMoveEvent(self, e):
        self.label2.setText("mouseMoveEvent")
        self.print_button_info(e)

    def mousePressEvent(self, e):
        self.label2.setText("mousePressEvent")
        self.print_button_info(e)

    def mouseReleaseEvent(self, e):
        self.label2.setText("mouseReleaseEvent")
        self.print_button_info(e)

    def mouseDoubleClickEvent(self, e):
        self.label2.setText("mouseDoubleClickEvent")
        self.print_button_info(e)

    def print_button_info(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label3.setText("Left button")
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label3.setText("Middle button")
        elif e.button() == Qt.MouseButton.RightButton:
            self.label3.setText("Right button")

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())
        #context.exec(self.mapToGlobal(e))

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
