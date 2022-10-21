from PyQt5 import QtCore, QtGui, QtWidgets

from calculadora import Ui_MainWindow
        
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pressedButton)

    def pressedButton(self):
        # Esta funcion se manda llamar cuando se presiona el boton sumar.
        # (1) Realiza las operaciones necesarias para obtener los sumandos de los lineEdit's
        #     Y convierte los sumandos de formato texto a formato numerico.
        
        
        # (2) Suma los valores numericos y guarda el resultado en una variable
        
        # (3) Coloca el resultado en el la etiqueta o label donde va el resultado.
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
