#1)Kodni tahlil qilamiz, 1-qatorda math modulini chaqirib oldik. 2-qatorda lambda funksiyani yaratdik, funksiyamiz pi va r argumentlarini qabul qilib, 2*pi*r qiymatni qaytaradi. Funksiyaga nom bermadik, lekin unga uzunlik identifikatori orqali murojat qilishimiz mumkin. 3-qatorda funksiyamizga murojat qildik va natijani konsolga chiqardik.
"""import math
uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi,10))"""

#2)Quyidagi dasturda biz avval daraja degan funksiya yasadik, bu funskiyamiz n degan o'zgaruvchi qabul qilib oladi va funksiya ichidagi noma'lum x ning n-darajasini qaytaradi. Aslida darajabu funksiya yasaydigan funksya bo'ldi. Xo'sh, undan qanday foydalanamiz? 4-5-qatorlarda esa daraja funksiyasidan yana 2 ta funksiya yasadik: kvadrat - kiritilgan sonning kvadratini hisoblaydi, kub - kiritilgan sonning kubini hisoblaydi.
"""def daraja(n):
    return lambda x : x**n

kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")"""

#3)Quyidagi dastur mevalar ro'yxatidan b harfiga boshlanuvchi mevalarni ajratib oladi. Bu yerda biz matnlarga tegishli bo'lgan .startswith() metodidan foydalandik. Bu metod, berilgan matn shu harfdan boshlanadimi yoki yo'q tekshiradi va True yoki False qiymat qaytaradi.
"""mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))
print(mevalar_b)"""

#4)Quyidagi dastur esa mevalar ro'yxatidan nomi 5 yoki undan kam harfdan iborat mevalarni saralab oladi
"""mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
print(mevalar2)"""

#5)
"""import random as r
sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
juft_sonlar = list(filter(lambda son: son%2==0,sonlar))

print(sonlar)
print(juft_sonlar)"""