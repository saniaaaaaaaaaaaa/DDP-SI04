from animals import *

class burung(animal):
    def __init__(self, nama, makanan, hidup, berkembangbiak, jenis_bulu, bunyi):
         super().__init__(nama, makanan, hidup, berkembangbiak,)
         self.jenis_bulu =jenis_bulu
         self.bunyi = bunyi
         
    def cetak_burung(self):
        super().cetak()
        print(f"hewan ini berbulu {self.jenis_bulu} dan hewan ini berbunyi {self.bunyi}")
        
print ("-----cetak burung-------")      
beo = burung("Burung beo", "Biji_bijian", "Udara", "Bertelur", "Blue and Orange", "Kamu Pintar")
beo.cetak_burung()

#objek 2
Gagak = burung("Burung Gagak", "Bangkai Hewan", "Pegunungan", "Bertelur", "Hitam", "Gakgakgakgak")
Gagak.cetak_burung()