katalog = [ 
    {'nama': 'Belajar Python',  'harga': 75000, 'stok': 5}, 
    {'nama': 'Struktur Data',   'harga': 95000, 'stok': 3}, 
    {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}, 
]

def cari_buku(katalog, keyword):
    data_buku = []
    for buku in katalog:
        for key,value in buku.items():
            if key == "nama":
                if keyword.lower() in value.lower():
                    data_buku.append(buku)
    if data_buku == []:
        print("Buku tidak ditemukan.")
    return data_buku

keyword = input("Masukkan keyword buku yang ingin dicari : ")
print("Buku yang ditemukan adalah : ")
buku = cari_buku(katalog, keyword)
print(buku)