# 💻 Warung Seblak Jaya - Point of Sale System

Aplikasi berbasis Python yang digunakan untuk mencatat transaksi penjualan makanan seperti Mie Jebew dan Seblak di Warung Seblak Jaya - SMKN 1 Probolinggo. Sistem ini mendukung multi pembeli, pencetakan struk, serta penyimpanan data transaksi ke dalam format JSON.

---

## 📌 Fitur

- ✅ Input transaksi hingga 5 pembeli sekaligus
- ✅ Pilihan menu Mie Jebew dan Seblak dengan level pedas, rasa, dan jenis kuah
- ✅ Cetak struk transaksi dengan format rapi
- ✅ Simulasi pembayaran dengan metode Cash atau QRIS
- ✅ Simpan transaksi ke file transaksi.json
- ✅ Validasi input jumlah dan nominal pembayaran
- ✅ Tampilkan isi file JSON setelah transaksi

---

## 🧰 Teknologi yang Digunakan

- Bahasa Pemrograman: *Python 3*
- Modul Bawaan: json
- Tidak menggunakan library eksternal
- Bisa dikompilasi menjadi .exe menggunakan pyinstaller

---

## 🛠 Cara Instalasi

### 📦 Menggunakan File Executable (.exe)

1. *Unduh File yang Diperlukan*
   - Buka repository: Pemesanan-Online-Seblak-Jaya
   - Masuk ke folder dist dan unduh:
     - dist/UASDPK.exe
     - dist/transaksi.json (jika tersedia)

2. *Jalankan Aplikasi*
   - Simpan file dist/UASDPK.exe dan dist/transaksi.json dalam folder yang sama
   - Klik dua kali dist/UASDPK.exe untuk menjalankan aplikasi
   - Jika muncul peringatan dari Windows Defender, klik Run anyway atau tambahkan pengecualian secara manual

3. *Persyaratan Sistem*
   - Hanya untuk sistem operasi Windows
   - .NET Framework mungkin dibutuhkan
   - Tidak memerlukan Python jika menggunakan file .exe

### 🧑‍💻 Instalasi Dari Kode Sumber (Source Code)

1. Clone repositori ini:
bash
git clone https://github.com/Ficky675/Pemesanan-Online-Seblak-Jaya

2. Masuk ke di rektori proyek:
bash
cd Pemesanan-Online-Seblak-Jaya


2. Instal dependensi yang diperlukan:
bash
pip instal dist/transaksi.json


2. Masuk ke di rektori proyek:
bash
phyton src\UASDPK.py


---

## 👨‍🏫 Panduan Pengguna

1. Jalankan program
2. Masukkan nama penjual
3. Masukkan jumlah pembeli (maksimal 5)
4. Untuk setiap pembeli:
   - Masukkan nama pembeli
   - Pilih kategori: Mie Jebew, Seblak, atau Selesai
   - Pilih topping dan jumlah untuk tiap kategori
   - Masukkan level pedas (1-5), jenis kuah (berkuah/nyemek), dan rasa (asin/manis/gurih manis) sesuai pilihan kategori
5. Setelah selesai memilih, pilih metode pembayaran: Cash atau QRIS
6. Masukkan nominal pembayaran (minimal sama dengan total)
7. Struk akan dicetak ke terminal
8. Transaksi otomatis disimpan ke transaksi.json
9. Anda bisa memilih untuk menampilkan isi file JSON setelah transaksi

---

## 📁 Struktur Folder

plaintext
.
├── UASDPK.py           # File utama Python (kode sumber)
├── UASDPK.exe          # File executable hasil konversi (opsional)
├── UASDPK.spec         # File spesifikasi PyInstaller (jika dikompilasi)
├── transaksi.json      # Output file JSON hasil transaksi
└── README.md           # Dokumentasi aplikasi


---

## 📄 Dokumentasi Kode (Ringkasan)

*flowchart*
![alt text](IMG_20250607_124716.jpg?raw=true)

*Tampilan Utama*
![alt text](gambar/Tampilan_Utama.jpg?raw=true)

*Tampilan Kategori 1*
![alt text](gambar/Kategori_1.jpg?raw=true)

*Tampilan Kategori 2*

![alt text](gambar/Kategori_2.jpg?raw=true)

*Tampilan Kategori 3*

![alt text](gambar/Kategori_3.jpg?raw=true)

*Tampilan Struk*
![alt text](gambar/Struk_pembelanjaan.jpg?raw=true)

*Tampilan JSON*
bash
{
    "penjual": "wira",
    "total": 74000,
    "pembeli": [
        {
            "nomor": 1,
            "nama": "adit",
            "kuah": "Nyemek",
            "rasa": "Gurih",
            "level_mie": "3",
            "level_seblak": "4"
        }
    ],
    "items": [
        {
            "pembeli_ke": 1,
            "nama_pembeli": "adit",
            "nama_item": "Mie Jebew Original",
            "kategori": "Mie Jebew",
            "jumlah": 1,
            "subtotal": 10000
        },
        {
            "pembeli_ke": 1,
            "nama_pembeli": "adit",
            "nama_item": "Toping Sosis",
            "kategori": "Mie Jebew",
            "jumlah": 22,
            "subtotal": 44000
        },
        {
            "pembeli_ke": 1,
            "nama_pembeli": "adit",
            "nama_item": "Pentol",
            "kategori": "Seblak",
            "jumlah": 20,
            "subtotal": 20000
        }
    ]
}


---

## 📝 Lisensi

Proyek ini dibuat untuk keperluan tugas UAS DPK dan bebas digunakan untuk keperluan edukasi.

---

## 🙌 Kontributor

- *Nama:* [Achmad Ficky Andrian]
- *Sekolah:* SMKN 1 Probolinggo
- *Mata Pelajaran:* Dasar Pemrograman Komputer (DPK)
