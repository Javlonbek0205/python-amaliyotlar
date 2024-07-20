#1)Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])
# Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
# Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida Fan klassiga tegishli obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.
# Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing. Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.
# Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, Foydalanuvchi, Sotuvchi, Mijoz va hokazo)
# Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.
# Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.
# Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun Foydalanuvchi klassidan Admin klassini yarating.
# Admin klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, ban_user() metodi konsolga "Foydalanuvchi bloklandi" degan matn chiqarsin.

#super class
class Shaxs:
  def __init__(self, name, pasport, t_yil):
    self.name = name
    self.pasport = pasport
    self.t_yil = t_yil
    self.age = 2024 - t_yil

  def get_info(self):
    javob = f"Ismi: {self.name}"
    javob +=f"\nPasport No_: {self.pasport}"
    javob +=f"\nYoshi: {self.age}"
    return javob

#talaba class
class Talaba(Shaxs):
  def __init__(self, name, pasport, t_yil, id_no):
    super().__init__(name, pasport, t_yil)
    self.id_no = id_no
    self.fanlar = []

  def add_fan(self, fan):
    self.fanlar.append(fan)
    fan.add_talaba()

  def get_fanlar(self):
    return f"Qatnashadigan kurslari: {[fan.get_fan() for fan in self.fanlar]}"

  def remove_fan(self, fan):
    if fan in self.fanlar:
      self.fanlar.remove(fan)
      fan.remove_talaba()
    else:
      print(f"Siz bu fanga yozilmagansiz")
#fan class
class Fan:
  def __init__(self, fan_nomi):
    self.fan_nomi = fan_nomi
    self.talaba = 0

  def get_fan(self):
    return self.fan_nomi

  def add_talaba(self):
    self.talaba +=1

  def remove_talaba(self):
    self.talaba -=1

  def get_info_soni(self):
    return f"{self.fan_nomi}: {self.talaba}"

talaba1 = Talaba('Salimjon Abdurahimov', 'AD1234567', 2002, '0000123')

#fan1 = Fan('Matematika')
#fan2 = Fan('English')
#fan3 = Fan('Fizika')
#talaba1.add_fan(fan2)
#talaba1.add_fan(fan3)

#print(fan2.get_info_soni())
#print(talaba1.get_fanlar())
#print(talaba1.get_info())

#user class
class User(Shaxs):
  def __init__(self, name, pasport, t_yil, email, tel_nomer):
    super().__init__(name, pasport, t_yil)
    self.email = email
    self.tel_nomer = tel_nomer

  def get_info(self):
    return f"{super().get_info()}\nEmail: {self.email}\nTelefon nomer: {self.tel_nomer}"

  def get_email(self):
    return self.email

  def get_tel_nomer(self):
    return self.tel_nomer

user1 = User('Salimjon Abdurahimov', 'AD1234567', 2002, 'salimjondeveloper@gmail.com', '902098908' )

#print(user1.get_info())

#admin class\\
class Admin(Shaxs):
  def __init__(self, name, pasport, t_yil, login):
    super().__init__(name, pasport, t_yil)
    self.login = login
    self.admin_no = 0
  def get_info(self):
    return f"{super().get_info()}\nLogin: {self.login}"
  def set_admin(self):
    self.admin_no += 1

  def get_admin_soni(self):
    return f"Admin soni: {self.admin_no}"

admin1 = Admin('Diyorbek Jalolov', 'AF1234567', 2000, "diyor001admin")
admin1.set_admin()
print(admin1.get_admin_soni())
print(admin1.get_info())
