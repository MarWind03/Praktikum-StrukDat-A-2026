x = 1       # integer untuk bilangan bulat
y = 0.1e1   # float untuk bilangan desimal
z = -1j     # complex untuk bilangan imajiner

# konversi dari integer ke float menggunakan casting
a = float(x) # a akan bernilai 1.0

# konversi dari float ke integer menggunakan casting
b = int(y) #b akan bernilai 1

# konversi dari integer ke complex menggunakan casting
c = complex(x) #c akan bernilai 1+0j

print(a)
print(b)
print(c)

# kita bisa mencetak tipe data variabel
print(type(a)) # float
print(type(b)) # integer
print(type(c)) # complex