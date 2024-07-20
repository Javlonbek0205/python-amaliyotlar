#1)Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
"""mahsulotlar = []
print("Mahsulotlar ro`yxatini yaratamiz")
n=1
while True:
  savol = f"{n}-mahsulot nomini kiriting:"
  mahsulot = input(savol)
  mahsulotlar.append(mahsulot)
  javob = input("Yana mahsulot kiritasizmi(yes/no):")
  if javob == 'no':
    break
  else:
    n+=1
print(f"Tashrif uchun raxmat mahsulotlaringiz: {mahsulotlar}")"""

#2)e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
"""e_bozor = {}
stop = True
print("Bozorlik yaratamiz")
while stop:
  nom = input("Mahsulot nomini kiriting: ")
  narx = int(input("Mahsulot narxini kiriting: "))
  e_bozor[nom]=narx
  savol = input("Yana mahsulot kiritasizmi(yes/no): ")
  if savol == 'no':
    stop = False
for name, price in e_bozor.items():
print(f"Olinishi kerak bo`lgan narsalar:\n"
      f"{name.title()} ning narxi: {price}")"""

#3)Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
"""e_bozor = {'sabzi':4000,\
           'kartoshka':3000,\
            'piyoz':3000,\
              'bodring':5000,\
                'pomidor':8000,\
                  'guruch':20000,\
                    'go`sht':96000,\
                      'limon':50000,\
                        'ko`kat':2000}
buyurtmalar = []
n=1
print("Buyurtma qabul qiluvchi")
while True:
  savol = f"{n}-buyurtmani kiriting: "
  mahsulot = input(savol)
  if mahsulot in e_bozor:
    buyurtmalar.append(mahsulot)
    print(f"{mahsulot.title()}ning narxi: {e_bozor[mahsulot]}")
    javob = input("Yana mahsulot qo'shasizmi?(yes/no): ")
    if javob == 'no':
      break
    elif javob == 'yes':
      n+=1
    else:
      print("To`g`ri malumot kiriting!!!")
      n+=1
  elif mahsulot not in e_bozor:
    print("Bu mahsulot bizda mavjud emas!")
    javob = input("Yana mahsulot qo'shasizmi?(yes/no): ".title())
    if javob == 'no':
      break
    elif javob == 'yes':
      n+=1
    else:
      print("To`g`ri malumot kiriting!!!")
      n+=1
print(f"Bozorlik tayyor!!!")
for buyurtma in buyurtmalar:
  if buyurtma in e_bozor:
    print(f"{buyurtma} narxi: {e_bozor[buyurtma]}")"""