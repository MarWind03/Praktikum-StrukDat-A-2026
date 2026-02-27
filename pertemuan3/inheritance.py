# Membuat kelas bernama Person, dengan properti firstname 
# dan lastname, serta sebuah metode printname.
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

# Membuat sebuah kelas bernama Student, 
# yang akan mewarisi properti dan metode dari kelas Person
class Student(Person):
  pass

class Student(Person):
  def __init__(self, fname, lname):
    # menambahkan properti lainnya
    pass

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

# Tambahkan properti bernama graduationyear ke kelas Student:
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

# Tambahkan parameter tahun, dan berikan tahun yang benar 
# saat membuat objek.
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

