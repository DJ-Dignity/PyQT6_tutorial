import sys
from random import choice

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QColor, QPalette
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QStackedLayout,
    QTabWidget,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QMenu,
)


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


class MainWindow0(QMainWindow):
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


class MainWindow1(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QListWidget,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:
            #print("w:")
            #print(w)
            widget = w()
            if w == QCheckBox:
                widget.setCheckState(Qt.CheckState.Checked)
                widget.setText("This is a checkbox")
                widget.stateChanged.connect(self.show_state)
            elif w == QComboBox:
                widget.addItems(["One", "Two", "Three"])
                widget.setEditable(True)
                widget.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
                widget.setMaxCount(10)
                widget.currentIndexChanged.connect(self.index_changed)
                widget.currentTextChanged.connect(self.text_changed)
            elif w == QDial:
                widget.setRange(-10, 100)
                widget.setSingleStep(5)
                widget.valueChanged.connect(self.value_changed)
                widget.sliderMoved.connect(self.slider_position)
                widget.sliderPressed.connect(self.slider_pressed)
                widget.sliderReleased.connect(self.slider_released)
            elif w == QLabel:
                widget.setText("Hello World")
                font = widget.font()
                font.setPointSize(30)
                widget.setFont(font)
                widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
            elif w == QListWidget:
                widget.addItems(["One", "Two", "Three"])
                widget.currentItemChanged.connect(self.index_changed)
                widget.currentTextChanged.connect(self.text_changed)
            elif w == QLineEdit:
                widget.setMaxLength(10)
                widget.setPlaceholderText("Enter your text")
                # widget.setReadOnly(True) # uncomment this to make readonly
                widget.returnPressed.connect(self.return_pressed)
                widget.selectionChanged.connect(self.selection_changed)
                widget.textChanged.connect(self.text_changed)
                widget.textEdited.connect(self.text_edited)
            elif w == QSlider:
                # widget.setMinimum(-10)
                # widget.setMaximum(3)
                widget.setRange(-10, 3)
                widget.setSingleStep(3)
                widget.valueChanged.connect(self.value_changed)
                widget.sliderMoved.connect(self.slider_position)
                widget.sliderPressed.connect(self.slider_pressed)
                widget.sliderReleased.connect(self.slider_released)
            elif w == QSpinBox:
                #widget.setMinimum(-10)
                #widget.setMaximum(3)
                widget.setRange(-10, 3)
                widget.setPrefix("$")
                widget.setSuffix("c")
                widget.setSingleStep(3)
                widget.valueChanged.connect(self.value_changed)
                widget.textChanged.connect(self.value_changed_str)
                # widget.lineEdit().setReadOnly(True) # Only arrow keys can change value

            layout.addWidget(widget)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(Qt.CheckState(s) == Qt.CheckState.Checked)
        print(s)

    def index_changed(self, i):
        print(i)

    def text_changed(self, s):
        print(s)

    def return_pressed(self):
        print("Return pressed!")

    def selection_changed(self):
        print("Selection changed")

    def text_edited(self,s):
        print(s)

    def value_changed(self, i):
        print(i)

    def value_changed_str(self, s):
        print(s)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("Slider pressed")

    def slider_released(self):
        print("Slider released")


class MainWindow2(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("yellow"))
        layout2.addWidget(Color("purple"))
        layout1.addLayout(layout2)
        layout1.addWidget(Color("green"))
        layout3.addWidget(Color("blue"))
        layout3.addWidget(Color("orange"))
        layout1.addLayout(layout3)

        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(20)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


class MainWindow3(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QGridLayout()
        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("green"), 1, 0)
        layout.addWidget(Color("blue"), 1, 1)
        layout.addWidget(Color("purple"), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


class MainWindow4(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        page_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stack_layout = QStackedLayout()

        page_layout.addLayout(button_layout)
        page_layout.addLayout(self.stack_layout)

        button = QPushButton("red")
        button.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(button)
        self.stack_layout.addWidget(Color("red"))

        button = QPushButton("green")
        button.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(button)
        self.stack_layout.addWidget(Color("green"))

        button = QPushButton("yellow")
        button.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(button)
        self.stack_layout.addWidget(Color("yellow"))

        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stack_layout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stack_layout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stack_layout.setCurrentIndex(2)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.West)
        tabs.setMovable(True)

        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
