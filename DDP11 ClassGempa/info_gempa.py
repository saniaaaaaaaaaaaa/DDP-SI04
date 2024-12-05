from Gempa import *

#Membuat objek gempa dengan lokasi dan skala
gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("Jayapura", 3.3)
gempa5 = Gempa("Garut", 4.0)

#info gempa
print("## Gempa Bumi dengan Skala ##")
print()
gempa1.dampak() # memanggil method dampak()

print()
print("## Gempa Bumi dengan Skala ##")
print()
gempa2.dampak() # memanggil method dampak()

print()
print("## Gempa Bumi dengan Skala ##")
print()
gempa3.dampak() # memanggil method dampak()

print()
print("## Gempa Bumi dengan Skala ##")
print()
gempa4.dampak() # memanggil method dampak()

print()
print("## Gempa Bumi dengan Skala ##")
print()
gempa5.dampak() # memanggil method dampak()


