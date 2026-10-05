import sqlite3
from PySide6.QtWidgets import QApplication, QWidget,QPushButton, QVBoxLayout, QLineEdit, QMessageBox

# Rotina de Inicialização e Criação do Banco de Dados
def inicializar_banco():
    try:
        conn = sqlite3.connect("smartgrid.db", timeout=5.0)
        
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS config_sistema (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                tensao_maxima REAL NOT NULL,
                corrente_maxima REAL DEFAULT 30.0
            );
        """)
        
        cursor.execute("""
            INSERT OR IGNORE INTO config_sistema (id, tensao_maxima, corrente_maxima)
            VALUES (1, 220.0, 30.0);
        """)

        conn.commit()

    finally:
        conn.close()


class FormularioExemplo(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configuração")
        self.resize(340, 160)

        layout = QVBoxLayout()
        self.input_tensao = QLineEdit()
        self.input_tensao.setPlaceholderText("Digite a Tensão Limite (ex.: 220.5)")

        self.btn_salvar = QPushButton("Salvar Limite")
        self.btn_salvar.clicked.connect(self.salvar_limite)

        layout.addWidget(self.input_tensao)
        layout.addWidget(self.btn_salvar)
        self.setLayout(layout)

    def salvar_limite(self):
        texto_digitado = self.input_tensao.text().strip()

        try:
            conn = None
            # Validação de campo em branco
            if not texto_digitado:
                raise ValueError("O campo de tensão não pode ficar em branco.")
                
            # Conversão e normalização de vírgula para ponto
            tensao = float(texto_digitado.replace(",", "."))

            # Regra de domínio elétrico
            if tensao <= 0 or tensao > 500:
                raise ValueError("A tensão deve ser entre 0V e 500V")
                
            # Gravação no SQLite
            with sqlite3.connect("smartgrid.db", timeout=3.0) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE config_sistema SET tensao_maxima = ? WHERE id = 1",
                    (tensao,),
                )
                
                # Confirma se a linha foi realmente alterada
                if cursor.rowcount == 0:
                    raise RuntimeError("O registro de configuração não foi encontrado no banco")
                else:
                    QMessageBox.information(self, "Sucesso", f"Tensão de ${tensao}V gravada no banco")
                    self.input_tensao.clear()

        except ValueError as erro_valor:
            QMessageBox.warning(self, "Entrada inválida", str(erro_valor))

        except Exception as erro_inesperado:
            QMessageBox.critical(self, "Falha Critica", f"Erro inesperado: {erro_inesperado}")

        finally:
            print("Executou o finally")
            if conn:
                conn.close()
                print("[DEBUG - FINALLY] Conexão com o banco fechada e recursos liberados.")


if __name__ == "__main__":
    # Garante a criação do banco
    inicializar_banco()

    app = QApplication([])
    janela = FormularioExemplo()
    janela.show()
    app.exec()