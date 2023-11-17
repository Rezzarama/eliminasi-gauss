import math

print('Soal UTS nomer 1\n')

# Koefisien a, b, dan c dalam persamaan kuadrat ax^2 + bx + c = 0
a = 1
b = -1
c = -1

# Menampilkan persamaan kuadrat
print(f"Persamaan kuadrat: {a}x^2 + {b}x + {c} = 0\n")

# Menghitung diskriminan
diskriminan = b**2 - 4*a*c
print(f"Langkah 1: Menghitung Diskriminan = b^2 - 4ac")
print(f"Diskriminan = {b}^2 - 4*{a}*{c}")
print(f"Diskriminan = {diskriminan}\n")

# Menyelesaikan persamaan kuadrat
if diskriminan > 0:
    print("Langkah 2: Diskriminan > 0")
    print("Solusi nyata (dua solusi):\n")
    x1 = (-b + math.sqrt(diskriminan)) / (2*a)
    x2 = (-b - math.sqrt(diskriminan)) / (2*a)
    print(f"x1 = (-(-{b}) + √{diskriminan}) / (2*{a})")
    print(f"x1 = ({b} + {math.sqrt(diskriminan)}) / {2*a}")
    print(f"x1 = {x1}\n")

    print(f"x2 = (-(-{b}) - √{diskriminan}) / (2*{a})")
    print(f"x2 = ({b} - {math.sqrt(diskriminan)}) / {2*a}")
    print(f"x2 = {x2}\n")
    print(f"Solusi x1: {x1}")
    print(f"Solusi x2: {x2}")
    
elif diskriminan == 0:
    print("Langkah 2: Diskriminan = 0")
    print("Solusi tunggal:\n")
    x = -b / (2*a)
    print(f"x = -({b}) / (2*{a})")
    print(f"x = {x}\n")
    print(f"Solusi tunggal: {x}")
    
else:
    print("Langkah 2: Diskriminan < 0")
    print("Solusi kompleks:\n")
    realPart = -b / (2*a)
    imaginaryPart = math.sqrt(abs(diskriminan)) / (2*a)
    print(f"x1 = {realPart} + {imaginaryPart}i")
    print(f"x2 = {realPart} - {imaginaryPart}i")
    print(f"Solusi x1: {realPart} + {imaginaryPart}i")
    print(f"Solusi x2: {realPart} - {imaginaryPart}i")


# Persamaan linier: 2x - 4 = 8
print('\n\n\nSoal UTS nomer 2\n')


# Langkah 1: Menampilkan persamaan
print("Persamaan linier: 2x - 4 = 8\n")

# Langkah 2: Mengisolasi variabel x
# Menambahkan 4 ke kedua sisi persamaan
right_side = 8  # nilai konstanta di sisi kanan
constant = 4  # konstanta yang akan ditambahkan ke kedua sisi persamaan

right_side += constant  # Menambahkan 4 ke sisi kanan

print("Langkah 2: Menambahkan 4 ke kedua sisi persamaan")
print(f"2x = {right_side}\n")

# Langkah 3: Membagi kedua sisi dengan koefisien variabel x
x_coef = 2  # koefisien variabel x
x_value = right_side / x_coef  # Menghitung nilai x

print("Langkah 3: Membagi kedua sisi dengan koefisien variabel x")
print(f"x = {right_side} / {x_coef}")
print(f"x = {x_value}\n")

# Hasil akhir
print(f"Jadi, nilai x dalam persamaan adalah x = {x_value}")
