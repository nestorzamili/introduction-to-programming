print("     Belajar Deret Aritmatika, Geometri, dan menghitung Faktorial    ")

while True:
    # Input banyak angka dan beda masing-masing angka
    while True:
        angka = int(input("\nMasukkan banyak angka yang mau dicetak [2..10]: "))
        if 2 <= int(angka) <= 10:
            break
        print("Input harus berupa angka antara 2 sampai 10.")

    while True:
        beda = int(input("Masukkan beda masing-masing angka [2..9]: "))
        if 2 <= int(beda) <= 9:
            break
        print("Input harus berupa angka antara 2 sampai 9.")

    # Tampilkan deret aritmatika
    print("\nDeret Aritmatika   : ")
    for i in range(angka):
        print(i*beda+1, end=' ')
    print()

    # Tampilkan deret geometri
    print("\nDeret Geometri     : ")
    for i in range(angka):
        print(beda**i, end=' ')
    print()

    # Tampilkan faktorial
    print("\nFaktorial dari", angka, "  : ")
    total = 1
    for i in range(angka, 0, -1):
        print(i, end='')
        if i != 1:
            print(" * ", end='')
        total *= i
    print(" = ", total)
    
    # Tanyakan apakah ingin mengulang atau tidak
    print()
    ulangi = input("Anda mau ulang? [y/t] : ")
    if ulangi.lower() != 'y':
        break
    elif ulangi.upper() != 'Y':
        break
print("\nTerima kasih, semoga ilmu anda bertambah")