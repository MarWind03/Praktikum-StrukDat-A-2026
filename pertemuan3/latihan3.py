class Person:
    def __init__(self , nama , jenis_kelamin, umur):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.umur = umur

class Karyawan(Person):
    def __init__(self, nama, jenis_kelamin, umur , gaji):
        super().__init__(nama, jenis_kelamin, umur)
        self._gaji = gaji

    def get_gaji(self):
        return self._gaji

    def set_gaji(self , gaji):
        self._gaji = gaji
    
class Rekening:
    def __init__(self, noRek, PIN):
        self.noRek = noRek
        self.__PIN = PIN

    def get_PIN(self):
        return self.__PIN
    
    def set_PIN(self , PIN):
        self.__PIN = PIN

p1 = Person("Damar" , "Laki" , 19)
p2 = Karyawan("Aldi" , "Laki" , 19 , 9999999)
p3 = Rekening("12022006", 123456)

for x in (p1 , p2):
    print(x.nama)
    print(x.jenis_kelamin)
    print(x.umur)
    if(x is p2):
        print(x.get_gaji())

print("PIN SEBELUM DIUBAH : ", p3.get_PIN())
p3.set_PIN(999999)
print("PIN SETELAH DIUBAH : ", p3.get_PIN())


