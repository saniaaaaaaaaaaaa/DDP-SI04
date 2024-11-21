#membuat sebuah funsi bernama celcius_ke_fahrenheit yang menerima satu argumen:suhu dalam celcius.fungsi ini harus mengembalikan

def celcius_ke_fahrenheit(celcius):
    print(celcius * 9/5 + 32)
    
celcius_ke_fahrenheit(0)

print("---------------mencari nilai genap---------------")
#no2
def is_genap(genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(7)

print("--------------------keterangan lulus dan tidak lulus-------------------")
#rata-rta nilai kelulusan 70
def skor(nilai):
    if nilai >= 80:
        print("lulus")
    else:
        print("gagal")
skor(80)
skor(60)

print("--------------------mencetak bilangan ganjil-------------------")
def bil_ganjil(ganjil):
    for i in range(1,ganjil+1, 2):
        print(i, end=" ")
bil_ganjil(20)
