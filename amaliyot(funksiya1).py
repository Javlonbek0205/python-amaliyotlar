##1)Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
#def malumot_ber(name, age=int):
#   """Foydalanuvchui haqida malumot beruvchi funksiya"""
#   print(f"Salom {name.title()}. Siz {2024-age}-yilda tug`ilgansiz")
#malumot_ber("sarvar", 23)

##2)Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
#def hisobla(number=float):
#  """Sonning kvadrati va kubini hisoblovchi funksiya"""
#  print(f"{number} sonining kvadrati: {number**2}\n"
#        f"Kubi esa: {number**3}")
#hisobla(3)

##3)Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
#def hisobla(number=int):
#  """Sonning juft yoki toqligini aniqlovchi funksiya"""
#  if number<=0:
#    qiymat = "toq ham emas juft ham emas"
#  elif number%2==0:
#    qiymat ="juft"
#  else:
#    qiymat = "toq"
#  print(f"Siz kiritgan son {qiymat}")
#hisobla(34)

##4)Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
#def kattasini_top(son1=float, son2=float):
#  """Katta sonni topuvchi funksiya"""
#  if son1>son2:
#    qiymat = son1
#  elif son1<son2:
#    qiymat = son2
 # else:
#    qiymat ="yo`q sonlar teng"
#  print(f"Sonlarning kattasi {qiymat} ")
#kattasini_top(90, 90)

##5)Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya yozing. Yuqoridagi funksiyada y uchun 2 standart qiymatini bering
#def daraja_top(x=float,y=2):
#  """x ning y chi darjasini hisoblovchi funksiya: y(defoult)=2"""
#  print(f"{x}^{y} darajasi: {x**y}")
#daraja_top(2,3)

##6)Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
#def qoldiqsiz_top(son=float):
#  """Sonni(2-10) gacha qoldiqsiz bo`linadiganlarini topish"""
#  for n in range(2,11):
#    if son%n==0:
#      print(f"{son}-soni quyidagi sonlarga qoldiqsiz bo`linadi:{n}")
#qoldiqsiz_top(91823396)