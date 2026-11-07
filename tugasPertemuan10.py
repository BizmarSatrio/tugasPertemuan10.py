# 1. Tuple
# a. Buatlah sebuah Tuple bernama mahasiswa yang berisi 3 data diri Anda: ("Nama", "NIM", "Prodi"). 
mahasiswa = ("Bizmar Satrio Hutomo","2605060062","Teknologi Informasi")
print(mahasiswa)
# b. Tampilkan data NIM dan Prodi ke layar dengan cara mengakses indeksnya.
print(mahasiswa[1])
print(mahasiswa[2])
print()

# c. Coba jalankan kode mahasiswa[2] = "Teknologi Informasi".
# Amati pesan error yang muncul, lalu jelaskan mengapa hal tersebut terjadi 
mahasiswa[2] = "Teknologi Informasi"

# d. Buatlah sebuah Set bernama nilai_angka dari barisan angka berikut: 10, 4, 3, 2, 4, 10, 7, 5. 
# Cetak nilai_angka ke layar dan jelaskan apa yang terjadi pada angka 10 dan 4 yang ditulis dua kali! 
nilai_angka = {10,4,3,2,4,10,7.5}
print(nilai_angka)
print()

# 2. Manipulasi Dictionary
# a. Buatlah sebuah dictionary bernama data_mahasiswa 
# dengan pasangan key-value berikut: - "nim": "240101" - "nama": "Budi Santoso" - "prodi": "Teknologi Informasi"
data_mahasiswa = {
    "nim":"240101",
    "nama":"Budi Santoso",
    "prodi":"Teknologi Informasi",
}
print(data_mahasiswa)
# b. Ubah nilai "prodi" menjadi "Sastra Mesin " sekaligus menambahkan key baru "angkatan" dengan nilai 2026. 
data_mahasiswa.update({"prodi":"Sastra Mesin"})
data_mahasiswa.update({"angkatan":"2026"})
print(data_mahasiswa)
print()

# c. Hapus data "nim", lalu tampilkan hasil akhir dictionary ke layar. 
del data_mahasiswa["nim"]
print(data_mahasiswa)
print()

# 3. Perulangan pada Dictionary 
# a. Buatlah dictionary bernama keranjang dengan data harga buah berikut: 
# {"apel": 5000, "pisang": 3000, "jeruk": 7000, "anggur": 15000}
keranjang = {
    "apel":5000,
    "pisang":3000,
    "jeruk":7000,
    "anggur":15000,
}
print(keranjang)

# b. Gunakan perulangan untuk menampilkan setiap barang dan harganya dengan format: "Harga apel: Rp 5000" 
total_belanja = 0
for barang,harga in keranjang.items():
    print(f"Harga {barang}: Rp{harga}")
    total_belanja += harga
print()
# c. Tampilkan total belanja 
print(f"Total Belanja: Rp{total_belanja} ")