#dars1 = 'read_write_file.txt'
#open1 = 'open(file_name) operatori yordamida fayllar ochiladi va close(file_name) yordamida yopiladi'
#open2 = 'with open(file_name) as file->yordamida fileni ochib birdaniga yopish mumkin. O`qish uchun ochiladi'
#write1 = "with open(file_name, 'w') as file-> yordamida fileni yangi yaratadi eskisini o`chiradi va yozadi"
#write2 = "with open(file_name, 'a')as file-> yordamida mavjud faylga malumot yozadi yo`q bo`lsa yangi yaratadi"
#with open(dars1, 'w') as file:
#  file.write(open1+'\n')
#  file.write(open2+'\n')
#  file.write(write1+'\n')
#  file.write(write2+'\n')
#write3 = "pickle moduli yordamida biz o`zgaruvchilarni fayllarga yozishimiz mumkin"
#write4 = "import pickle> with open(o`zgaruvchi_file.pkl, 'wb') as file> picle.dump(ozgaruvchi, file)--> yoziladi"
#with open(dars1, 'a') as file:
#  file.write(write3+'\n')
#  file.write(write4+'\n')

#dars2 = 'read_write_file.txt'
#with open(dars2) as file:
#  dars = file.read()
#print(dars)
pay = 'pi_million_digits (1).txt'
with open(pay) as file:
    pi = file.read()
text = pi
def t_yil_top():
  t_kun = input("Tug'ilgan kunni kiriting: ")
  t_oy = input("Tug'ilgan oyni kiriting: ")
  t_yil = input("Tug'ilgan yilni kiriting: ")
  andoza = f"{t_kun}{t_oy}{t_yil}"
  print(andoza)
  if andoza in text:
    print("Bu sonlar pi tarkibida bor")
  else:
    print("Bu raqamlar pi tarkibida yo`q")

t_yil_top()
