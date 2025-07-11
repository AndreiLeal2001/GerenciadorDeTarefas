from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem,
    QCheckBox, QInputDialog, QMessageBox, QDateTimeEdit
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QDateTime
from core.tarefas import GerenciadorDeTarefas

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do Style - Gerenciador de Tarefas")
        self.setMinimumSize(700, 800)
        self.setStyleSheet("background-color: #2c3e50; color: #ecf0f1;")

        self.gerenciador = GerenciadorDeTarefas()

        self.init_ui()

    def init_ui(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)

        # Cabeçalho
        header = QLabel("📋 Minhas Tarefas")
        header.setFont(QFont("Segoe UI", 24, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)

        # Campo de entrada
        self.input_descricao = QLineEdit()
        self.input_descricao.setPlaceholderText("Adicionar uma nova tarefa")
        self.input_descricao.setStyleSheet("padding: 12px; font-size: 16px; border: 1px solid #ccc; border-radius: 6px; background-color: #34495e; color: #ecf0f1;")
        self.input_descricao.returnPressed.connect(self.adicionar_tarefa)

        # Data/Hora atual
        self.input_data = QDateTimeEdit(QDateTime.currentDateTime())
        self.input_data.setCalendarPopup(True)
        self.input_data.setStyleSheet("padding: 10px; font-size: 14px; background-color: #34495e; color: #ecf0f1;")

        form_layout = QHBoxLayout()
        form_layout.addWidget(self.input_descricao)
        form_layout.addWidget(self.input_data)
        main_layout.addLayout(form_layout)

        # Lista de tarefas
        self.lista_tarefas = QListWidget()
        self.lista_tarefas.setStyleSheet("padding: 10px; font-size: 15px; background-color: #34495e; color: #ecf0f1;")
        main_layout.addWidget(self.lista_tarefas)

        # Barra inferior com botões
        barra_layout = QHBoxLayout()
        for texto, slot, cor in [
            ("Listar", self.listar_tarefas, "#3498db"),
            ("Buscar", self.buscar_tarefa, "#9b59b6")
        ]:
            btn = QPushButton(texto)
            btn.setStyleSheet(self.button_style(cor))
            btn.clicked.connect(slot)
            barra_layout.addWidget(btn)

        main_layout.addLayout(barra_layout)

        self.setCentralWidget(main_widget)

    def button_style(self, color):
        return f'''
        QPushButton {{
            background-color: {color};
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 14px;
            font-weight: bold;
        }}
        QPushButton:hover {{
            background-color: darken({color}, 10%);
        }}
        '''

    def adicionar_tarefa(self):
        desc = self.input_descricao.text().strip()
        data = self.input_data.dateTime().toString()
        if desc:
            self.gerenciador.adicionar_tarefa(desc, data)
            self.input_descricao.clear()
            self.input_data.setDateTime(QDateTime.currentDateTime())
            self.listar_tarefas()
        else:
            QMessageBox.warning(self, "Atenção", "Digite a descrição da tarefa.")

    def listar_tarefas(self):
        self.lista_tarefas.clear()
        tarefas = self.gerenciador.listar_tarefas()
        for tarefa in tarefas:
            item = QListWidgetItem()
            checkbox = QCheckBox(tarefa)
            checkbox.stateChanged.connect(lambda state, desc=tarefa, cb=checkbox: self.marcar_tarefa(cb, desc, state))
            self.lista_tarefas.addItem(item)
            self.lista_tarefas.setItemWidget(item, checkbox)

    def buscar_tarefa(self):
        chave, ok = QInputDialog.getText(self, "Buscar", "Palavra-chave:")
        if ok and chave:
            self.lista_tarefas.clear()
            resultados = self.gerenciador.buscar_tarefa(chave)
            for r in resultados:
                item = QListWidgetItem()
                checkbox = QCheckBox(r["descricao"])
                checkbox.stateChanged.connect(lambda state, desc=r["descricao"], cb=checkbox: self.marcar_tarefa(cb, desc, state))
                self.lista_tarefas.addItem(item)
                self.lista_tarefas.setItemWidget(item, checkbox)

    def marcar_tarefa(self, checkbox, descricao, estado):
        if estado == Qt.Checked:
            checkbox.setText(f"✔️ {descricao}")
            checkbox.setStyleSheet("text-decoration: line-through; color: gray;")
            self.exibir_opcoes(descricao)
        else:
            checkbox.setText(descricao)
            checkbox.setStyleSheet("")

    def exibir_opcoes(self, descricao):
        escolha, ok = QInputDialog.getItem(
            self, "Ação para Tarefa",
            f"Tarefa: {descricao}O que deseja fazer?",
            ["Editar", "Excluir", "Cancelar"], 0, False
        )
        if ok:
            if escolha == "Editar":
                nova, ok2 = QInputDialog.getText(self, "Editar Tarefa", "Nova descrição:")
                if ok2 and nova:
                    self.gerenciador.editar_tarefa(descricao, nova)
                    self.listar_tarefas()
            elif escolha == "Excluir":
                confirm = QMessageBox.question(self, "Confirmação", f"Excluir tarefa '{descricao}'?",
                                               QMessageBox.Yes | QMessageBox.No)
                if confirm == QMessageBox.Yes:
                    self.gerenciador.excluir_tarefa(descricao)
                    self.listar_tarefas()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())