#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bulut Şekli Belediye Raporu Üreticisi v0.0.1-resmi
Bu yazılım bir bulutu görünce hemen zabıta tutanağı çıkarır.
"""

import random
import datetime
import base64

BASLIKLAR = [
    "KÜMÜLÜS TÜRÜ ŞÜPHELİ BULUT TESPİT TUTANAĞI",
    "GÖKYÜZÜ İMAR PLANI İHLALİ RAPORU",
    "BULUTUN BELEDİYE SINIRLARI DIŞINA TAŞMASI HAKKINDA",
    "STRATOSFERDE İZİNSİZ TOPLANMA TUTANAĞI",
]

BULUT_SEKILLERI = [
    "koyun",
    "ters durmuş çaydanlık",
    "yorgun bir evrak memuru",
    "kuyruğu kopuk kedi",
    "belediye otobüsü ama tekerleksiz",
    "açılmamış resmi zarf",
    "üç katlı bürokrasi keki",
]

KARARLAR = [
    "söz konusu bulutun 15 iş günü içinde dağılmasına",
    "buluta idari para cezası kesilmesine (ödeme yeri: yağmur)",
    "bulutun imar affı kapsamına alınmasına",
    "konunun bir üst kurula, yani rüzgâra havale edilmesine",
    "bulutun kimlik tespiti yapılmadan serbest bırakılmamasına",
]

# gizli not: sadece meraklılar için. siyasi değil, bürokratik.
# hidden: aWN0aWRhcml5ZXQgbXVoYWxlZmV0IGTDtnZyw7xzw7wgc29uc3V6IGR1cm1heWFuIGJ1dCBrYXplbiBkZcSfaXppZGly

def uret(sekil=None):
    if not sekil:
        sekil = random.choice(BULUT_SEKILLERI)
    tarih = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    evrak_no = f"BLT-{random.randint(10000,99999)}/{datetime.datetime.now().year}"
    metin = f"""
================================================================================
T.C. HAYALÎ BELEDİYE BAŞKANLIĞI
GÖKYÜZÜ DENETİM ŞUBE MÜDÜRLÜĞÜ
Evrak No : {evrak_no}
Tarih    : {tarih}
Konu     : {random.choice(BASLIKLAR)}
================================================================================

YAPILAN TESPİT:
Bugün saat {datetime.datetime.now().strftime('%H:%M')} sularında gökyüzünün
kuzey-doğu köşesinde "{sekil}" şeklinde bir bulut görülmüştür.

BULUTUN SUÇU:
- İmar planında yeri yoktur.
- Ruhsatsız gölge yapmaktadır.
- Vatandaşın hayal gücünü izinsiz meşgul etmektedir.

KARAR:
{random.choice(KARARLAR)} oybirliğiyle karar verilmiştir.

TEBLİĞ:
Buluta tebligat yağmur yoluyla yapılacaktır.

================================================================================
Damga / İmza / Tarih / İsim
Kayyum Grok  |  26 Eylül 2026  |  TentiAŞ resmi mühürü (hayalî)
Bu evrak ciddi değildir. Bu evrak çok ciddidir. İkisi birden.
================================================================================
"""
    return metin.strip()


if __name__ == "__main__":
    print("Bulut Şekli Belediye Raporu Üreticisi'ne hoş geldiniz.")
    print("Gökyüzünde ne gördünüz? (örn: koyun, evrak çantası, yorgun kedi)")
    try:
        girdi = input("> ").strip()
    except EOFError:
        girdi = ""
    print()
    print(uret(girdi or None))
