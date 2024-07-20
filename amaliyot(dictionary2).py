#1)Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.
"""python = {'append':'listga yangi qiymat qo`shadi',\
          'title':'matnning birinchi harfini katta harf bilan boshlaydi',\
          'lower':'matnning hamma harfini kichik qilib beradi',\
          'upper':'matnning hamma harfini katta harf qilib beradi',\
          'remove':'listdagi birinchi uchragan qiymatni o`chiradi',\
          'float':'onlik sonlar uchun ishlatiladi',\
          'integer':'butun sonlarni uchun ishlatladi',\
          'if':'shart berish uchun ishlatiladi'}
for atama in sorted(python.keys()):
  print(atama.title())"""

#2)Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring
"""davlatlar = {'Uzbekistan':'Toshkent', 'Amerika':'Vashington', 'Fransiya':'Paris', 'Rossiya':'Maskva', }
for davlat in sorted(davlatlar):
  print(f"Davlat:{davlat}")
for poytaxt in sorted(davlatlar.values()):
  print(f"Poytaxt:{poytaxt}")"""

#3)Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
"""davlatlar = {'Amsterdam':'Niderlandiya',\
'Andorra-la-Velya':'Andorra',\
'Afina':'Gretsiya',\
'Belgrad':'Serbiya',\
'Berlin':'Germaniya',\
'Bern':'Shveytsariya',\
'Bratislava':'Slovakiya',\
'Brussel':'Belgiya',\
'Budapesht':'Vengriya ',\
'Buxarest':'Ruminiya',\
'Dublin':'Irlandiya',\
'Kiyev':'Ukraina',\
'Kishinyov':'Moldova',\
'Kopengagen':'Daniya',\
'Lissabon':'Portugaliya ',\
'London':'Buyuk Britaniya',\
'Lyublyana':'Sloveniya ',\
'Lyuksemburg':'Lyuksemburg',\
'Madrid':'Ispaniya',\
'Minsk':'Belorussiya',\
'Monako':'Monako',\
'Moskva':'Rossiya',\
'Oslo':'Norvegiya ',\
'Parij':'Fransiya ',\
'Praga':'Chexiya ',\
'Reykyavik':'Islandiya',\
'Riga':'Latviya',\
'Rim':'Italiya',\
'San-Marino':'San Marino ',\
'Sarayevo':'Bosniya',\
'Skopye':'Makedoniya ',\
'Sofiya':'Bolgariya',\
'Stokgolm':'Shvetsiya',\
'Tallin':'Estoniya',\
'Tirana':'Albaniya ',\
'Vaduts':'Lixtenshteyn',\
'Valletta':'	Malta',\
'Varshava':'Polsha',\
'Vatikan':'Vatikan shahri',\
'Vena':'Avstriya',\
'Vilnyus':'Litva',\
'Helsinki':'Finlandiya',\
'Zagreb':'Xorvatiya',\
'Malta qasri':'Malta ordeni',\
'Podgoritsa':'Montenegro',\
'Prishtina':'Kosovo ',\
'Tiraspol':'Transnistria'
}
poytaxt = input("Assalomu alaykum qaysi poytaxt davlatini bilmoqchisiz:>>>")
if poytaxt.title() in davlatlar:
  print(f"{poytaxt.title()} poytaxtining davlati:{davlatlar[poytaxt.title()]}")
else:
  print("Bizda bu malumot yo`q")"""

#4)Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
"""menu = {'mastava':20000,\
        'sho`rva':18000,\
          'dimlama':22000,\
            'shashlik':11000,\
              'somsa':8000,\
                'achchiqgo`sht':25000,\
                  'beshteks':28000}
savat = []
print("3 ta taom kiriting!")
for n in range(3):
  taom = input(f"{n+1}-taomni kiriting:")
  savat.append(taom)
for taom in menu:
  if taom in savat:
    print(f"{taom.title()} ning narxi-{menu[taom.lower()]}so`m")
for food in savat:
  if food not in menu:
    print(f"Bizda {food} yo`q")"""
