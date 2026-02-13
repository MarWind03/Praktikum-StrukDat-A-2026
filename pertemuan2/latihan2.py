# NO 1
nilai = [75, 80, 65, 90, 85]
nilai.append(95)
nilai.remove(min(nilai))
nilai.sort()
jumlah = sum(nilai)

print(max(nilai), min(nilai) , jumlah)
print(jumlah / len(nilai))
print(nilai , '\n')

# NO 2
dosen = ("D001", "Dr. Andi", "Struktur Data", 12)
print(dosen[1] , dosen[2])
for i in dosen:
    print(i , end = " ")
print("\n")
listdosen = list(dosen)
listdosen.pop(3)
listdosen.append(14)
dosen = tuple(listdosen)
# karena dosen bertipe tuple, dan tuple itu unchangeable maka dikonversi ke list dulu
# baru ipk baru di append ke list
# setelah itu baru dikonversi kembali dari list ke tuple

# kelebihan tuple adalah unchangable

# NO 3
keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}

print(keahlian_A & keahlian_B)
print(keahlian_A - keahlian_B)
print(keahlian_A ^ keahlian_B)
if "Java" not in keahlian_B:
    print("Tidak ada")
else: print("Ada")
print("")

# NO 4
mahasiswa = {
"M001": {"nama": "Rina", "prodi": "Informatika", "ipk":
3.60},
"M002": {"nama": "Doni", "prodi": "Sistem Informasi",
"ipk": 3.25},
"M003": {"nama": "Lina", "prodi": "Informatika", "ipk":
3.80}
}
print("Nama Mahasiswa dengan IPK >= 3.5 adalah : ", end = "")
sum = 0
for x,y in mahasiswa.items():
    for z in y:
        if z == "ipk":
            sum += y[z]
            if y[z] >= 3.5:
                print(y["nama"] , end = " ")
print("")
print(f"Rata-rata IPK mahasiswa adalah : {sum/3}")

mahasiswa["M004"] = {
    "nama" : "Damar",
    "prodi" : "Teknik Informatika",
    "ipk" : 3.99
}

for x, y in mahasiswa.items():
    print(x , y)