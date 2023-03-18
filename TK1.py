print("RESTORAN BUNGAR")
print('=' * 40)
print("\nSelamat siang...")

# Input jumlah orang dan nama pemesan
jumlah_orang = int(input("Pesan untuk berapa orang: "))
nama_pemesan = input("Pesanan atas nama: ")

# Menu makanan beserta harga
print("\nMenu spesial hari ini")
print('=' * 40)
menu = {
    "1. Nasi Goreng Spesial": 9999.99,
    "2. Ayam Bakar Spesial": 12345.67,
    "3. Steak Sirloin Spesial": 21108.40,
    "4. Kwetiaw Siram Spesial": 13579.13,
    "5. Kambing Guling Spesial": 98765.43
}

for item, price in menu.items():
    print("{:<25} @ Rp {:,.2f}".format(item, price))

# Input jumlah pesanan untuk setiap menu
print("\nPesanan Anda [batas pesanan 0-10 porsi]")
print()
jumlah_pesanan = {}
for item, price in menu.items():
    jumlah = int(input("{:<25} = ".format(item)))
    jumlah_pesanan[item] = jumlah

# Detail pembelian
print("\nSelamat menikmati makanan anda...")
print("\nPembelian :")
print("{:<25} {:<15} {:<20} {:<30}".format("Menu", "Jumlah Pesanan", "Harga Satuan", "Harga Total"))
print("-" * 80)
total_harga = 0
for item, price in menu.items():
    if jumlah_pesanan[item] > 0:
        harga_total = price * jumlah_pesanan[item]
        print("{:<25} {:<15} Rp. {:<12,.2f} =   Rp. {:<5,.2f}".format(item, f"{jumlah_pesanan[item]} porsi    *", price, harga_total))
        total_harga += harga_total

print("-" * 80)
print("{:<58} =   Rp {:,.2f}".format("Total Pembelian", total_harga))


# Hitung harga diskon dan total pembelian setelah diskon
harga_diskon = total_harga * 0.1
total_pembelian_setelah_diskon = total_harga - harga_diskon

# Hitung pembelian per orang
pembelian_per_orang = total_pembelian_setelah_diskon / jumlah_orang

print("\n{:<58} =   Rp {:,.2f}".format("Disc. 10 % <Masa Promosi>", harga_diskon))
print("-" * 80)
print("{:<58} =   Rp {:,.2f}".format("Total Pembelian setelah disc 10 %", total_pembelian_setelah_diskon))
print("{:<58} =   Rp {:,.2f}".format("Pembelian per orang <untuk "+ str(jumlah_orang) + " orang>", pembelian_per_orang))

print("\nTerima kasih atas kunjungan Anda...")
input("\nTekan ENTER untuk keluar...")
