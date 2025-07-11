import sys
from PyQt5.QtWidgets import QApplication
from gui.gui import MainWindow
# Certifique-se que o caminho está correto

def main():
    # Cria a instância da aplicação
    app = QApplication(sys.argv)

    # Inicializa a janela principal
    window = MainWindow()
    window.show()

    # Executa a aplicação
    sys.exit(app.exec())
    
if __name__ == '__main__':
    main()
