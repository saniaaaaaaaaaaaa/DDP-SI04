class Gempa:
    #konstraktor inisialisasi atribut
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
        
    #method penentua skala gempa
    def dampak(self):
        #logika/statmen
        if self.skala < 2:
            print("Gempa Tidak Berasa")
        elif  2 <= self.skala <=4:
            print("Gempa Berdampak Bangunan retak")
        elif 4 <= self.skala <=6:
            print("Gempa Berdampak Bangunan Roboh")
        elif self.skala > 6:
            print("Gempa Besara Berpotensi Tsunami")
            
        #Menampilka lokasi dan skla gempa
        print(f"lokasi gempa: {self.lokasi}")
        print(f"skala gempa: {self.skala}")
        
        