#1)Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
"""kitoblar = []
kitob = "(Dasturni to`xtatmoqchi bo`lsangiz'stop' so`zini kiriting)"
kitob += "Yaxshi ko`rgan kitobingizni kiriting:"
while True:
  qiymat = input(kitob)
  if qiymat.lower()=='stop':
    break
  else:
    kitoblar.append(qiymat)
print(f"Raxmat siz yoqtirgan kitoblar: {kitoblar}")"""

#2)Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)
"""yosh = "(Dasturni to`xtatish uchun 'stop' yoki 'quite' deb yozing)"
yosh += "Yoshingizni kiriting: "


while True:
  qiymat=input(yosh)
  if qiymat == 'stop' or qiymat=='quite':
    break
  else:
    if int(qiymat)<=7:
      narx=2000
    elif int(qiymat) >7 and int(qiymat)<=18:
      narx=3000
    elif int(qiymat) >18 and int(qiymat)<=65:
      narx=10000
    elif int(qiymat)>65:
      narx='bepul'
  print(f"Siz uchun kirish: {narx}")
print("Tashrifingizdan hursandmiz")"""

#3)Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?
"""savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='Exit':
        break

    if float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")"""
