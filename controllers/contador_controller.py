from PySide6.QtWidgets import QMainWindow
from ui.tela import Ui_Dialog


class ContadorController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.valor_contador = 0

        self.ui.btn_incrementar.clicked.connect(self.incrementar)
        self.ui.btn_decrementar.clicked.connect(self.decrementar)

        self.atualizar_display()

    def incrementar(self):
        """Lógica para incrementar o valor."""
        self.valor_contador += 1
        self.atualizar_display()

    def decrementar(self):
        """Lógica para decrementar o valor."""
        self.valor_contador -= 1
        self.atualizar_display()

    def atualizar_display(self):
        """Atualiza o texto da QLabel na interface."""
        self.ui.lcdNumber.display(int(self.valor_contador))