# Menyelesaikan Persamaan Kuadrat ax**2 + bx + c = 0
 
# Mengimpor Modul Cmath
import cmath
 
# Menginput Angka
a = int(input("Masukkan Nilai A : "))
b = int(input("Masukkan Nilai B : "))
c = int(input("Masukkan Nilai C : "))
 
# Menghitung Diskriminan
d = (b**2) - (4*a*c)
 
# Menghitung x1 dan x2
x1 = (-b-cmath.sqrt(d))/(2*a)
x2 = (-b+cmath.sqrt(d))/(2*a)
 
#Menampilkan Hasil x1 dan x2
print(f"Hasil Persamaan Kuadrat adalah {x1} dan {x2}")
