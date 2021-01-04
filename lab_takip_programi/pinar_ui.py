# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pinar_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AnaEkran(object):
    def setupUi(self, AnaEkran):
        AnaEkran.setObjectName("AnaEkran")
        AnaEkran.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AnaEkran)
        self.centralwidget.setObjectName("centralwidget")
        AnaEkran.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AnaEkran)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuTalep_i_lemleri = QtWidgets.QMenu(self.menubar)
        self.menuTalep_i_lemleri.setObjectName("menuTalep_i_lemleri")
        AnaEkran.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AnaEkran)
        self.statusbar.setObjectName("statusbar")
        AnaEkran.setStatusBar(self.statusbar)
        self.mTalepEkle = QtWidgets.QAction(AnaEkran)
        self.mTalepEkle.setObjectName("mTalepEkle")
        self.menuTalep_i_lemleri.addAction(self.mTalepEkle)
        self.menubar.addAction(self.menuTalep_i_lemleri.menuAction())

        self.retranslateUi(AnaEkran)
        QtCore.QMetaObject.connectSlotsByName(AnaEkran)

    def retranslateUi(self, AnaEkran):
        _translate = QtCore.QCoreApplication.translate
        AnaEkran.setWindowTitle(_translate("AnaEkran", "MainWindow"))
        self.menuTalep_i_lemleri.setTitle(_translate("AnaEkran", "Talep işlemleri"))
        self.mTalepEkle.setText(_translate("AnaEkran", "talep ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AnaEkran = QtWidgets.QMainWindow()
    ui = Ui_AnaEkran()
    ui.setupUi(AnaEkran)
    AnaEkran.show()
    sys.exit(app.exec_())

