from orm_db import *
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
# session oturum acaçarak db üzerinde iş ve işlemler yapmamızı sağlıyor
# bu işlemlerin db ye kaydedilmesini sağlıyor

def kullanici_girisi(eposta,sifre):

    pgirisi = session.query(Personel).filter(Personel.personel_eposta == eposta,
                                             Personel.personel_sifre == sifre).first()
    try:
        if (pgirisi.personel_adi) :
            return [True,pgirisi.mevki_id,pgirisi.personel_id]
    except:
        return 0

def mevkilistele():
    return session.query(Mevki).all()

def birimistele():
    return session.query(Birim).all()


def personel_ekle(personel):
    if len(personel[0]) >10:
        print("uzun fazla bilgi")
        return 0
    else:
        bilgi =Personel(personel_adi=personel[0],
                        personel_eposta=personel[1],
                        personel_sifre=personel[2],
                        birim_id=int(personel[3]),
                        mevki_id=int(personel[4]))
        session.add(bilgi)
        session.commit()
        return 1


def talep_ekle(talep):
    bilgi =Talep(talep_adi=talep[0],talep_tanimi=talep[1],talep_durumu=talep[2],
                 talep_acan=talep[3],talep_giden=talep[4],talep_onemi=talep[5],talep_notlari=talep[6],
                 talep_acilis=talep[7],talep_birimi=talep[8])
    session.add(bilgi)
    session.commit()

def talep_sorgulama(talep_id,talep_birim):
    try:
        talep_bilgisi = session.query(Talep).filter(Talep.talep_id == talep_id,
                                                    Talep.talep_birimi == talep_birim).first()

        if not(talep_bilgisi == None):
            return talep_bilgisi
    except:
        return 0



