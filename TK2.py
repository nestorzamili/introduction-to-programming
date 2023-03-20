# Input dan validasi Nama serta NIM Mahasiwa
while True:
    nama_mahasiswa = input("Masukkan Nama Anda [1..25] : ")
    if 1 <= len(nama_mahasiswa) <= 25:
        break
    print("Nama harus 1 sampai 20 karakter.")

while True:
    nim = input("Masukkan NIM Anda [harus 10 karakter] : ")
    if len(nim) == 10:
        break
    print("NIM harus 10 karakter.")

# Tampilkan selamat datang
print()
print('@' * 90)
print("\nRegistrasi sukses...")
print("Selamat datang ", nama_mahasiswa, "[NIM :", nim,"]..")
print("\nMari belajar macam-macam deret bilangan..")
print()
print('@' * 90)
print()

while True:
    # Input angka
    while True:
        angka = int(input("Masukkan Sembarang Angka [5..20]: "))
        if 5 <= int(angka) <= 20:
            break
        print("Input harus berupa angka antara 5 sampai 20.")

    # Fungsi untuk menghitung deret bilangan genap
    def bilangan_genap(angka):
        total = 0
        for i in range(2, 2*angka+1, 2):
            total += i
            print(i, end=' ')
        return total
    print('@' * 90)
    print("\nDeret Bilangan")
    print('#' * 15)
    print()
    print(angka, "Bilangan genap :")
    total_genap = bilangan_genap(angka)
    print("\nHasil Penjumlahan =", total_genap)

    # Fungsi untuk menghitung deret bilangan ganjil
    def bilangan_ganjil(angka):
        total = 0
        for i in range(1, 2*angka, 2):
            total += i
            print(i, end=' ')
        return total
    print()
    print(angka, "Bilangan ganjil :")
    total_ganjil = bilangan_ganjil(angka)
    print("\nHasil Penjumlahan =", total_ganjil)

    # Fungsi untuk menghitung deret bilangan fibonacci
    def bilangan_fibonacci(angka):
        total = 0
        a, b = 1, 1
        for i in range(angka):
            total += a
            print(a, end=' ')
            a, b = b, a+b
        return total
    print()
    print(angka, "Bilangan Fibonacci :")
    total_fibonacci = bilangan_fibonacci(angka)
    print("\nHasil Penjumlahan =", total_fibonacci)

    # Tanyakan apakah ingin mengulang atau tidak
    print()
    ulangi = input("Anda ingin mengulang? [y/t] : ")
    if ulangi.lower() != 'y':
        break
    elif ulangi.upper() != 'Y':
        break
print("\nTerima kasih, semoga ilmu anda bertambah")