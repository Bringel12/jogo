from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox
import sys


app = QApplication(sys.argv)


jogador = uic.loadUi('adivinha.ui')  

def Reiniciar():
    jogador.lineEdit.clear()
    jogador.lineEdit_2.clear()


def continuar():
    try:
        numero_usuario = int(jogador.lineEdit.text())  
        computador = randint(0, 5)                     
        if numero_usuario == computador:
            jogador.lineEdit_2.setText("Parabéns, você venceu!")
        else:
            jogador.lineEdit_2.setText(f"Eu ganhei! Pensei no número {computador}.")
    except ValueError:
        jogador.lineEdit_2.setText("Digite um número válido de 0 a 5.")
    

    jogador.lineEdit.clear()


jogador.continuar.clicked.connect(continuar)  
jogador.Reiniciar.clicked.connect(Reiniciar)

jogador.show()

sys.exit(app.exec_())
