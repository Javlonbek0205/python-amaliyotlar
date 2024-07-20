from uuid import uuid4

class Shaxs:
  def __init__(self, name, pasport, t_yil):
    self.name = name
    self.__pasport = pasport
    self.t_yil = t_yil
    self.age = 2024 - t_yil

  def get_info(self):
    javob = f"Ismi: {self.name}"
    javob +=f"\nPasport No_: {self.__pasport}"
    javob +=f"\nYoshi: {self.age}"
    return javob

class Talaba(Shaxs):
  talaba_soni = 0
  def __init__(self, name, pasport, t_yil):
    super().__init__(name, pasport, t_yil)
    self.__id_no = uuid4()
    self.fanlar = []
    Talaba.talaba_soni +=1

  @classmethod
  def get_num_talaba(cls):
    return cls.talaba_soni

  def get_id_no(self):
    return self.__id_no

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

talaba1 =Talaba('Salimjon Adhamov', 'AD1233245', 2001)
talaba2 = Talaba('Azimjon Holiqov', 'AB2398101', 1989)

print(Talaba.get_num_talaba())
print(talaba1.get_id_no())
talaba2.__pasport = 'AB122334'
print(talaba2.get_info())
