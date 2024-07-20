#1)Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
"""ismlar = ['Alisher', 'Sarvarbek', 'Olimjon', 'Diyorbek', 'Salimjon']
n=0
for ism in ismlar:
  n+=1
  print(f"Salom hurmatli {ism}, sizni o`quv markazimizga taklif qilamiz")
print(f"kod {n} marta takrorlandi")"""

#2)10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
"""sonlar = []
for son in range(11,100,2):
  sonlar.append(son)
  print(f"{son} ning kubi {son**3} ga teng")
print(sonlar)"""

#3)Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
"""kinolar = []
print("Eng yaxshi ko`rgan 5 kinolaringizni kiriting")
for n in range(5):
  kinolar.append(input(f"{n+1}-kino nomini kiriting:"))
print("Siz yoqtirgan kinolar:",kinolar,"")"""

#4)Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
"""ismlar = []
n = int(input("Nechta odam bilan ko`rishdingiz?:>>"))
for i in range(n):
  ismlar.append(str(input(f"{i+1}-odamning ismi:").title()))
print("Siz ko`rishgan odamlar:",ismlar,"")"""