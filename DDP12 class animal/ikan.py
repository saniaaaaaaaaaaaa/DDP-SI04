from animals import *

class ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembangbiak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.warna = warna_ikan
        self.jenis = jenis_ikan
        
    def cetak_ikan(self):
        super().cetak()
        print(f"warna ikan ini adalah {self.warna} dan hewan ini jenis ikan {self.jenis}")
        
print("-----jenis ikan-----")      
nemo = ikan("ikan Nemo", "plankton", "air", "bertelur", "orange", "air laut")
nemo.cetak_ikan()

#objek 2
koi = ikan("ikan Koi", "cacing sutra", "air", "bertelur", "orange dan putih", "air tawar")
koi.cetak_ikan()

