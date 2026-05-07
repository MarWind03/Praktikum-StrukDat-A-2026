from abc import ABC, abstractmethod

class Hewan(ABC):
  @abstractmethod
  def suara(self):
    pass

class Kucing(Hewan):
  def suara(self):
    print("Meong!")

class Anjing(Hewan):
  def suara(self):
    print("Guk guk!")

# hewan1 = Hewan() # Jika ini dijalankan, akan menghasilkan ERROR

kucing1 = Kucing()
anjing1 = Anjing()

kucing1.suara()
anjing1.suara()

from abc import ABC, abstractmethod

class Vehicle(ABC):
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  
  # Metode biasa (akan diwariskan apa adanya)
  def deskripsi(self):
    print("Ini adalah kendaraan merek", self.brand)
  
  # Metode abstrak (wajib dibuat ulang oleh kelas turunan)
  @abstractmethod
  def roda(self):
    pass

class Car(Vehicle):
  def roda(self):
    print("Memiliki 4 roda.")

class Motorcycle(Vehicle):
  def roda(self):
    print("Memiliki 2 roda.")

car1 = Car("Ford", "Mustang")
motor1 = Motorcycle("Honda", "CBR")

# Menggunakan metode biasa yang diwarisi
car1.deskripsi()
# Menggunakan metode yang mengimplementasikan metode abstrak
car1.roda()

motor1.deskripsi()
motor1.roda()