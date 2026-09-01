class Sensor:
    def __init__(self, nome: str, tipo: str, valor_atual: float, id: int = None):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.valor_atual = valor_atual

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "tipo": self.tipo,
            "valor_atual": self.valor_atual
        }

    def __repr__(self) -> str:
        return f"<Sensor id={self.id} nome='{self.nome}' tipo='{self.tipo}' valor={self.valor_atual}>"