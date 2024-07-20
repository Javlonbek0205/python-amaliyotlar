#1)Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)
#Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).
#Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.
"""class User:
  def __init__(self, name, last_name, email, b_year):
    self.name = name
    self.last_name = last_name
    self.email = email
    self.b_year = b_year

  def get_info(self, yil=2024):
    return f"Foydalanuvchi ism familyasi: {self.name} {self.last_name}\nGmail: {self.email}\nYoshi: {yil - self.b_year}"
  def get_fullname(self):
    return f"{self.name} {self.last_name}"
  def get_email(self):
    return self.email
  def get_age(self,yil=2024):
    return yil-self.b_year
user1 = User('Javlonbek', 'Maxmudov', 'javlonbekdeveloper7@gmail.com', 2005)
user2 = User('Salimjon', 'Abdurahimov', 'salimjon005@gmail.com', 2000)
print(user1.get_email())
print(user2.get_age(), user2.get_fullname())
print(user1.get_info())
print(user2.get_info())"""

#2)Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)

#Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing

#get_info() metodi avti haqida to'liq ma'lumotni matn ko'rinishida qaytarsin

#Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.

#update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin

#Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)

#Avtosalonga yangi avtomobillar qo'shish uchun metod yozing

#Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing

#Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring

#dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi turli klass va obyektlarning xususiyatlari va metodlarini toping (dir(str), dir(int) va hokazo)

"""class Avto:
  def __init__(self, model, rang, karobka, narh):
    self.km = 0
    self.model = model
    self.rang = rang
    self.karobka = karobka
    self.narh = narh
  def get_info(self):
    return f"Mashina modeli: {self.model}\nRangi: {self.rang}\nKarobka: {self.karobka}\nNarh: {self.narh}$\nYurgan masofa: {self.km}km"

  def get_shirt_info(self):
    return f"Mashina modeli: {self.model}, Narh: {self.narh}$ "

  def get_model(self):
    return self.model

  def get_color(self):
    return self.rang

  def get_price(self):
    return self.narh

  def set_color(self, new_color):
    self.rang = new_color

  def set_price(self, new_price:int):
    self.narh = new_price

  def update_km(self):
    self.km +=10

avto1 = Avto('BMW(3010)', 'Red', 'avtomat', 320000)
avto2 = Avto('BMW(LC20)', 'Black', 'avtomat', 258000)"""


#avto1.update_km()
#avto1.set_color('white')
#print(avto1.get_info())
#print(avto1.get_color())

"""class Yangi_avtosalon:
  def __init__(self, salon_nomi, manzili):
    self.salon_nomi = salon_nomi
    self.manzili = manzili
    self.sotuvdagi_avtolar = []
    self.avto_soni = 0

  def add_avto(self,avto):
    self.sotuvdagi_avtolar.append(avto)
    self.avto_soni+=1

  def get_salon_name(self):
    return self.salon_nomi

  def get_manzil(self):
    return self.manzili

  def get_avtolar(self):
    return [avto.get_shirt_info() for avto in self.sotuvdagi_avtolar]

salon1 = Yangi_avtosalon('Speed is life', 'Andijon')"""

#salon1.add_avto(avto1)
#salon1.add_avto(avto2)
#speed_salon = salon1.get_avtolar()
#print(speed_salon)


"""def see_methods(klass):#  Klass va obyektlarning methodlarini qaytaruvchi funksiya#

  return [method for method in dir(klass) if method.startswith('__') is False]
print(see_methods(avto1))

print(see_methods(salon1))"""

#print(dir(Avto))
#print(salon1.__dict__)