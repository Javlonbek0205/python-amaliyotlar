def kattasi_top(x, y, z):
    if (x >= y and x >= z):
        return x
    elif (y >= x and y >= z):
        return y
    else:
        return z

def juft_top(qiymatlar:list):
    son = []
    for qiymat in qiymatlar:
        if qiymat<0:
            continue
        elif qiymat % 2 != 0:
            continue
        else:
           son.append(qiymat)
    return son
def matn_katta_qil(matn:list):
    new_matn = []
    for word in matn:
        if isinstance(word, int):
            new_matn.append(word)
        elif isinstance(word, float):
            new_matn.append(word)
        else:
            new_matn.append(word.capitalize())
    return new_matn
