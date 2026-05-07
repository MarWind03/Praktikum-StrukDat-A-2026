pengunjung_hari_ini = [
 {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi",
"kembali": False},
 {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",
"kembali": True},
 {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi",
"kembali": False},
 {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",
"kembali": True},
 {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains",
"kembali": False},
 {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum",
"kembali": False},
]

info_perpus = ("Perpustakaan Kampus Terpadu" , 
               "Jl. Pendidikan No. 5, Pekanbaru",
               "0761-54321")

# SOAL 1
def tampilkan_pengunjung():
    print("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print(f"{'No':<3} | {'ID':<4} | {'Nama':<7} | {'Usia':<4} | {'Kategori':<8} | {'Status Kembali':<14}")
    print('-' * 55)
    for i in range(len(pengunjung_hari_ini)):
        dict = pengunjung_hari_ini[i]
        kode = dict['id']
        nama = dict['nama']
        umur = dict['usia']
        kategori = dict['kategori']
        kembali = "Sudah Kembali" if dict['kembali'] else "Belum Kembali"
        print(f"{i+1:<3} | {kode:<4} | {nama:<7} | {umur:<4} | {kategori:<8} | {kembali:<14}")
    print()

def filter_belum_kembali():
    list = [dict['nama'] for dict in pengunjung_hari_ini if not dict['kembali']]
    list.sort()
    print("===== PENGUNJUNG BELUM KEMBALI =====")
    for i in range(len(list)):
        print(f"{i+1}. {list[i]}")
    print(f"Total belum kembali: {len(list)} pengunjung")
    print()
    
tampilkan_pengunjung()
filter_belum_kembali()

# SOAL 2
def info_perpustakaan():
    print("Info Perpustakaan:")
    nama, alamat, telp = info_perpus
    print(f"Nama    : {nama}")
    print(f"Alamat  : {alamat}")
    print(f"Telp    : {telp}\n")

def rekap_kategori():
    buku = []
    for dict in pengunjung_hari_ini:
        kategori = dict['kategori']
        buku.append(kategori)    
    buku = set(buku)
    print(f"Kategori Buku Unik: {buku}")
    print(f"Jumlah Kategori : {len(buku)}")
    print()

    print("Rekap per kategori:")
    dict = {"test" : 0}
    for j in buku:
        dict[j] = 0

    for i in pengunjung_hari_ini:
        kategori = i['kategori']
        for j in buku:
            if kategori == j:
                dict[j] += 1
    maks = max(dict.values())
    terbanyak = [i for i,j in dict.items() if j == maks]
    for j in buku:
        print(f"{j}   : {dict[j]} pengunjung")
    print()
    print(f"Kategori terbanyak : {terbanyak} ({maks} pengunjung)\n")

info_perpustakaan()
rekap_kategori()

# SOAL 3
class Pengunjung:
    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
        Pengunjung.jumlah += 1
    
    def get_id(self):
        return self.__id
    def get_nama(self):
        return self.__nama
    def get_kategori(self):
        return self.__kategori
    
    def tampilkan_info(self):
        print(f"ID        : {self.get_id()}")
        print(f"Nama      : {self.get_nama()}")
        print(f"Kategori  : {self.get_kategori()}")

    jumlah = 0
    @staticmethod
    def hitung_pengunjung():
        return Pengunjung.jumlah

    
class PengunjungPrioritas(Pengunjung):
    def __init__(self, id , nama, kategori, prioritas):
        super().__init__(id, nama, kategori)
        self.prioritas = prioritas

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Prioritas : {self.prioritas}")
        if self.prioritas == "Mendesak":
            print("** Layani Segera! **")

tes = Pengunjung('M001' , 'Rina', 'Fiksi')
tes2 = PengunjungPrioritas('M007' , 'Gilang', 'Referensi', 'Mendesak')
tes.tampilkan_info()
print()
tes2.tampilkan_info()

print(f"Total pengunjung terdaftar: {Pengunjung.hitung_pengunjung()}")


# SOAL 4
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class AntrianPeminjaman:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        curNode = self.head
        if self.head == None:
            self.head = Node(data)
        else:
            while curNode.next:
                curNode = curNode.next
            curNode.next = Node(data)

    def tampilkan(self):
        if self.head == None:
            return
        else:
            curNode = self.head
            print("===== ANTRIAN PEMINJAMAN =====")
            i = 1
            while curNode:
                print(f"[{i}] {curNode.data["id"]:<4} - {curNode.data['nama']:<7} | {curNode.data['kategori']:<10}")
                curNode = curNode.next
                i += 1
            print(f"Total Antrian: {i-1}\n")

    def panggil_berikutnya(self):
        if self.head == None:
            return
        curNode = self.head
        print("Memanggil pengunjung berikutnya...")
        print(f"Silakan masuk: {curNode.data['nama']} ({curNode.data['id']}) - {curNode.data['kategori']}\n")
        self.head = curNode.next

    def cari(self, nama):
        if self.head == None:
            return
        curNode = self.head

        if curNode.data['nama'] == nama:
            print(f"Mencari '{nama}'...")
            print(f"Ditemukan: {curNode.data['id']} - {nama} | {curNode.data['kategori']} (posisi ke-1)\n")
            return
        
        posisi = 1
        while curNode.next and curNode.next.data['nama'] != nama:
            curNode = curNode.next
            posisi += 1
        posisi += 1
        if curNode.next == None:
            return
        
        print(f"Mencari '{nama}'...")
        print(f"Ditemukan: {curNode.next.data['id']} - {nama} | {curNode.next.data['kategori']} (posisi ke-{posisi})\n")

        

    def hapus_berdasarkan_id(self, id):
        if self.head == None:
            return
        curNode = self.head
        if curNode.data['id'] == id:
            print(f"Menghapus pengunjung dengan ID {curNode.data['id']}...")
            print(f"{curNode.data['nama']} ({curNode.data['id']}) berhasil dihapus dari antrian.\n")
            self.head = curNode.next
            return
        
        while curNode.next and curNode.next.data['id'] != id:
                curNode = curNode.next
        
        if curNode.next == None:
            return
        
        print(f"Menghapus pengunjung dengan ID {curNode.next.data['id']}...")
        print(f"{curNode.next.data['nama']} ({curNode.next.data['id']}) berhasil dihapus dari antrian.\n")
        curNode.next = curNode.next.next    
    
    def hitung(self):
        if self.head == None:
            return 0
        jumlah = 0
        curNode = self.head
        while curNode:
            curNode = curNode.next
            jumlah+=1

        return jumlah

antrian = AntrianPeminjaman()
antrian.tambah({"id": "M001", "nama": "Rina", "kategori": "Fiksi"})
antrian.tambah({"id": "M002", "nama": "Hendra", "kategori": "Sains"})
antrian.tambah({"id": "M003", "nama": "Siti", "kategori": "Fiksi"})
antrian.tambah({"id": "M004", "nama": "Taufik", "kategori": "Hukum"})
antrian.tampilkan()
antrian.panggil_berikutnya()
antrian.tampilkan()
antrian.hapus_berdasarkan_id("M003")
antrian.tampilkan()
antrian.cari("Taufik")
print("Total antrian:", antrian.hitung())
