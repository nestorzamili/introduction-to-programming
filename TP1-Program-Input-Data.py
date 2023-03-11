# Meminta input nama pengguna
nama = input("Masukkan nama Anda: ")
print("Stock Gudang Input Barang\n###########################")
print()
print("Selamat datang", nama)
print()

# Meminta input rincian barang
nama_barang = input("Masukkan nama barang yang mau ditambah: ")
jumlah_barang = int(input("Masukkan jumlah barang yang mau ditambah: "))
harga_beli = float(input("Masukkan harga beli untuk barang tersebut: "))
harga_jual = float(input("Masukkan harga jual untuk barang tersebut: "))

# Mengubah harga beli dan harga jual ke dalam format Rupiah
harga_beli_formatted = "Rp. " + "{:,.2f}".format(harga_beli)
harga_jual_formatted = "Rp. " + "{:,.2f}".format(harga_jual)

# Menampilkan rincian barang
print()
print("Stock Gudang Rincian Barang\n###########################")
print("Nama Barang   :", nama_barang)
print("Jumlah barang :", jumlah_barang)
print("Harga beli    :", harga_beli_formatted)
print("Harga jual    :", harga_jual_formatted)
