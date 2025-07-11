import logging

# Configurações do log
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s",
    filename="app.log",
    filemode="a",  # "w" sobrescreve; "a" adiciona ao final
    encoding="utf-8"
)

# Atalho para usar o logger em outros módulos
logger = logging.getLogger(__name__)