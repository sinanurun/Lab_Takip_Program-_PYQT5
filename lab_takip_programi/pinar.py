from PyQt5.QtWidgets import QMainWindow ,QApplication
from pinar_ui import Ui_AnaEkran
import sys
class AnaEkran(QMainWindow,Ui_AnaEkran):
    def __init__(self):
        super(AnaEkran,self).__init__()
        self.setupUi(self)
        self.mTalepEkle.triggered.connect(self.fMesaj)

    def fMesaj(self):
        print(87974654)







app = QApplication(sys.argv)
arayuz = AnaEkran()
arayuz.show()
sys.exit(app.exec_())