import sys
import string
import random
import pyqrcode
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QGroupBox, QVBoxLayout, QHBoxLayout, QCheckBox, QPushButton, \
    QLabel, QWidget, QSpinBox, QFileDialog


class sifreci(QWidget):
    def __init__(self):
        super().__init__()
        self.SelfUI()

    def SelfUI(self):
        self.setWindowTitle("Şifreci")
        self.setGeometry(600,200,400,200)
        self.setWindowIcon(QIcon('password.png'))
        self.grb1=QGroupBox("Seçim")
        self.grb2=QGroupBox("Sonuç")

        # sayfa düzenleri
        vbox_anasayfa=QVBoxLayout()
        vbox_grb1=QVBoxLayout()
        hbox_grb2=QHBoxLayout()

        # sayfa içindeki widgetler
        self.sayilar=QCheckBox("Sayılar(0123456789)")
        self.isaretler=QCheckBox("İşaretler(+-*/,!'^+%&/()=?)")
        self.harfler=QCheckBox("Harfler(ABCDEFGHIJKLMNOPQRSTUVWXYZ)")
        self.sifre_üret=QPushButton("Oluştur")
        self.sifre_üret.clicked.connect(self.sifre_uret)
        self.sifre_qr=QPushButton("")
        self.sifre_qr.clicked.connect(self.qrolustur)
        self.sifre_qr.setStyleSheet("background-color:#FAF17C")


        self.sifre_qr.setIcon(QIcon('qr.png'))
        self.sifre_goster=QLabel("       ")
        self.sifre_goster.setStyleSheet("font-size:20px;color:blue;font-weight:bold;")
        self.uzunluk=QSpinBox()
        self.uzunluk.setValue(8)

        #widgetleri sayfa düzenlerini ekleme
        vbox_grb1.addWidget(self.sayilar)
        vbox_grb1.addWidget(self.isaretler)
        vbox_grb1.addWidget(self.harfler)
        vbox_grb1.addWidget(self.uzunluk)
        vbox_grb1.addStretch()

        hbox_grb2.addWidget(self.sifre_goster)
        hbox_grb2.addStretch()
        hbox_grb2.addWidget(self.sifre_üret)

        hbox_grb2.addWidget(self.sifre_qr)
        # groupboxlara sayfa düzenlerini aktarmak

        self.grb1.setLayout(vbox_grb1)
        self.grb2.setLayout(hbox_grb2)
        # anasayfaya groupboxları ekleme

        vbox_anasayfa.addWidget(self.grb1)
        vbox_anasayfa.addWidget(self.grb2)
        # uygulamanın  sayfa düzenini set etmek
        self.setLayout(vbox_anasayfa)
        self.show()


    def sifre_uret(self):
        try:
            length = self.uzunluk.value()
            password = []

            if self.sayilar.isChecked():
                r=list(string.digits)
            else:
                r=list()
            if self.harfler.isChecked():
                h=list(string.ascii_letters)
            else:
                h=list()

            if self.isaretler.isChecked():
                k=list("+-*/,!'^+%&/()=?")
            else:
                k=list()

            self.characters = list(h+ r + k)

            for i in range(length):
                password.append(random.choice(self.characters))

            ## shuffling the resultant password
            random.shuffle(password)
            self.sifre_goster.setText(str("".join(password)))
            self.sifre_goster.setStyleSheet("font-size:20px;color:blue;font-weight:bold;")
        except:
            self.sifre_goster.setText("Lütfen öncelik seçiniz!")
            self.sifre_goster.setStyleSheet("font-size:20px;color:red;font-weight:bold;")


    def qrolustur(self):
        try:
            if self.sifre_goster.text()!="       ":
                dosyaAdi = QFileDialog.getSaveFileName(self,"QR Oluştur","","*.png")
                qr=pyqrcode.create(self.sifre_goster.text())
                qr.png(dosyaAdi[0],scale=8)
            else:
                pass
        except:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = sifreci()
    sys.exit(app.exec())