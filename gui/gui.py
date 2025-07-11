from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTextEdit
from GerenciadorDeTarefas import GerenciadorDeTarefas

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
        tarefas = self.gerenciador.listar_tarefas()
        self.output.append(''.join(tarefas))

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()