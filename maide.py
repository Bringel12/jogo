import sys
import os
from random import randint
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

def resource_path(relative_path):
    """Retorna o caminho absoluto para o arquivo, funcionando em script e em executável PyInstaller."""
    try:
        base_path = sys._MEIPASS  # Pasta temporária criada pelo PyInstaller
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class MinhaJanela(QMainWindow):
    def __init__(self):
        super(MinhaJanela, self).__init__()

        # Caminho absoluto para o arquivo .ui
        ui_path = resource_path("adivinha.ui")

        # Verifica se o arquivo .ui existe
        if not os.path.exists(ui_path):
            QMessageBox.critical(self, "Erro", f"Arquivo 'adivinha.ui' não encontrado em:\n{ui_path}")
            sys.exit(1)

        # Carrega a interface
        loadUi(ui_path, self)

        # Conecta os botões às funções
        self.continuar.clicked.connect(self.continuar_jogo)
        self.Reiniciar.clicked.connect(self.reiniciar)

    def reiniciar(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()

    def continuar_jogo(self):
        try:
            numero_usuario = int(self.lineEdit.text())

            if numero_usuario < 0 or numero_usuario > 5:
                self.lineEdit_2.setText("Digite um número entre 0 e 5.")
                return

            computador = randint(0, 5)

            if numero_usuario == computador:
                self.lineEdit_2.setText("Parabéns, você venceu!")
            else:
                self.lineEdit_2.setText(f"Eu ganhei! Pensei no número {computador}.")

        except ValueError:
            self.lineEdit_2.setText("Digite um número válido entre 0 e 5.")

        self.lineEdit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec_())
