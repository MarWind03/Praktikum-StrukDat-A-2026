def tampilkan_menu():
    print("=== PyBook Store ===")
    print("1. Tambah Buku")
    print("2. Tampilkan Semua Buku")
    print("3. Beli Buku")
    print("4. Laporan Penjualan")
    print("5. Keluar")

def tambah_buku(nama, harga, stok):
    if harga <= 0:
        print(f"[ERROR] Harga harus lebih besar dari nol!")
        return None
    elif stok < 0:
        print(f"[ERROR] Stok tidak boleh bernilai negatif!")
        return None

    return {"nama" : nama, "harga":harga, "stok":stok}

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
            log_transaksi.append((data_buku[0], jumlah_beli, data_buku[1]*jumlah_beli))
            data_buku[2] -= jumlah_beli
            print(f"Total harga yang harus dibayar adalah : {data_buku[1]*jumlah_beli}")
        
        if ada and not cukup:
            print("[ERROR] Stok Buku tidak Cukup!")
        if ada == True:
            ketemu = ada
            
    if ketemu == False:
        print("[ERROR] Buku tidak ditemukan!")


katalog = []
log_transaksi = []

while True:
    tampilkan_menu()
    pilihan = int(input("Masukkan Pilihan Anda : "))
    if(pilihan == 1):
        nama = input("Masukkan Nama Buku : ")
        harga = float(input("Masukkan Harga Buku : "))
        stok = int(input("Masukkan Stok Buku : "))

        buku = tambah_buku(nama, harga, stok)
        if buku == None:
            continue
        else:
            print("Buku berhasil ditambahkan!")
            katalog.append(buku)

    elif(pilihan == 2):
        print("Daftar Buku Yang Tersedia :")
        for buku in katalog:
            print(buku)

    elif(pilihan == 3):
        nama = input("Masukkan nama buku : ")
        jumlah = int(input("Masukkan Jumlah beli : "))
        proses_transaksi(katalog, nama, jumlah)

    elif(pilihan == 4):
        total_pemasukan = 0
        nama_buku = []
        for transaksi in log_transaksi:
            nama, jumlah , total = transaksi
            nama_buku.append(nama)
            total_pemasukan += total
        nama_buku = set(nama_buku)
        frekuensi = {"tes" : "gaada"}
        for i in nama_buku:
            frekuensi[i] = 0
        for transaksi in log_transaksi:
            nama, jumlah , total = transaksi
            frekuensi[nama] += jumlah
        maks = -1
        buku = "gaada"
        for x,y in frekuensi.items():
            if x != "tes":
                if(y > maks):
                    maks = y
                    buku = x
        print(f"Total Pemasukan adalah : {total_pemasukan}")
        print(f"Buku Terlaris adalah : {buku}")
            


    elif(pilihan == 5):
        print("Terima kasih sudah berbelanja!")
        break
    print()