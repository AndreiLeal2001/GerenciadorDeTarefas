from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QDateTimeEdit, QPushButton, QMessageBox
from PyQt5.QtCore import QDateTime, QTimer
from datetime import datetime

class WidgetAgendamento(QWidget):
    def __init__(self, gerenciador):
        super().__init__()
        self.gerenciador = gerenciador
        self.setWindowTitle("Agendar Tarefa")

        # Layout
        layout = QVBoxLayout()

        # Entrada de descrição
        self.descricao_input = QLineEdit()
        self.descricao_input.setPlaceholderText("Descrição da tarefa")
        layout.addWidget(self.descricao_input)

        # Campo de data e hora
        self.data_hora_input = QDateTimeEdit(QDateTime.currentDateTime())
        self.data_hora_input.setCalendarPopup(True)
        layout.addWidget(self.data_hora_input)

        # Botão de agendar
        agendar_btn = QPushButton("Agendar Tarefa")
        agendar_btn.clicked.connect(self.agendar_tarefa)
        layout.addWidget(agendar_btn)

        self.setLayout(layout)

        # Timer para verificar alarmes
        self.timer = QTimer()
        self.timer.timeout.connect(self.verificar_agendamentos)
        self.timer.start(60000)  # Verifica a cada minuto

    def agendar_tarefa(self):
        descricao = self.descricao_input.text()
        datetime_qt = self.data_hora_input.dateTime()
        data_hora = datetime_qt.toPyDateTime()

        self.gerenciador.agendar_tarefa(descricao, data_hora)
        QMessageBox.information(self, "Tarefa Agendada", f"Tarefa '{descricao}' marcada para {data_hora.strftime('%d/%m/%Y %H:%M')}")
        self.descricao_input.clear()

    def verificar_agendamentos(self):
        agora = datetime.now()
        proximas = self.gerenciador.tarefas_proximas(agora)
        for t in proximas:
            QMessageBox.warning(self, "Alerta de Tarefa", f"Tarefa '{t['descricao']}' está agendada para agora!")