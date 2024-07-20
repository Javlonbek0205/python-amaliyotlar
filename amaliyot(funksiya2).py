#1)Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
#def malumot_ber(first_name, last_name, b_year:int, where, gmail=None, number=None):
#  """Foydalanuvchi malumotlarini olib dictionary qaytaruvchi funksiya"""
"""  malumotlarim = {"ism":first_name,\
                  'familya':last_name,\
                  't_yil':b_year,\
                    'yoshi':2024-b_year,\
                      'joylashuv':where,\
                        'email':gmail,\
                          'tel_nomer':number}
  return malumotlarim
people = []
print("Mijioz ma'lumotlarini kiriting:")
while True:
  ism = input("Ismi: ")
  familya = input("Familya: ")
  t_yil = int(input("Tug`ilgan yili: "))
  joylashuv = input("Yashash manzili: ")
  email = input("Gmail manzilini kiriting: ")
  t_nomer = input("Telefon nomerini kiriting: ")
  people.append(malumot_ber(ism, familya, t_yil, joylashuv, email, t_nomer ))
  javob = input("Davom etasizmi?(yes/no): ")
  if javob == 'no':
    break
print("\nMijoz ma'lumotlari tayyor")
for person in people:
  print(f"{person['ism'].title()} {person['familya'].title()}, {person['yoshi']} yoshda.\n"
        f"Gmail malumoti: {email}\n"
        f"Telefon nomeri: {t_nomer}")"""

#2)Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
#def kattani_top(son1,son2,son3):
#  """Sonlarning kattasini topuvhi funksiya"""
"""  if (son1>=son2 and son2>=son3) or (son1>=son3 and son3>=son2):
    kattasi = son1
  elif (son2>=son1 and son1>son3) or (son2>=son3 and son3>=son1):
    kattasi = son2
  elif (son3>=son1 and son1>=son2) or (son3>=son2 and son2>=son1):
    kattasi = son3
  return kattasi
print(kattani_top(0,2,2))
"""

#3)Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
#def aylana_yasa(radius:float, pi=3.14):
#  """Aylana radiusini olib uning parametrlarini chiqaruvchi funksiya"""
"""  aylana = {'radius':radius,\
            'diametri':radius*2,\
              'aylana_uzun':2*pi*radius,\
                'doira_yuzi':pi*radius**2}
  return aylana
r = float(input("Radiusni kiriting: "))
if r<0:
  print("\nBunday aylana mavjud emas!!!")
else:
  aylana1= aylana_yasa(r)
  print(f"\nAylana radiusi: {aylana1['radius']}\n"
        f"Aylana diametri: {aylana1['diametri']}\n"
        f"Aylana uzunligi: {aylana1['aylana_uzun']}\n"
        f"Doira yuzi:  {aylana1['doira_yuzi']}")"""

#4)Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
"""def tub_sonni_top(min,max):
  tub_sonlar = []
  for n in range(min, max+1):
    tub = True
    if n==1:
      tub = False
    elif n==2:
      tub = True

    else:
      for x in range(2,n):
        if n%x==0:
          tub = False
    if tub:
      tub_sonlar.append(n)
  return tub_sonlar
print(tub_sonni_top(3,30))"""

#5)Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing. Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
"""def fibonacci(n):
  sonlar = []
  for x in range(n):
    if x==0 or x==1:
      sonlar.append(1)
    else:
      sonlar.append(sonlar[x-1]+sonlar[x-2])
  return sonlar
print(fibonacci(10))"""