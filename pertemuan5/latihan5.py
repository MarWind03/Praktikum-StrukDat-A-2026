# NO 1
stok_barang = [15, 40, 30, 10, 25]
stok_barang[stok_barang.index(10)] = 50
print(stok_barang)

stok_barang.append(5)
print(stok_barang)

stok_barang.sort(reverse=True)
print(stok_barang)

print(sum(stok_barang))
print("Stok Aman" if sum(stok_barang)/len(stok_barang) > 20 else "Waspada")

# NO 2
data_aktivitas = [("Diki",88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
for x in data_aktivitas:
    a , b = x
    if b > 80:
        print(f"{a} mendapatkan predikat Gold")
    elif b > 49:
        print(f"{a} mendapatkan predikat Silver")
    else:
        print(f"{a} mendapatkan predikat Bronze")

# NO 3
ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}
print("Mahasiswa yang di ukm coding saja : ", ukm_coding - ukm_robotik)
print("Mahasiswa unik yang mendaftar di salah satu atau kedua ukm: ", ukm_coding | ukm_robotik)
print("Apakah Andi anggota ukm robotik? : ", "Andi" in ukm_robotik)

# NO 4
gudang_pc = [
    {"item": "Monitor", "harga": 1500000, "stok": 5},
    {"item": "Keyboard", "harga": 400000, "stok": 12},
    {"item": "Mouse", "harga": 250000, "stok": 20}
]

for x in gudang_pc:
    for a , b in x.items():
        if b == "Keyboard":
            x["kategori"] = "Aksesoris"
            break

gudang_pc.append({"item": "Headset", "harga": 350000, "stok" : 8})      

# print(gudang_pc)

for x in gudang_pc:
    print(f"Item: {x["item"]} | Total Aset: Rp {x["harga"]*x["stok"]}")
