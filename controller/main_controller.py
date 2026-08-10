from PySide6.QtWidgets import QMainWindow, QMessageBox
from ui.Ui_janela1 import Ui_MainWindow

class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Conecta o botão à função
        self.ui.btn_validar.clicked.connect(self.validar_nome)

    def validar_nome(self):
        nome = self.ui.txt_nome.text().strip()
        idade  = self.ui.txt_Idade.text().strip()

        if not nome:
            QMessageBox.warning(self, "Atenção", "O campo nome não pode ser nulo!")
        else:
            QMessageBox.information(self, "Sucesso", f"Seja bem-vindo, {nome}")

        if not idade:
            QMessageBox.warning(self, "Atenção", "O campo idade não pode ser nulo!")
        else:
            if idade < "18":
                QMessageBox.information(self, "Atenção", "Você é menor de idade")
            else:
                QMessageBox.information(self, "Sucesso", "Você ja é adulto")