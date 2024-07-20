#1)O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring Ro'yxatning uzunligini konsolga chiqaring
#davlatlar =['O`zbekiston', 'Amerika', 'Rossiya', 'Germaniya', 'Shvetsariya']
#print(len(davlatlar))

#2)sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
#print(sorted(davlatlar))

#3)sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
#print(sorted(davlatlar, reverse=True))

#4)Asl ro'yxatni qaytadan konsolga chiqaring
#print(davlatlar)

#5)reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
#davlatlar.reverse()
#print(davlatlar)

#6)sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring
#davlatlar.sort()
#print(davlatlar)
#davlatlar.sort(reverse=True)
#print(davlatlar)

#7)120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
#son = list(range(120,1200))
#print(son)

#8)Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
#print(sum(son))

#9)Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
#print(max(son)-min(son))

#10)Ro'yxatdagi elementlar sonini hisoblang
#print(len(son))

#11)Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
#print([son[:20]], [son[540:560]], [son[1060:]])

#12)taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
#taomlar = ['osh', 'shashlik', 'tuxum', 'achchiqgo`sht', 'pirok']
#nonushta = taomlar[:]
#nonushta.remove('osh')
#nonushta.remove('shashlik')
#nonushta.remove('achchiqgo`sht')
#nonushta.append('saryoq')
#nonushta.append('limon choy')
#print(nonushta)
#print(taomlar)

#13)Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring
#nonushta = tuple(nonushta)
#taomlar = tuple(taomlar)
#print(nonushta)
#print(taomlar)