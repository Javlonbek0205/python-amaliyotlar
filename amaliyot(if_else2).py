#1)Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring
"""son = int(input("Juft son kiriting:>>"))
if son%2==0:
  print("Raxmat")
else:
  print("Bu son juft emas")"""

#2)Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
"""age = int(input("Yoshingizni kiriting:"))
if age<=4 or age>=60:
  price = 0
elif age<=18:
  price = 10000
else:
  price = 20000
print(f"Siz uchun kirish {price} so`m")"""

#3)Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
"""son1 = float(input("1-sonni kiriting:"))
son2 = float(input("2-sonni kiriting:"))
if son1>son2:
  qiymat = "katta"
elif son1<son2:
  qiymat = "kichik"
else:
  qiymat = "teng"
print(f"1-son qiymati 2-songa nisbatan {qiymat}")"""

#4)mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
"""mahsulot = ['sabzi', 'guruch', 'go`sht', 'piyoz', 'kartoshka', 'tuxum', 'limon', 'bodring', 'pomidor', 'lavlagi']
savat = []
print("5 ta mahsulot nomini kiriting")
for n in range(5):
  savat.append(str(input(f"{n+1}-mahsulot:")))
for buyurtma in savat:
  if buyurtma.lower() in mahsulot:
   print(f"{buyurtma.title()} bizning do`konimizda bor")
  elif buyurtma.lower() not in mahsulot:
    print(f"Kechirasiz bizda {buyurtma} qolmagan")"""

#5)Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
"""mahsulotlar = ['sabzi', 'guruch', 'go`sht', 'piyoz', 'kartoshka', 'tuxum', 'limon', 'bodring', 'pomidor', 'lavlagi']

savat = []
print("5 ta mahsulot nomini kiriting")
for n in range(5):
  savat.append(str(input(f"{n+1}-mahsulot:")))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
  if mahsulot.lower() in mahsulotlar:
    bor_mahsulotlar.append(mahsulot)
  elif mahsulot.lower() not in mahsulotlar:
    mavjud_emas.append(mahsulot)
if mavjud_emas:
  print(f"kechirasiz bu mahsulotlar bizda mavjud emas:")
  for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("siz so`ragan mahsulotlar hammasi bor")"""

#6)foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
"""users = ['admin1', 'boss', 'user', 'salim', 'olim']
login =input("Yangi login kiriting:")

if login in users:
  print("Login band yangi login kiriting")
else:
  print("Xush kelibsiz hurmatli foydalanuvchi")"""

#7)Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
"""son = int(input("Butun son kiriting:"))
qoldiqsiz = []
for i in range(2,11):
  if son%i==0:
    qoldiqsiz.append(i)
print(f"Bu son {qoldiqsiz} sonlarga qoldiqsiz bo`linadi")"""
