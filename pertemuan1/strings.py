print("Halo Dunia!")
print("Ini Contoh Output.")

print("Bisa Petik Dua")
print('Petik Satu Juga Bisa!')

# Multiline string bisa menggunakan ('') atau (""") tiga kali
a = """Ini Contoh String Multiline
Ini Contoh String Multiline
Ini Contoh String Multiline
Ini Contoh String Multiline
"""
print(a)

# Slicing string (memotong)
a = "Haloo, Duniaa!!"
print(a[1:5]) # akan mencetak string a dari indeks 1 sampai 4 (aloo)
print(a[:3])  # akan mencetak string a dari awal sampai indeks 2 (Hal)
print(a[10:]) # akan mencetak string a dari 10 sampai akhir (iaa!!)
print(a[:-1]) # akan mencetak string a dari awal sampai indeks -1 (Haloo, Duniaa!)

# Uppercase (Kapital) dan Lowercase (Kapitil)
a = "HaLo, DUnia!"
print(a.upper()) # akan mencetak "HALO, DUNIA!"
print(a.lower()) # akan mencetak "halo, dunia!"

# Menghapus Whitespace (spasi dan tab) dari string
a = "       Haloo, Duniaa!!        "
print(a.strip()) # akan mencetak "Haloo, Duniaa!!"

# Mengganti (replace)
a = "Haloo, Duniaa!!"
print(a.replace("oo" , "ah")) # akan mencetak "Halah, Duniaa!!"

# Memisah (split)
a = "Halo Dunia !!!"
print(a.split(' ')) # akan mencetak list kata yang dipisahkan oleh ' '
#['Halo', 'Dunia', '!!!']

# Penyambungan string (+)
a = "Halo, "
b = "Dunia!!"
c = a + b
print(c) # akan mencetak "Halo, Dunia!!"

# Perkalian string (*)
a = "wk"
print(a*3) # akan mencetak "wkwkwk"