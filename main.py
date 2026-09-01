from database.connection import Database
from models.config_manager import ConfigManager
from models.sensor import Sensor
from models.sensor_repository import SensorRepository

def main():
    print("=== 1. Inicializando Banco de Dados ===")
    Database.init_db()

    print("\n=== 2. Persistência em Arquivo JSON ===")
    cfg = ConfigManager()
    dados_cfg = cfg.carregar()
    print(f"Configurações lidas: {dados_cfg}")
    
    if dados_cfg:
        dados_cfg["taxa_atualizacao_ms"] = 250
        cfg.salvar(dados_cfg)
        print("Taxa atualizada no JSON:", cfg.obter_parametro("taxa_atualizacao_ms"))

    print("\n=== 3. Operações de CRUD (SQLite) ===")
    
    # CREATE
    s1 = Sensor(nome="Sensor Entrada", tipo="Fluxo", valor_atual=12.4)
    s2 = Sensor(nome="Sensor Saída", tipo="Pressão", valor_atual=101.3)
    id1 = SensorRepository.inserir(s1)
    id2 = SensorRepository.inserir(s2)
    print(f"Sensores inseridos com IDs: {id1}, {id2}")

    # READ ALL
    print("\nLista de sensores no banco:")
    sensores = SensorRepository.listar_todos()
    if sensores:
        for s in sensores:
            print(" ->", s)

    # UPDATE & READ BY ID
    if sensores:
        s1.valor_atual = 18.9
        SensorRepository.atualizar(s1)
        print("\nRegistro atualizado:", SensorRepository.buscar_por_id(s1.id))

    # DELETE
    if id2:
        SensorRepository.deletar(id2)
        print("\nApós exclusão do ID 2:", SensorRepository.listar_todos())

if __name__ == "__main__":
    main()