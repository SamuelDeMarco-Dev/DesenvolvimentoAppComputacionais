# import sys
# import random
# from PySide6 import QtCore, QtWidgets, QtGui

# class MyWidget(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()

#         self.hello = ["Hello World","Hola Mundo","Olá Mundo"]

#         self.button = QtWidgets.QPushButton("Clique-me")
#         self.text = QtWidgets.QLabel("Hello World",alignment = QtCore.Qt.AlignCenter)

#         self.layout = QtWidgets.QVBoxLayout(self)
#         self.layout.addWidget(self.text)
#         self.layout.addWidget(self.button)

#         self.button.clicked.connect(self.magic)

#     @QtCore.Slot()
#     def magic(self):
#         self.text.setText(random.choice(self.hello))


# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])

#     widget = MyWidget()
#     widget.resize(800,600)

#     widget.show()

#     sys.exit(app.exec())


import sys

from PySide6.QtWidgets import QApplication
from controllers.contador_controller import ContadorController

def main():
    app = QApplication(sys.argv)

    window = ContadorController()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()