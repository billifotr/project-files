import sys
from PyQt6.QtCore import Qt

# from PyQt6.QtGui import QGuiApplication

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QHBoxLayout, QLayout, QPushButton

# from PyQt6.QtQml import QQmlApplicationEngine
# from PyQt6.QtQuick import QQuickWindow

class Color(QWidget):
  
  def __init__(self, color):
    super(Color, self).__init__()

    # self.autoFillBackground(True)

    palette = self.palette()
    palette.setColor(QPalette.ColorRole.Window, QColor(color))
    self.setPalette(palette)

class MainWindow(QMainWindow):

  def __init__(self):
    super(MainWindow, self).__init__()

    self.setWindowTitle("App")
    self.setMinimumSize(1024, 512)

    widget = QWidget()
    layout = QHBoxLayout()

    button1 = QPushButton("Add")
    button2 = QPushButton("Take")

    layout.addWidget(button1)
    layout.addWidget(button2)
    
    widget.setLayout(layout)
    self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

# QQuickWindow.setSceneGraphBackend('software')

# app = QGuiApplication(sys.argv)

# engine = QQmlApplicationEngine()
# engine.quit.connect(app.quit)
# engine.load('./UI/main.qml')

# sys.exit(app.exec())
