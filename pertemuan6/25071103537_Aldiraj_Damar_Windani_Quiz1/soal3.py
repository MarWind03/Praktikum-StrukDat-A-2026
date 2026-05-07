katalog = [ 
    {'nama': 'Belajar Python',  'harga': 75000, 'stok': 5}, 
    {'nama': 'Struktur Data',   'harga': 95000, 'stok': 3}, 
    {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}, 
]
riwayat_transaksi = []

def proses_transaksi(katalog, nama_buku, jumlah_beli):
    ketemu = False
    for buku in katalog:
        ada = False
        cukup = False
        data_buku = []
        for key, value in buku.items():
            data_buku.append(value)

        if data_buku[0].lower() == nama_buku.lower():
            ada = True
        if data_buku[2] >= jumlah_beli:
            cukup = True

        if cukup and ada:
            data_buku[2] -= jumlah_beli
            riwayat_transaksi.append(data_buku[0])
            print(f"Total harga yang harus dibayar adalah : {data_buku[1]*jumlah_beli}")
        
        if ada and not cukup:
            print("[ERROR] Stok Buku tidak Cukup!")
        if ada == True:
            ketemu = ada
            
    if ketemu == False:
        print("[ERROR] Buku tidak ditemukan!")

for i in range(3):
    nama = input("Masukkan nama buku : ")
    jumlah = int(input("Masukkan Jumlah beli : "))
    proses_transaksi(katalog, nama, jumlah)

riwayat_transaksi = set(riwayat_transaksi)
print("Buku yang pernah dibeli adalah : ")
print(riwayat_transaksi)




    


        
            

