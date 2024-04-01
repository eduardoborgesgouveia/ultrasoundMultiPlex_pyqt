import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicação com Menu Lateral")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.create_side_menu()

    def create_side_menu(self):
        self.btn_conectar_equipamento = QPushButton("Conectar Equipamento")
        self.btn_conectar_equipamento.clicked.connect(self.show_conectar_equipamento)
        self.layout.addWidget(self.btn_conectar_equipamento)

        self.btn_configurar_monitoramento = QPushButton("Configurar Monitoramento")
        self.btn_configurar_monitoramento.clicked.connect(
            self.show_configurar_monitoramento
        )
        self.layout.addWidget(self.btn_configurar_monitoramento)

        self.btn_processar_dados = QPushButton("Processar Dados")
        self.btn_processar_dados.clicked.connect(self.show_processar_dados)
        self.layout.addWidget(self.btn_processar_dados)

    def show_conectar_equipamento(self):
        self.set_current_widget("Conectar Equipamento")

    def show_configurar_monitoramento(self):
        self.set_current_widget("Configurar Monitoramento")

    def show_processar_dados(self):
        self.set_current_widget("Processar Dados")

    def set_current_widget(self, widget_name):
        # Aqui você implementaria a lógica para mostrar o widget correspondente ao botão clicado
        print(f"Mostrando {widget_name}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
