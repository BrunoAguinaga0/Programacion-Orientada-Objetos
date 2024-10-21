from PyQt6.QtWidgets import QApplication, QWidget
import sys

class UsoDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100,100,720,480)
        self.setWindowTitle("Ventana Prueba")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = UsoDialog()
    sys.exit(app.exec())