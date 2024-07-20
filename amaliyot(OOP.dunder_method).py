class Shaxs:
  def __init__(self, name, pasport, t_yil):
    self.name = name
    self.pasport = pasport
    self.t_yil = t_yil
    self.age = 2024 - t_yil

  def __repr__(self):
    javob = f"Ismi: {self.name}"
    return javob

#talaba class
class Talaba(Shaxs):
  def __init__(self, name, pasport, t_yil, id_no):
    super().__init__(name, pasport, t_yil)
    self.id_no = id_no
    self.fanlar = []

  def add_fan(self, fan):
    if isinstance(fan, Fan):
      self.fanlar.append(fan)
      fan.add_talaba(self)
    else:
      print("Siz fan kiritmayapsiz!!!")

  def __len__(self):
    print(f"{self.name} kurslar soni:")
    return len(self.fanlar)


  def get_fanlar(self):
    return f"{self.name} kurslari: {[fan.get_fan() for fan in self.fanlar]}"

  def remove_fan(self, fan):
    if fan in self.fanlar:
      self.fanlar.remove(fan)
      fan.remove_talaba(self)
    else:
      print(f"Siz bu fanga yozilmagansiz")
#fan class
class Fan:
  def __init__(self, fan_nomi):
    self.fan_nomi = fan_nomi
    self.talaba_soni = 0
    self.fan_students = []

  def get_fan(self):
    return self.fan_nomi

  def get_students(self):
    return f"{self.fan_nomi} qatnashuvchilar: {[talaba.__repr__() for talaba in self.fan_students]}"

  def add_talaba(self, talaba):
    if isinstance(talaba, Talaba):
      self.fan_students.append(talaba)
      self.talaba_soni +=1

    else:
      print("Talaba kiriting!!!")

  def remove_talaba(self, talaba):
    if isinstance(talaba, Talaba):
      self.fan_students.remove(talaba)
      self.talaba_soni -= 1

    else:
      print("Iltimos talaba kiriting")

  def get_talaba_num(self):
    return f"{self.fan_nomi}: {self.talaba_soni}"

talaba1 = Talaba('Salimjon Abdurahimov', 'AD1234567', 2002, '0000123')
talaba2 = Talaba('Hasan Husanov', 'AD1234567', 2009, '00001275')

fan1 = Fan('Matematika')
fan2 = Fan('English')
fan3 = Fan('Fizika')
talaba2.add_fan(fan2)
for fan in  [fan1, fan2, fan3]:
  talaba1.add_fan(fan)

talaba1.remove_fan(fan1)
print(fan2.get_talaba_num())
print(talaba1.get_fanlar())
print(fan1.get_students())
print(fan2.get_students())
print(len(talaba2))
print(len(talaba1))

#user class
"""class User(Shaxs):
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
    return f"Admin soni: {self.admin_no}

admin1 = Admin('Diyorbek Jalolov', 'AF1234567', 2000, "diyor001admin")
admin1.set_admin()
print(admin1.get_admin_soni())
print(admin1.get_info())"""