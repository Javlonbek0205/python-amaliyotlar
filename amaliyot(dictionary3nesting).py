#1)Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring
"""person_1 = {'ism':'Sharif Abdullayev',
            'kasbi':'Repper',
            'malumoti':'o`rta'
            }
person_2 = {'ism':'Mirshakar Fayzullayev',
            'kasbi':'Stand up comik',
            'malumoti':'oliy'
            }
person_3 = {'ism':'Anvar Narzullayev',
            'kasbi':'Seniour developer',
            'malumoti':'olim'
            }
person_4 = {'ism':'Javlonbek Maxmudov',
            'kasbi':'Junior developer',
            'malumoti':'o`rta'
            }
people = [person_1, person_2, person_3, person_4]
for person in people:
  print(f"{person['ism']} ning kasbi "
        f"{person['kasbi']} ma'lumoti esa "
        f"{person['malumoti']}")"""

#2)Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring
"""person_1 = {'ism':'Sharif Abdullayev',
            'kasbi':'Repper',
            'malumoti':'o`rta',
            'proyekt': ["Gulim treki", "Sog`indim treki", 'O`zbekistonlik treki']
            }
person_2 = {'ism':'Mirshakar Fayzullayev',
            'kasbi':'Stand up comik',
            'malumoti':'oliy',
            'proyekt': ["Sahna stand up asoschisi", "Tungi qahramon boshlovchisi"]
            }
person_3 = {'ism':'Anvar Narzullayev',
            'kasbi':'Seniour developer',
            'malumoti':'olim',
            'proyekt': ["Mohirdev asoschisi", "MohirAI asoschisi"]
            }
person_4 = {'ism':'Javlonbek Maxmudov',
            'kasbi':'Junior developer',
            'malumoti':'o`rta',
            'proyekt':['My blog sayt asoschisi']
            }
people = [person_1, person_2, person_3, person_4]
for person in people:
  print(f"{person['ism']} quyidagi proyektlari bor:")
  for project in person['proyekt']:
    print(f"{project.title()}")"""

#3)Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang. Natijani konsolga chiqaring.
"""stop_loop =False
friends = {'ali':[],
           'vali':[],
           'hasan':[]}
ism = input("Salom foydalanuvchi ismingizni kiriting:").lower()

if ism in friends:
  for n in range(3):
    kino = input(f"Xush kelibsiz {ism.title()} "
                  f"{n+1}-yoqtirgan kinolaringizni kiriting:")
    friends[ism].append(kino)
    print(friends[ism])
else:
  print("Siz foydalanuvchi emassiz")"""

#4)Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.
"""davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }
for davlat, info in davlatlar.items():
  print(f"\n{davlat.title()} davlatining poytaxti:{info['poytaxt']}"
        f"\nMaydoni: {info['maydon']}"
        f"\nAholi soni: {info['aholi']}"
        f"\nPul birligi: {info['pul birligi']}")
"""

#5)Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
"""davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }
city = input("Qaysi davlat haqida bilmoqchisiz?>>>").lower()
if city in davlatlar:
  info = davlatlar[city]
  print(f"\n{city.title()} davlatining poytaxti: {info['poytaxt'].title()}"
        f"\nMaydoni: {info['maydon']}"
        f"\nAholi soni: {info['aholi']}"
        f"\nPul birligi: {info['pul birligi']}")
else:
  print(f"Kechirasiz bizda {city.title()} davlati haqida ma`lumot topilmadi")"""