class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.id = 0

    def is_empty(self):
        return self.size == 0
    
    def cek_antrian(self):
        if self.is_empty():
            print(f"[CEK] Apakah antrian kosong? -> YA, antrian masih kosong.")
        else:
            print(f"[CEK] Apakah antrian kosong? -> TIDAK, antrian masih ada.")
    
    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1  
        self.id += 1
        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self.id})")

    def dequeue(self):
        if self.is_empty():
            print("Antrian Masih Kosong.")
            return
        tmp_nama = self.head.nama
        tmp_keluh = self.head.keluhan
        self.head = self.head.next

        if self.head.next is None:
            self.tail = None
        
        self.size -= 1
        print(f"[PANGGIL] Dokter memanggil: {tmp_nama} (keluhan: {tmp_keluh})")
    
    def info(self):
        print(f"[INFO] Jumlah Pasien Menunggu: {self.size} orang.")

    def peek(self):
        if self.is_empty():
            print("Antrian masih kosong.")
        else:
            print(f"[PEEK] Pasien berikutnya: {self.head.nama} - {self.head.keluhan}\n")

    def tampilkan_antrian(self):
        if self.is_empty():
            print("Antrian masih kosong.")
        else:
            print(f"[ANTRIAN SAAT INI]")
            idx = 1
            tmp = self.head
            while tmp.next:
                print(f"  {idx:>2}. {tmp.nama:<10} -> {tmp.keluhan}")
                tmp = tmp.next
                idx += 1
            print(f"  {idx:>2}. {tmp.nama:<10} -> {tmp.keluhan}\n")

    def clear(self):
        self.head = self.tail = None
        self.id = self.size = 0
        print(f"[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.") 
    


print("====================================")
print("  SISTEM ANTRIAN POLI UMUM")
print("  RS SEHAT BERSAMA")
print("====================================\n")

queue = QueueLinkedList()
queue.cek_antrian()
queue.enqueue("BUDI", "Demam Tinggi")
queue.enqueue("ANI", "Batuk Pilek")
queue.enqueue("CITRA", "Sakit Kepala")
queue.info()
queue.peek()
queue.dequeue()
queue.enqueue("DODI", "Nyeri Perut")
queue.tampilkan_antrian()
queue.dequeue()
queue.info()
print()
queue.clear()
queue.cek_antrian()
queue.enqueue("BUDI", "Demam Tinggi")
queue.enqueue("ANI", "Batuk Pilek")
queue.enqueue("CITRA", "Sakit Kepala")
queue.enqueue("DODI", "Nyeri Perut")
queue.tampilkan_antrian()
print()

print("====================================")
print(" Simulasi Selesai!")
print("====================================")
