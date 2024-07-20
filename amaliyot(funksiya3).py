#1)Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.
"""def kattalashtir(matnlar):
  for matn in range(len(matnlar)):
    matnlar[matn] = matnlar[matn].capitalize()

matn1 = ['salom', 'hayr', 'salim', 'toshmat', 'husan']
kattalashtir(matn1)
print(matn1)"""

#2)Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring
"""def kattalashtir(matnlar):
  matnlar = matnlar[:]
  for matn in range(len(matnlar)):
    matnlar[matn] = matnlar[matn].capitalize()
  return matnlar

matn1 = ['salom', 'hayr', 'salim', 'toshmat', 'husan']
yangi_matn = kattalashtir(matn1)
print(yangi_matn)"""

#3)Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.
"""def bahola(ismlar):
    baholar = {}
    name = ismlar[:]
    for ism in range(len(name)):
        baho = input(f"Talaba {name[ism].title()}ning bahosini kiriting: ")
        baholar[name[ism]]=baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
print(talabalar)"""