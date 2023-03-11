# Program Ramalan
print("Selamat Datang Di Program Ramalam Cupu")
print('+' * 40)
print()

# Masukkan detail user dan pasangannya
print("Data Anda : ")
print('\u2764' * 7)
nama = input("Masukkan Nama Anda  : ")
umur = int(input("Masukkan Umur Anda  : "))
print()
print("Data Pasangan Anda : ")
print('\u2764' * 13)
nama_pasangan = input("Masukkan Nama Pasangan Anda  : ")
umur_pasangan = int(input("Masukkan Umur Pasangan Anda  : "))

print()
print(nama, [umur], "tahun")

# Mencetak pola love
print()
print("   ❤❤❤     ❤❤❤")
print(" ❤❤❤❤❤,,❤❤❤❤❤")
print(" ❤❤❤❤❤❤❤❤❤❤❤")
print("  ❤❤❤❤❤❤❤❤❤❤")
print("    ❤❤❤❤❤❤❤❤")
print("      ❤❤❤❤❤")
print("         ❤❤")
print()

print(nama_pasangan, [umur_pasangan], "tahun")
print()
hasil = input("Tekan ENTER untuk melihat hasil ramalan...")

# memilih angka random
import random
random_number = random.randint(50, 100)
cocok = round(random_number / 1.1, 2)
print()
print("Kecocokan anda dengan pasangan anda adalah : ", cocok, "%")
print()
print()
print("Terima Kasih karena anda telah menggunakan jasa Ramalan kami.. ^^v")
