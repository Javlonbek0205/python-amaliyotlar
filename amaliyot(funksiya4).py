#1)Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
"""def kopaytir(*sonlar):
  kopaytma=1
  for son in sonlar:
    kopaytma *= son
  return kopaytma
sonlar = kopaytir(1,2,3,5,6,8)
print(sonlar)"""

#2)Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.
"""def talaba_yarat(ism, familya, **malumotlar):
  malumotlar['ism']=ism
  malumotlar['familya']=familya
  return malumotlar
talaba1 = talaba_yarat('Javlonbek', 'Maxmudov', tel_raqam=902098908, manzil='Eskihaqqulobod')
print(talaba1)"""
