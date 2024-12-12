class animal:
    def __init__(self, nama, makanan, hidup, berkembangbiak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangbiak = berkembangbiak
        
    def cetak(self):
        print(f"hewan {self.nama} ini memakan {self.makanan}, hewan ini juga hidup di{self.hidup} dan berkembangbiak dengan cara {self.berkembangbiak}")
       
# c1 = animal("burung", "biji_bijian", "darat", "bertelur")  
# c1.cetak()