# Super Class dan Objek menggunakan string input
class Pahlawanku:
    def __init__(self,name,hero,about):
        self.name = input("Nama Pahlawan :")
        self.hero = hero
        self.about = about
    def showInfo(self):
       print(f"{self.name} sebagai Pahlawan {self.hero} dan {self.about}")
#Sub Class Revolusi
class Revolusi(Pahlawanku):
    def __init__(self,name=()):
        print("="*35, "Pahlawaku","=" * 35)
        # Menggunaka SuperClass untuk pahlawanku dan Constructor
        super().__init__(name, "Revolusi","Gugur Karena kebiadaban PKI.")
        super().showInfo()
# Sub Class Nasional
class Nasional(Pahlawanku):
    def __init__(self, name=()):
        super().__init__(name," Nasional ","Panglima Perang Kemerdekaan." )
        super().showInfo()
#Sub Class Guru
class Guru(Pahlawanku):
    def __init__(self, name=()):
        super().__init__(name,"Pahlawan Tampa Tanda Jasa","Jasa Jasamu Sangat Berharga." )
        super().showInfo()
#Menciptakan New Objek Rev, Nas dan NN
Rev = Revolusi()
Nas= Nasional()
NN= Guru()
print("Hore Saya Berhasil Boss")
print("=" * 32, "S E L E S A I", "=" * 34)
