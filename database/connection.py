import sqlite3

class Database:
    DB_NAME = "database.db"

    @classmethod
    def get_connection(cls):
        """Criar conexão com sqlite3 e configurar o row_factory como sqlite3.Row."""
        conn = sqlite3.connect(cls.DB_NAME)

        conn.row_factory = sqlite3.Row
        return conn

    @classmethod
    def init_db(cls):
        """Criar a tabela 'sensores' (id, nome, tipo, valor_atual, criado_em) com IF NOT EXISTS."""
        with cls.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sensores(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    valor_atual REAL NOT NULL,
                    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
                )"""
            )
            conn.commit()