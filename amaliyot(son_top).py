import random as r

def kompyuter_topadi(x=10):
  """Odam o`ylaganini topadigan funksiya"""
  input(f"\n1 dan {x} gacha istalgan son o`ylang va istalgan tugmani bosing. Men topaman!!!")
  taxmin_com = 0
  min = 1
  max = x
  while True:
    taxmin_com +=1
    if min != max:
      i = r.randint(min,max)
    else:
      i = min
    javob = input(f"Siz o`ylagan son {i}: to`g'ri(t), bundan katta(+), bundan kichik(-): ".lower())
    if javob == '+':
      min = i+1
    elif javob == '-':
      max = i-1
    else:
      break
  print(f"Men {taxmin_com} ta taxmin bilan topdim")
  return taxmin_com

def men_topaman(x=10):
  """Kompyuter son o`ylaydigan funksiya"""
  print("Keling o`ylagan sonni topish o`ynaymiz")
  print(f"Men 1 dan {x} gacha son o`yladim. Topa olasizmi?:")
  son ='>>>'
  taxmin = 0
  a = r.randint(1,x)
  while True:
    mening_sonim = int(input(son))
    taxmin+=1
    if mening_sonim == a:
      break
    elif mening_sonim<a:
      print("Xato, men o`ylagan son bundan kattaroq, yana harakat qiling.")
    elif mening_sonim>a:
      print("Xato, men o`ylagan son bundan kichikroq, yana harakat qiling.")
  print(f"TOPDINGIZ! {a} sonini o`ylagan edim. {taxmin} ta taxmin bilan topdingiz. Tabriklayman!")
  return taxmin

def sorov(x=10):#javob ha\yo`q`
  yana = True
  while yana:
    men_taxmin = men_topaman(x)
    com_taxmin = kompyuter_topadi(x)
    if men_taxmin>com_taxmin:
      print(f"Men yutdim. Siz {men_taxmin} urinishda topdingiz")
    elif men_taxmin<com_taxmin:
      print(f"TABRIKLAYMAN!!! Siz yutdingiz. Siz {men_taxmin} urinishda topdingiz")
    else:
      print(f"Durrang ikkimiz ham {men_taxmin} urinishda topdik")
    yana = int(input("Yana o`ynaysizmi ha(1)/yo`q(0): "))

if __name__=="__main__":
  sorov()