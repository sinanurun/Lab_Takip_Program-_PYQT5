# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musteri_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(538, 378)
        font = QtGui.QFont()
        font.setPointSize(14)
        Form.setFont(font)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(130, 20, 238, 103))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.rnekIdLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.rnekIdLabel.setObjectName("rnekIdLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rnekIdLabel)
        self.talep_id = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.talep_id.setObjectName("talep_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.talep_id)
        self.rnekBirimiLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.rnekBirimiLabel.setObjectName("rnekBirimiLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rnekBirimiLabel)
        self.talep_birimi = QtWidgets.QComboBox(self.formLayoutWidget)
        self.talep_birimi.setObjectName("talep_birimi")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.talep_birimi)
        self.ornek_sorgu_buton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.ornek_sorgu_buton.setObjectName("ornek_sorgu_buton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ornek_sorgu_buton)
        self.ornek_bilgisi = QtWidgets.QLabel(Form)
        self.ornek_bilgisi.setGeometry(QtCore.QRect(60, 170, 431, 151))
        self.ornek_bilgisi.setText("")
        self.ornek_bilgisi.setTextFormat(QtCore.Qt.RichText)
        self.ornek_bilgisi.setScaledContents(True)
        self.ornek_bilgisi.setWordWrap(True)
        self.ornek_bilgisi.setObjectName("ornek_bilgisi")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.rnekIdLabel.setText(_translate("Form", "Örnek id"))
        self.rnekBirimiLabel.setText(_translate("Form", "Örnek Birimi"))
        self.ornek_sorgu_buton.setText(_translate("Form", "Örnek Sorgula"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

