from animals import *

class ular(animal):
    def __init__(self, nama, makanan, hidup, berkembangbiak, jenis_ular, jenis_bisa):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.jenis = jenis_ular
        self.bisa = jenis_bisa
        
    def cetak_ular(self):
         super().cetak()
         print(f"jenis ular ini {self.jenis} dan jenis bisa {self.bisa}")
         
print("-----jenis ular----")
kobra = ular("ular kobra", "kadal", "darat", "bertelur", "kaca_tunggal", "neurotoxin")
kobra.cetak_ular()

#objek 2
sanca = ular("ular sanca", "burung dan biawak", "air", "bertelur", "sanca_hijau", "tidak_berbisa")
sanca.cetak_ular()
        