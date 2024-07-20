#1)otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
"""otam = {}
onam = {}
dostim = {}
otam['ismi']='Jasurbek'
otam['tug`ligan yili']=1980
otam['shahri']='Andijon'
otam['manzil']='Baliqchi'
onam['ismi']='Gulbahor'
onam['tug`ligan yili']=1981
onam['shahri']='Andijon'
onam['manzil']='Baliqchi'
print(f"Otamning ismi {otam['ismi']}, {otam['tug`ligan yili']}-yilda, {otam['manzil']}da tug`ulgan")"""

#2)Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
"""taomlar = {'otam':'osh', 'onam':'shashlik', 'amakim':'manti', 'tog`am':'dimlama'}
print(f"Dadamnining sevimli taomi {taomlar['otam']}")
print(f"Onamning sevimli taomi {taomlar['onam']}")
print(f"Amakimning sevimli taomi {taomlar['amakim']}"""

#3)Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
"""atama = input("Python atamasini kiriting:>>")
python = {'append':'listga yangi qiymat qo`shadi',\
          'title':'matnning birinchi harfini katta harf bilan boshlaydi',\
          'lower':'matnning hamma harfini kichik qilib beradi',\
          'upper':'matnning hamma harfini katta harf qilib beradi',\
          'remove':'listdagi birinchi uchragan qiymatni o`chiradi',\
          'float':'onlik sonlar uchun ishlatiladi',\
          'integer':'butun sonlarni uchun ishlatladi',\
          'if':'shart berish uchun ishlatiladi'}
print(f"{atama.lower()} atamasi {python[atama.lower()]}")"""

#4)Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
#Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
"""soz = input("So`z kiriting:")
sozlar = {'olma':'apple', 'banan':'banana', 'kitob':'book', 'ovqat':'food', 'yemoq':'eat', 'ichmoq':'drink'}

if soz.lower() in sozlar.keys():
  print(f"{soz.title()}ning Inglizchasi: {sozlar[soz.lower()]}")
else:
  print("Kechirasiz bunday so`z kiritilmagan")"""
