from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton,
    QLineEdit, QTextEdit, QLabel, QHBoxLayout, QMessageBox,
    QDateTimeEdit, QInputDialog, QSizePolicy, QListWidget, QListWidgetItem, QCheckBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from core.tarefas import GerenciadorDeTarefas

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('✨ Gerenciador de Tarefas')
        self.resize(600, 700)  # Agora é redimensionável
        self.setStyleSheet("background-color: #f4f4f4;")

        self.gerenciador = GerenciadorDeTarefas()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Título
        titulo = QLabel("Gerencie Suas Tarefas")
        titulo.setFont(QFont("Arial", 18, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo)

        # Campo de entrada
        self.input_descricao = QLineEdit()
        self.input_descricao.setPlaceholderText('Digite uma nova tarefa...')
        self.input_descricao.setStyleSheet("padding: 10px; font-size: 14px;")
        layout.addWidget(self.input_descricao)

        # Campo de data/hora
        self.input_data = QDateTimeEdit()
        self.input_data.setCalendarPopup(True)
        self.input_data.setStyleSheet("padding: 10px; font-size: 14px;")
        layout.addWidget(self.input_data)

        # Botões
        btn_layout = QHBoxLayout()
        for nome, func in [
            ("Adicionar", self.adicionar_tarefa),
            ("Listar", self.listar_tarefas),
            ("Excluir", self.excluir_tarefa),
            ("Editar", self.editar_tarefa),
            ("Buscar", self.buscar_tarefa)
        ]:
            btn = QPushButton(nome)
            btn.setStyleSheet(self.button_style())
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
            btn.clicked.connect(func)
            btn_layout.addWidget(btn)

        layout.addLayout(btn_layout)

        # Lista de tarefas
        self.tarefa_list_widget = QListWidget()
        self.tarefa_list_widget.setStyleSheet("background-color: #fff; font-size: 13px; margin-bottom: 10px;")
        layout.addWidget(self.tarefa_list_widget)

        # Área de saída
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet("background-color: #fff; padding: 10px; font-size: 13px;")
        layout.addWidget(self.output)

        # Widget central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def button_style(self):
        return (
            "QPushButton {"
            "  background-color: #3498db;"
            "  color: white;"
            "  padding: 12px 20px;"
            "  margin: 4px;"
            "  border-radius: 6px;"
            "  font-weight: bold;"
            "  font-size: 14px;"
            "}"
            "QPushButton:hover {"
            "  background-color: #2980b9;"
            "}"
        )

    def adicionar_tarefa(self):
        descricao = self.input_descricao.text().strip()
        data = self.input_data.dateTime().toString()
        if descricao:
            self.gerenciador.adicionar_tarefa(descricao, data)
            self.output.append(f'✅ Tarefa adicionada: "{descricao}" com data "{data}"')
            self.input_descricao.clear()
        else:
            QMessageBox.warning(self, "Campo vazio", "Por favor, digite uma tarefa antes de adicionar.")

    def listar_tarefas(self):
        self.tarefa_list_widget.clear()
        tarefas = self.gerenciador.listar_tarefas()
        for tarefa in tarefas:
            item = QListWidgetItem()
            checkbox = QCheckBox(tarefa)
            checkbox.setStyleSheet("margin: 4px;")
            checkbox.stateChanged.connect(lambda state, desc=tarefa, cb=checkbox: self.marcar_completo(cb, desc, state))
            self.tarefa_list_widget.addItem(item)
            self.tarefa_list_widget.setItemWidget(item, checkbox)
        else:
            self.output.append("\n🚫 Nenhuma tarefa cadastrada.")

    def marcar_completo(self, checkbox, descricao, state):
        if state == Qt.Checked:
            checkbox.setText(f"✔️ {descricao}")
            checkbox.setStyleSheet("margin: 4px; text-decoration: line-through; color: gray;")
            self.exibir_opcoes(descricao)
        else:
            checkbox.setText(descricao)
            checkbox.setStyleSheet("margin: 4px;")

    def excluir_tarefa(self):
        descricao = self.input_descricao.text().strip()
        if descricao:
            confirmacao = QMessageBox.question(self, 'Confirmação', f'Tem certeza que deseja excluir a tarefa "{descricao}"?',
                                               QMessageBox.Yes | QMessageBox.No)
            if confirmacao == QMessageBox.Yes:
                self.gerenciador.excluir_tarefa(descricao)
                self.output.append(f'🗑️ Tarefa excluída: "{descricao}"')
        else:
            QMessageBox.warning(self, "Campo vazio", "Digite a tarefa que deseja excluir.")

    def editar_tarefa(self):
        descricao_antiga = self.input_descricao.text().strip()
        descricao_nova, ok = QInputDialog.getText(self, "Editar Tarefa", "Digite a nova descrição:")
        if ok and descricao_antiga and descricao_nova:
            self.gerenciador.editar_tarefa(descricao_antiga, descricao_nova)
            self.output.append(f'✏️ Tarefa editada: "{descricao_antiga}" para "{descricao_nova}"')
        else:
            QMessageBox.warning(self, "Campo vazio", "Digite uma tarefa para editar.")

    def buscar_tarefa(self):
        palavra_chave, ok = QInputDialog.getText(self, "Buscar Tarefa", "Digite a palavra-chave:")
        if ok and palavra_chave:
            self.tarefa_list_widget.clear()
            resultados = self.gerenciador.buscar_tarefa(palavra_chave)
            if resultados:
                for r in resultados:
                    item = QListWidgetItem()
                    checkbox = QCheckBox(r["descricao"])
                    checkbox.setStyleSheet("margin: 4px;")
                    checkbox.stateChanged.connect(lambda state, desc=r["descricao"], cb=checkbox: self.marcar_completo(cb, desc, state))
                    self.tarefa_list_widget.addItem(item)
                    self.tarefa_list_widget.setItemWidget(item, checkbox)
            else:
                QMessageBox.information(self, "Busca", f'Nenhuma tarefa encontrada para: "{palavra_chave}"')
        else:
            QMessageBox.warning(self, "Campo vazio", "Digite uma palavra-chave para buscar.")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
