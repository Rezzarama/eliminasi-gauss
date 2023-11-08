# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         current_element = arr[i]
#         j = i
#         while j > 0 and arr[j - 1] > current_element:
#             arr[j] = arr[j - 1]
#             j -= 1
#         arr[j] = current_element

# # Array yang akan diurutkan
# arr = [1, 5, 3, 7, 2]
# insertion_sort(arr)

# # Cetak array yang sudah diurutkan
# print(arr)

# Meminta pengguna memasukkan angka desimal
decimal_number = int(input("Masukkan angka desimal: "))

# Menginisialisasi variabel untuk menyimpan bilangan biner
binary_number = ""

# Proses konversi ke bilangan biner
while decimal_number > 0:
    remainder = decimal_number % 2
    binary_number = str(remainder) + binary_number
    decimal_number //= 2

# Mencetak hasil
print(f"Bilangan biner: {binary_number}")
