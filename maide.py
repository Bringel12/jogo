from random import randint
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
import os

class MinhaJanela(QMainWindow):
    def __init__(self):
        super(MinhaJanela, self).__init__()

        # Verifica se o arquivo .ui existe
        if not os.path.exists("adivinha.ui"):
            QMessageBox.critical(self, "Erro", "Arquivo 'adivinha.ui' não encontrado.")
            sys.exit(1)

        # Carrega a interface
        loadUi("adivinha.ui", self)

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


# Executa o aplicativo
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec_())
