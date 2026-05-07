plat = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]

def pisah_plat(list_plat):
    ganjil = []
    genap = []
    for s in list_plat:
        a , b , c = s.split()
        b = int(b)
        if b % 2 == 1:
            ganjil.append(s)
        else:
            genap.append(s)
    return (ganjil , genap)

tuple_plat = pisah_plat(plat)
list_ganjil , list_genap = tuple_plat
print(list_ganjil)
print(list_genap)