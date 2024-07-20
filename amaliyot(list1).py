#1)ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting.Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
#dost = ['Husniddin', 'Asror', 'Alisher']
#print("Salom "+dost[1]+", bugun darslaring bormi?\n"+dost[2]+", darsga #boramizmi? ")

#2)sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
#sonlar = [1, 2, 3, 0.02, -10.2]
#print(sonlar[1]+sonlar[3])
#sonlar[2]=12
#sonlar.append(sonlar[4]+2)
#print(sonlar)

#3)t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
#t_shaxslar = ["Alisher Navoiy", "Amir Temur", "Imom al Buxoriy", "Albert Enshteyn,"]
#z_shaxslar = [ "Elon Musk", "Bill Gates"]
#print("Men tarixiy shaxslardan ",t_shaxslar.pop(2)," bilan,\nzamonaviy shaxslardan ",z_shaxslar.pop(0)," bilan #ko`rishgan bo`lar edim")

#4)friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
#friends = []
#friends.append('sarvarbek'.title())
#friends.append('Asrorbek'.title())
#friends.append('ahrorbek'.title())
#friends.append('husniddin'.title())
#friends.append('fazliddin'.title())
#print(friends)

#5)Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
#friends.remove("Sarvarbek")
#friends.remove("Ahrorbek")
#print(friends)

#5)Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
#friends.insert(2,'Azimjon')
#friends.insert(0,'Alisher')
#friends.insert(4,'Kozimjon')
#print(friends)

#6)Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
#mehmonlar =[]
#mehmonlar.append(friends.pop(1))
#mehmonlar.append(friends.pop(4))
#print(mehmonlar)