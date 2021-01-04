from musteri_ui import Ui_Form as Musteri_Ui
from PyQt5.QtWidgets import *
from db_islemleri import *
import sys
import time

class Musteri_Ekrani(QWidget,Musteri_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        birim_listesi = birimistele()
        for birim in birim_listesi:
            self.talep_birimi.addItem(birim.birim_adi)

        self.ornek_sorgu_buton.clicked.connect(self.f_ornek_sorgu)

    def f_ornek_sorgu(self):
        talep_id = int(self.talep_id.text())
        birim = self.talep_birimi.currentIndex()+1
        try:
            talep_bilgisi = talep_sorgulama(talep_id,birim)
            if talep_bilgisi !=0:
                ornek_bilgisi = "Talep Adı: {},<br>" \
                                "Talep Tanımı: {}<br>" \
                                "Talep Durumu: {}<br>" \
                                "Talep Açıklması:{}".format(talep_bilgisi.talep_adi,
                                                            talep_bilgisi.talep_tanimi,
                                                            "İşlem Devam Ediyor" if talep_bilgisi.talep_durumu!=0 else "Sonuçları Teslim Alabilirsiniz",
                                                            talep_bilgisi.talep_notlari)
                self.ornek_bilgisi.setText(ornek_bilgisi)
            else:
                self.ornek_bilgisi.setText("Aradığınız Numune Bulunamadı")
        except:
            self.ornek_bilgisi.setText("Aradığınız Numune Bulunamadı")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Musteri_Ekrani()
    pencere.show()
    sys.exit(app.exec_())