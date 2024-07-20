#1)random moduli <<randint(a,b)>>
"""import random as r # random modulini r deb chaqirayapmiz

son = r.randint(0,100) # 0 va 100 oralig'ida tasodifiy son
print(son)"""

#2)choice(x)
#x ning ichidan tasodifiy qiymatni qaytaruvchi funksiya. Bunda x bir necha elementdan iborat o'zgaruvchi (matn, ro'yxat) bo'lishi kerak.
"""import random as r
ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
print(ism)
print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz

x = list(range(0,51,5))
print(x)
print(r.choice(x))
"""
#3)<<shuffle(x)>>
#x ichidagi elementlarni tasodifiy tartibda qaytaruvchi funksiya. Bunda x bir necha elementdan iborat o'zgaruvchi (matn, ro'yxat) bo'lishi kerak.
"""x = list(range(11))
print(x)
r.shuffle(x)
print(x)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 10, 8, 7, 3, 5, 0, 6, 9, 4]"""