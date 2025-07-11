from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTextEdit, QMessageBox
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gerenciador de Tarefas')

        self.gerenciador = GerenciadorDeTarefas()

        # Layout principal
        layout = QVBoxLayout()

        # Campo de entrada
        self.input_descricao = QLineEdit()
        self.input_descricao.setPlaceholderText('Descrição da Tarefa')
        layout.addWidget(self.input_descricao)

        # Botões
        btn_adicionar = QPushButton('Adicionar Tarefa')
        btn_adicionar.clicked.connect(self.adicionar_tarefa)
        layout.addWidget(btn_adicionar)

        btn_listar = QPushButton('Listar Tarefas')
        btn_listar.clicked.connect(self.listar_tarefas)
        layout.addWidget(btn_listar)

        # Área de saída
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        # Widget central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def adicionar_tarefa(self):
        descricao = self.input_descricao.text()
        self.gerenciador.adicionar_tarefa(descricao)
        self.output.append(f'Tarefa "{descricao}" adicionada!')
        self.input_descricao.clear()

    def listar_tarefas(self):
        tarefas_formatadas = []
        for t in self.tarefas:
            concluida = t.get("concluida", False)
            tarefas_formatadas.append(f'{"[X]" if concluida else "[ ]"} {t["descricao"]}')
        return tarefas_formatadas

    def excluir_tarefa(self, descricao):
        confirmacao = QMessageBox.question(self, 'Confirmação', f'Tem certeza que deseja excluir a tarefa "{descricao}"?',
                                           QMessageBox.Yes | QMessageBox.No)
        if confirmacao == QMessageBox.Yes:
            self.gerenciador.excluir_tarefa(descricao)
            self.output.append(f'Tarefa "{descricao}" excluída!')
        else:
            self.output.append(f'Exclusão de tarefa cancelada: "{descricao}".')

    def concluir_tarefa(self, descricao):
        try:
            self.gerenciador.concluir_tarefa(descricao)
            self.output.append(f'Tarefa "{descricao}" concluída!')
        except Exception as e:
            QMessageBox.critical(self, 'Erro', f'Erro ao concluir tarefa: {e}')

    def editar_tarefa(self, descricao_antiga, descricao_nova):
        try:
            self.gerenciador.editar_tarefa(descricao_antiga, descricao_nova)
            self.output.append(f'Tarefa "{descricao_antiga}" editada para "{descricao_nova}"!')
        except Exception as e:
            QMessageBox.critical(self, 'Erro', f'Erro ao editar tarefa: {e}')

    def buscar_tarefa(self, palavra_chave):
        try:
            resultados = self.gerenciador.buscar_tarefa(palavra_chave)
            if resultados:
                self.output.append(f'Resultados da busca por "{palavra_chave}": ' + ''.join([t['descricao'] for t in resultados]))
            else:
                self.output.append(f'Nenhuma tarefa encontrada para a palavra-chave: "{palavra_chave}".')
        except Exception as e:
            QMessageBox.critical(self, 'Erro', f'Erro ao buscar tarefa: {e}')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

import json
import os

# Caminho absoluto até a pasta /data (um nível acima de /core)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
ARQUIVO = os.path.join(DATA_DIR, 'tarefas.json')

# Garante que a pasta /data existe
os.makedirs(DATA_DIR, exist_ok=True)

def salvar_tarefas(tarefas):
    """Salvar a lista de tarefas em formato JSON."""
    with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

def carregar_tarefas():
    """Carregar as tarefas do arquivo JSON, se existir."""
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    return []

import logging
from core.storage import salvar_tarefas, carregar_tarefas

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GerenciadorDeTarefas:
    def __init__(self):
        try:
            self.tarefas = carregar_tarefas()
            logger.info('Tarefas carregadas com sucesso.')
        except Exception as e:
            logger.error(f'Erro ao carregar tarefas: {e}')
            self.tarefas = []

    def adicionar_tarefa(self, descricao, data=None):
        try:
            if not descricao:
                raise ValueError('Descrição da tarefa não pode ser vazia.')
            tarefa = {
            'descricao': descricao,
            'concluida': False
            }
            if data:
                tarefa['data'] = data
            self.tarefas.append(tarefa)
            salvar_tarefas(self.tarefas)
            logger.info(f'Tarefa adicionada: {descricao}')
        except Exception as e:
            logger.error(f'Erro ao adicionar tarefa: {e}')

    def listar_tarefas(self):
        return [f'{"[X]" if t["concluida"] else "[ ]"} {t["descricao"]}' for t in self.tarefas]

    def buscar_tarefa(self, palavra_chave):
        try:
            resultados = [t for t in self.tarefas if palavra_chave.lower() in t['descricao'].lower()]
            logger.info(f'Busca realizada por palavra-chave: {palavra_chave}')
            return resultados
        except Exception as e:
            logger.error(f'Erro ao buscar tarefa: {e}')
            return []

    def concluir_tarefa(self, descricao):
        try:
            for tarefa in self.tarefas:
                if tarefa['descricao'] == descricao:
                    tarefa['concluida'] = True
                    salvar_tarefas(self.tarefas)
                    logger.info(f'Tarefa concluída: {descricao}')
                    return
            logger.warning(f'Tarefa não encontrada para conclusão: {descricao}')
        except Exception as e:
            logger.error(f'Erro ao concluir tarefa: {e}')

    def editar_tarefa(self, descricao_antiga, descricao_nova):
        try:
            for tarefa in self.tarefas:
                if tarefa['descricao'] == descricao_antiga:
                    tarefa['descricao'] = descricao_nova
                    salvar_tarefas(self.tarefas)
                    logger.info(f'Tarefa editada: {descricao_antiga} -> {descricao_nova}')
                    return
            logger.warning(f'Tarefa não encontrada para edição: {descricao_antiga}')
        except Exception as e:
            logger.error(f'Erro ao editar tarefa: {e}')

    def excluir_tarefa(self, descricao):
        try:
            self.tarefas = [t for t in self.tarefas if t['descricao'] != descricao]
            salvar_tarefas(self.tarefas)
            logger.info(f'Tarefa excluída: {descricao}')
        except Exception as e:
            logger.error(f'Erro ao excluir tarefa: {e}')