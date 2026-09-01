from database.connection import Database
from models.sensor import Sensor

class SensorRepository:

    @staticmethod
    def inserir(sensor: Sensor) -> int:
        """Inserir novo sensor (INSERT parametrizado com ?), recuperar o lastrowid e atualizar o sensor.id."""
        query = "INSERT INTO sensores (nome, tipo, valor_atual) VALUES (?, ?, ?)"
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (sensor.nome, sensor.tipo, sensor.valor_atual))
            conn.commit
            sensor.id = cursor.lastrowid
            return sensor.id

    @staticmethod
    def listar_todos() -> list[Sensor]:
        """Buscar todos os registros (SELECT) e converter cada linha retornada em um objeto Sensor."""
        query = "SELECT id, nome, tipo, valor_atual FROM sensores ORDER BY id ASC"
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            linhas = cursor.fetchall()
            return [
                Sensor(id=l["id"],
                       nome=l["nome"],
                       tipo=l["tipo"],
                       valor_atual=l["valor_atual"])
            for l in linhas]

    @staticmethod
    def buscar_por_id(sensor_id: int) -> Sensor | None:
        """Buscar registro pelo ID com SELECT ... WHERE id = ? e retornar objeto Sensor ou None."""
        query = "SELECT id, nome, tipo, valor_atual FROM sensores WHERE id = ?"

        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (sensor_id,))

            linha = cursor.fetchone()
            if linha:
                return Sensor(
                    id = linha["id"],
                    nome = linha["nome"],
                    tipo = linha["tipo"],
                    valor_atual= linha["valor_atual"]
                )
            return None
            

    @staticmethod
    def atualizar(sensor: Sensor) -> bool:
        """Atualizar nome, tipo e valor_atual com base no ID (UPDATE ... WHERE id = ?)."""
        query = "UPDATE sensores SET nome = ?, tipo = ?, valor_atual = ? WHERE id = ?"
        
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (sensor.nome, sensor.tipo, sensor.valor_atual, sensor.id))
            conn.commit()

        return cursor.rowcount > 0

    @staticmethod
    def deletar(sensor_id: int) -> bool:
        """Deletar registro pelo ID (DELETE FROM ... WHERE id = ?)."""
        query = "DELETE FROM sensores WHERE id = ?"
                
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (sensor_id,))
            conn.commit()

        return cursor.rowcount > 0