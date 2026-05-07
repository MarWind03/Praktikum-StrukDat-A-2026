def tambah_buku(nama, harga, stok):
    if harga <= 0:
        print(f"[ERROR] Harga harus lebih besar dari nol!")
        return None
    elif stok < 0:
        print(f"[ERROR] Stok tidak boleh bernilai negatif!")
        return None

    return {"nama" : nama, "harga":harga, "stok":stok}

data_buku = []
for i in range(3):
    print(f"Masukkan Data Buku ke-{i+1}")
    nama = input("Masukkan Nama Buku : ")
    harga = float(input("Masukkan Harga Buku : "))
    stok = int(input("Masukkan Stok Buku : "))
    data_buku.append([nama , harga , stok])

print(data_buku)
print("Buku yang berhasil ditambahkan : ")
for nama, harga, stok in data_buku:
    buku = tambah_buku(nama, harga, stok)
    if buku == None:
        continue
    print(buku)
