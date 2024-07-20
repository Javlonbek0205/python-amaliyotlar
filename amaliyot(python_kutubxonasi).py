#1)Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring
"""from datetime import datetime, timedelta

# Bugungi sana
bugun = datetime.today()

# 2 hafta keyin sanalar
ikki_hafta_ildiz = timedelta(weeks=2)
ikki_hafta_keyin = bugun + ikki_hafta_ildiz

# 10 kun orqaga sanalar
sanalar = []
for i in range(10):
    kun_ildiz = timedelta(days=i)
    kun_sana = ikki_hafta_keyin + kun_ildiz
    sanalar.append(kun_sana.strftime('%Y-%m-%d'))


# Konsolga chiqarish
print("Bugungi sana:", bugun.strftime('%Y-%m-%d'))
print("2 hafta keyin:", ikki_hafta_keyin.strftime('%Y-%m-%d'))
print("10 kun sanalar:")
sanalar.sort(reverse=False)
for sana in sanalar:
    print(sana)"""

#2)Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring
"""import datetime as dt

hozir = dt.datetime.now()

bugun = dt.date.today()
qurbon_hayit = dt.date(2024, 6, 16)
oraliq = bugun - qurbon_hayit
print(f"Qurbon hayitidan {oraliq.days} kun o`tdi")"""

#3)Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun o'tganini qaytaruvchi funksiya yozing
"""import datetime as dt
x=int(input("Tug`ilgan yilingizni kiriting: "))
y=int(input("Tug`ilgan oyni kiriting: "))
z=int(input("Tug`ligan sanangizni kiriting: "))

try:
  t_sana = [x,y,z]
  t_sana = dt.date(x,y,z)
except:
  print("Ma'lumot xato kiritildi!!!")


else:
  bugun = dt.date.today()
  farq = bugun - t_sana
  year = farq.days//365
  month = (farq.days-(year*365))//30
  day = farq.days-(year*365+month*30)
  print(f"Siz tug`ilganingizga taxminan: {year} yil\n"
      f"{month} oy\n"
      f"{day} kun bo`ldi")
  print(f"Jami yashagan kunlaringiz: {farq.days}")
print(t_sana)"""

#4)Foydalanuvchidan telefon raqamini kiritishni so'rang. Kiritlgan qiymatni andoza yordamida tekshiring
"""import re
andoza_t ='^998?[0-9]{2}?[0-9]{3}?[0-9]{2}?[0-9]{2}$'
t_raqam = "Telefon  raqamingizni kiriting (uzb davlat kodi bilan:998): "
raqamlar = []
while True:
  tel_raqam = input(t_raqam)
  if re.match(andoza_t, tel_raqam):
    raqamlar.append(tel_raqam)
    print("Raqamingiz muvafaqqiyatli qabul qilindi")
    break
  else:
    print("Xato malumot!!!")
print(raqamlar)"""

#5)Berilgan matndan veb sahifa manzilini ajratib olyuvchi funksiya yozing. Quyidagi matndan namuna sifatida foydalanishingiz mumkin: Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test
import re
url =[]
def url_ajrat(matn):
  andoza_url = 'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'
  task = str(matn)
  if re.match(andoza_url,task):
    url.append(task)
    print(f"Url manzillar: {url}")
  else:
    print("Bu matnda url mazil yo`q")
url_ajrat("https://youtu.be/vsxJPRLXpgI Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test")