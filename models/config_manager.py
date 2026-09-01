import json
import os

class ConfigManager:
    DEFAULT_CONFIG = {
        "versao_app": "1.0.0",
        "taxa_atualizacao_ms": 500,
        "limite_alerta": 85.5,
        "modo_operacao": "AUTOMATICO"
    }

    def __init__(self, filename: str = "config.json"):
        self.filename = filename
        self._carregar_ou_criar_padrao()

    def _carregar_ou_criar_padrao(self):
        """Verificar se o arquivo existe. Se não existir, gravar o DEAFULT_CONFIG"""
        if not os.path.exists(self.filename):
            self.salvar(self.DEFAULT_CONFIG)

    def carregar(self) -> dict:
        """Abrir e ler o arquivo JSON (usar bloco try/except com fallback defensivo)."""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except(json.JSONDecodeError, IOError):
            return self.DEFAULT_CONFIG.copy()

    def salvar(self, config_data: dict) -> None:
        """Abrir o arquivo em modo escrita e gravar o dicionário formatado como JSON"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(config_data, f, indent=4, ensure_ascii=False)

    def obter_parametro(self, chave: str):
        config = self.carregar()
        if config:
            return config.get(chave, self.DEFAULT_CONFIG.get(chave))
        return self.DEFAULT_CONFIG.get(chave)