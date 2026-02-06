import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()           
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()                
        self.setStyleSheet("border: 5px solid green;")

    def initUI(self):                
        self.setWindowTitle("DIGITAL CLOCK")
        self.setGeometry(500, 400, 300, 150)
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("color: #00E5FF;")
        self.setStyleSheet("background-color: #0F172A;")
        font_id = QFontDatabase.addApplicationFont("digital-font")  
        if font_id == -1:
            my_font = QFont("Helvetica", 40)  
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            my_font = QFont(font_family, 40) 
        self.time_label.setFont(my_font)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss ap")
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
