"""
bu bölümde orm yapısı kullanılarak db iş ve işlemleri gerçekleştirilmektedir.
tablo tanımları vb işlmler
sqlinjection
PYQT5
"""
# from sqlalchemy import Column, ForeignKey, Integer, String # yerine * da olabilirdi
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *  #tablolar arası ilişki kurmak için
from sqlalchemy import *

Base = declarative_base()

# lab işlemleri için db orm yapısı
class Birim(Base):
    #tablo adı
    __tablename__ = 'birim'
    #tablo sutunları ve özellikleri varsa da ilişkileri
    birim_id = Column(Integer, unique= True, primary_key=True, autoincrement= True)
    birim_adi = Column(String(250), nullable=False)


class Isdurumu(Base):
    __tablename__ = 'isdurumu'
    isdurumu_id = Column(Integer,unique=True, primary_key=True, autoincrement= True)
    isdurumu_tanimi_adi = Column(String(250), unique=True)

class Mevki(Base):
    __tablename__ = 'mevki'
    mevki_id = Column(Integer,unique=True, primary_key=True, autoincrement= True)
    mevki_adi = Column(String(250),unique=True)


class Personel(Base):
    __tablename__ = 'personel'
    personel_id = Column(Integer,unique=True, primary_key=True, autoincrement= True)
    personel_adi = Column(String(5))
    personel_eposta = Column(String(100),unique=True)
    personel_sifre = Column(String(100))
    birim_id = Column(Integer,ForeignKey('birim.birim_id'))
    birim = relationship(Birim, backref='personel')
    mevki_id = Column(Integer,ForeignKey('mevki.mevki_id'))
    mevki = relationship(Mevki, backref='personel')


class Talep(Base):
    __tablename__ = 'talep'

    talep_id = Column(Integer,unique=True, primary_key=True, autoincrement= True)
    talep_adi = Column(String(100))
    talep_tanimi = Column(String(100))
    talep_durumu= Column(Integer())
    talep_acan = Column(Integer,ForeignKey('personel.personel_id'))
    talepacan = relationship(Personel, foreign_keys=[talep_acan])
    talep_giden = Column(Integer,ForeignKey('personel.personel_id'))
    talepgiden = relationship(Personel, foreign_keys=[talep_giden])
    talep_onemi =Column(Integer)
    talep_notlari = Column(String(250))
    talep_acilis = Column(String(250))
    talep_kapanis = Column(String(250))
    talep_birimi = Column(Integer,ForeignKey('birim.birim_id'))


# sqlite olarak kayıtedilecek dosyayı gösteriyoruz
engine = create_engine('sqlite:///lab_takip.sqlite')

# Tanımladığımız Base üzerindeki tabloları oluşturuyoruz
Base.metadata.create_all(engine)