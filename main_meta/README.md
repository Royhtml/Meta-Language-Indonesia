# Meta Language v1.0

<div align="center">

![Meta Language](https://img.shields.io/badge/Meta-Language-blue?style=for-the-badge)
![Version](https://img.shields.io/badge/version-1.0-green?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.6+-yellow?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-red?style=for-the-badge)

**Bahasa Pemrograman dengan Sintaks Indonesia, Kekuatan Python**

[Dokumentasi](#-daftar-isi) • [Instalasi](#-instalasi) • [Mulai Cepat](#-mulai-cepat) • [Sintaks](#-sintaks-lengkap) • [Contoh](#-contoh-program)

</div>

---

<img src="icon.png" alt="Meta Language">

## 📋 Daftar Isi

- [Tentang Meta Language](#-tentang-meta-language)
- [Instalasi](#-instalasi)
- [Mulai Cepat](#-mulai-cepat)
- [Cara Penggunaan](#-cara-penggunaan)
- [Sintaks Lengkap](#-sintaks-lengkap)
  - [Input dan Output](#input-dan-output)
  - [Variabel dan Tipe Data](#variabel-dan-tipe-data)
  - [Konversi Tipe Data](#konversi-tipe-data)
  - [Operasi Matematika](#operasi-matematika)
  - [Percabangan (Kondisi)](#percabangan-kondisi)
  - [Perulangan (Loop)](#perulangan-loop)
  - [Fungsi](#fungsi)
  - [List (Daftar)](#list-daftar)
  - [Dictionary](#dictionary)
  - [String](#string)
  - [Kelas dan OOP](#kelas-dan-oop)
  - [Penanganan Error](#penanganan-error)
  - [Boolean dan Operator Logika](#boolean-dan-operator-logika)
- [Contoh Program](#-contoh-program)
- [Mode Interaktif (REPL)](#-mode-interaktif-repl)
- [Debug Mode](#-debug-mode)
- [Error Handling](#-error-handling)
- [Struktur Proyek](#-struktur-proyek)
- [FAQ](#-faq)
- [Kontribusi](#-kontribusi)
- [Lisensi](#-lisensi)
- [Kontak](#-kontak)

---

## 🌟 Tentang Meta Language

Meta Language adalah bahasa pemrograman yang dirancang khusus untuk penutur Bahasa Indonesia. Dengan sintaks yang sepenuhnya menggunakan kata kunci Bahasa Indonesia, Meta Language memudahkan siapa saja untuk belajar pemrograman tanpa harus menghafal kata kunci bahasa Inggris.

### ✨ Fitur Utama

- **Sintaks Bahasa Indonesia** - Semua kata kunci menggunakan Bahasa Indonesia
- **Berbasis Python** - Dikonversi dan dijalankan sebagai kode Python murni
- **Error Message Berbahasa Indonesia** - Pesan error yang mudah dipahami
- **REPL Interaktif** - Mode interaktif untuk eksperimen cepat
- **Debug Mode** - Lihat hasil konversi ke Python
- **Multi-platform** - Berjalan di Windows, macOS, dan Linux

### 📊 Perbandingan Sintaks

| Python | Meta Language |
|--------|---------------|
| `print("Hello")` | `meta("Hello")` |
| `input("Nama: ")` | `masukan("Nama: ")` |
| `if x > 5:` | `jika x > 5 maka:` |
| `for i in range(5):` | `untuk i dalam rentang(5):` |
| `def fungsi():` | `modul fungsi():` |
| `return x` | `kembalikan x` |
| `True / False` | `benar / salah` |

---

## 💻 Instalasi

### Prasyarat

- Python 3.6 atau lebih tinggi
- pip (Python package installer)

### Langkah Instalasi

#### 1. Clone Repository

```bash
git clone https://github.com/username/meta-language.git
cd meta-language
```

#### 2. Install Dependencies

Meta Language tidak memerlukan dependensi eksternal, hanya menggunakan library bawaan Python.

#### 3. Setup (Opsional - Windows)

Untuk menambahkan Meta Language ke PATH:

```powershell
# PowerShell (Administrator)
$metaPath = "C:\path\to\meta-language"
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";$metaPath", "User")
```

#### 4. Verifikasi Instalasi

```bash
python meta.py --version
# Output: Meta Language v1.0
```

### Instalasi Global (Opsional)

**Linux/macOS:**
```bash
chmod +x meta.py
sudo ln -s $(pwd)/meta.py /usr/local/bin/meta
```

**Windows:**
Buat file `meta.bat` di direktori yang ada di PATH:
```batch
@echo off
python "C:\path\to\meta-language\meta.py" %*
```

---

## 🚀 Mulai Cepat

### Program Pertama Anda

Buat file bernama `halo.meta`:

```python
-- Program Halo Dunia
-- File: halo.meta

meta("╔══════════════════════════════════════╗")
meta("║     HALO DUNIA DARI META LANGUAGE    ║")
meta("╚══════════════════════════════════════╝")
meta("")

nama = masukan("Siapa nama Anda? ")
meta(f"Halo, {nama}! Selamat datang di Meta Language!")
```

Jalankan program:

```bash
meta halo.meta
```

### Membuat Program Kalkulator Sederhana

Buat file `kalkulator.meta`:

```python
-- Kalkulator Sederhana
-- File: kalkulator.meta

meta("=== KALKULATOR SEDERHANA ===")
meta("")

a = desimal(masukan("Masukkan angka pertama: "))
b = desimal(masukan("Masukkan angka kedua: "))
operator = masukan("Operator (+, -, *, /): ")

jika operator == "+" maka:
    hasil = a + b
atau jika operator == "-" maka:
    hasil = a - b
atau jika operator == "*" maka:
    hasil = a * b
atau jika operator == "/" maka:
    jika b != 0 maka:
        hasil = a / b
    selain itu:
        meta("Error: Tidak bisa membagi dengan nol!")
        hasil = kosong
selain itu:
    meta("Operator tidak dikenal!")
    hasil = kosong

jika hasil != kosong maka:
    meta(f"Hasil: {a} {operator} {b} = {hasil}")
```

---

## 📖 Cara Penggunaan

### Command Line Interface

```bash
meta                               # Menjalankan main.meta (auto-detect)
meta <file.meta> [argumen...]      # Menjalankan program dengan argumen
meta --debug [file.meta]           # Menjalankan dengan debug mode
meta --repl                        # Mode interaktif (REPL)
meta --help                        # Menampilkan bantuan
meta --version                     # Menampilkan versi
```

### Argumen Program

Anda dapat mengirim argumen ke program Meta:

```python
-- program.meta
import sys

meta("Argumen yang diterima:")
untuk i, arg dalam enumerasi(sys.argv):
    meta(f"  {i}: {arg}")
```

Jalankan dengan:
```bash
meta program.meta halo dunia 123
```

### Komentar

```python
-- Ini adalah komentar satu baris
meta("Hello")  -- Komentar setelah kode

--[[
    Ini adalah komentar
    multi-baris
--]]
```

---

## 📚 Sintaks Lengkap

### Input dan Output

| Fungsi Meta | Fungsi Python | Deskripsi | Contoh |
|-------------|---------------|-----------|--------|
| `meta(teks)` | `print()` | Menampilkan teks ke layar | `meta("Hello World")` |
| `cetak(teks)` | `print()` | Alias untuk meta() | `cetak("Hello")` |
| `tulis(teks)` | `print()` | Alias untuk meta() | `tulis("Hello")` |
| `masukan(prompt)` | `input()` | Membaca input dari user | `nama = masukan("Nama: ")` |
| `baca(prompt)` | `input()` | Alias untuk masukan() | `data = baca("Data: ")` |

**Contoh:**
```python
-- Output dengan format
nama = "Budi"
umur = 25
meta(f"Nama: {nama}, Umur: {umur}")
meta("Nama: {}, Umur: {}".format(nama, umur))

-- Input dengan tipe data
nama = masukan("Masukkan nama: ")
umur = bilangan(masukan("Masukkan umur: "))
```

### Variabel dan Tipe Data

```python
-- Tipe data dasar
teks_var = "Ini string"
angka_var = 42
desimal_var = 3.14
boolean_var = benar
boolean_salah = salah
kosong_var = kosong

-- Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 100
```

### Konversi Tipe Data

| Fungsi Meta | Fungsi Python | Deskripsi |
|-------------|---------------|-----------|
| `teks(nilai)` | `str()` | Konversi ke string |
| `bilangan(nilai)` | `int()` | Konversi ke integer |
| `angka(nilai)` | `int()` | Alias untuk bilangan() |
| `desimal(nilai)` | `float()` | Konversi ke float |
| `list(nilai)` | `list()` | Konversi ke list |
| `dictionary(nilai)` | `dict()` | Konversi ke dictionary |
| `tuple(nilai)` | `tuple()` | Konversi ke tuple |
| `set(nilai)` | `set()` | Konversi ke set |
| `benar_salah(nilai)` | `bool()` | Konversi ke boolean |

### Operasi Matematika

| Fungsi Meta | Fungsi Python | Deskripsi |
|-------------|---------------|-----------|
| `akar(x)` | `math.sqrt()` | Akar kuadrat |
| `absolut(x)` | `abs()` | Nilai absolut |
| `bulatkan(x)` | `round()` | Pembulatan |
| `pangkat(x, y)` | `pow()` | Pangkat |
| `maksimal(...)` | `max()` | Nilai maksimum |
| `minimal(...)` | `min()` | Nilai minimum |
| `jumlah(...)` | `sum()` | Jumlah semua nilai |

**Contoh:**
```python
import matematika as mt  -- Import math module

x = 16
y = -5

meta(f"Akar dari {x}: {akar(x)}")           -- 4.0
meta(f"Absolut dari {y}: {absolut(y)}")     -- 5
meta(f"Pangkat 2^3: {pangkat(2, 3)}")       -- 8
meta(f"Maksimal: {maksimal(1, 5, 3, 9)}")   -- 9
```

### Percabangan (Kondisi)

```python
-- If-elif-else
nilai = 85

jika nilai >= 90 maka:
    meta("Grade: A")
atau jika nilai >= 80 maka:
    meta("Grade: B")
atau jika nilai >= 70 maka:
    meta("Grade: C")
atau jika nilai >= 60 maka:
    meta("Grade: D")
selain itu:
    meta("Grade: E")

-- Nested if
jika nilai >= 60 maka:
    meta("Anda lulus!")
    jika nilai >= 90 maka:
        meta("Dengan pujian!")
selain itu:
    meta("Anda perlu belajar lagi.")
```

### Perulangan (Loop)

#### For Loop

```python
-- Perulangan dengan rentang
untuk i dalam rentang(5):
    meta(f"Iterasi ke-{i}")  -- 0, 1, 2, 3, 4

-- Rentang dengan start, stop, step
untuk i dalam rentang(1, 10, 2):
    meta(i)  -- 1, 3, 5, 7, 9

-- Perulangan list
buah = ["apel", "jeruk", "mangga"]
untuk item dalam buah:
    meta(f"Saya suka {item}")

-- Dengan index
untuk i, item dalam enumerasi(buah):
    meta(f"{i}: {item}")
```

#### While Loop

```python
-- Perulangan while
hitung = 1
selama hitung <= 5:
    meta(f"Hitung: {hitung}")
    hitung = hitung + 1

-- Break dan Continue
i = 0
selama benar:
    i = i + 1
    jika i == 3 maka:
        lanjut  -- Skip 3
    jika i > 5 maka:
        berhenti  -- Keluar loop
    meta(i)
```

### Fungsi

```python
-- Definisi fungsi tanpa parameter
modul sapa():
    meta("Halo dari Meta Language!")

-- Definisi fungsi dengan parameter
modul tambah(a, b):
    kembalikan a + b

-- Fungsi dengan nilai default
modul sapa_person(nama, salam="Halo"):
    kembalikan f"{salam}, {nama}!"

-- Memanggil fungsi
sapa()
hasil = tambah(5, 3)
meta(sapa_person("Budi"))
meta(sapa_person("Ani", "Selamat pagi"))

-- Fungsi rekursif
modul faktorial(n):
    jika n <= 1 maka:
        kembalikan 1
    selain itu:
        kembalikan n * faktorial(n - 1)

meta(faktorial(5))  -- 120
```

### List (Daftar)

```python
-- Membuat list
buah = ["apel", "jeruk", "mangga"]
angka = [1, 2, 3, 4, 5]
campuran = [1, "dua", 3.0, benar]

-- Method List
buah.tambah("anggur")           -- append()
buah.masukkan(1, "pisang")      -- insert(index, item)
buah.hapus("jeruk")             -- remove()
item = buah.pop()               -- pop()
item_tertentu = buah.pop(0)     -- pop(index)
buah.bersihkan()                -- clear()
buah.perluas(["kiwi", "melon"]) -- extend()

-- Akses dan manipulasi
meta(buah[0])                   -- Akses index
meta(buah[-1])                  -- Index dari belakang
meta(buah[1:3])                 -- Slicing
panjang = buah.panjang()        -- len()

-- Sorting dan reversing
buah.urutkan()                  -- sort()
buah.balik()                    -- reverse()
salinan = buah.salin()          -- copy()

-- List Comprehension
kuadrat = [x*x untuk x dalam rentang(5)]
genap = [x untuk x dalam rentang(10) jika x % 2 == 0]
```

### Dictionary

```python
-- Membuat dictionary
siswa = {
    "nama": "Budi",
    "umur": 20,
    "nilai": 85
}

-- Akses dan manipulasi
meta(siswa["nama"])             -- Akses langsung
meta(siswa.ambil("alamat", "Tidak ada"))  -- get() dengan default

-- Menambah/mengubah
siswa["alamat"] = "Jakarta"
siswa.perbarui({"umur": 21, "kelas": "A"})

-- Method dictionary
kunci = siswa.kunci()           -- keys()
nilai = siswa.nilai()           -- values()
item = siswa.item()             -- items()
siswa.popitem()                 -- popitem()

-- Iterasi dictionary
untuk k, v dalam siswa.item():
    meta(f"{k}: {v}")
```

### String

| Method Meta | Method Python | Deskripsi |
|-------------|---------------|-----------|
| `string.jadikan_besar()` | `.upper()` | Huruf besar semua |
| `string.jadikan_kecil()` | `.lower()` | Huruf kecil semua |
| `string.jadikan_kapital()` | `.capitalize()` | Kapital awal |
| `string.jadikan_judul()` | `.title()` | Format judul |
| `string.ganti(a, b)` | `.replace()` | Mengganti teks |
| `string.pisah(sep)` | `.split()` | Memisah string |
| `string.gabung(list)` | `.join()` | Menggabung list |
| `string.strip()` | `.strip()` | Hapus spasi |
| `string.cari(teks)` | `.find()` | Mencari teks |
| `string.hitung(teks)` | `.count()` | Menghitung kemunculan |
| `string.mulai_dengan(teks)` | `.startswith()` | Cek awalan |
| `string.akhir_dengan(teks)` | `.endswith()` | Cek akhiran |

**Contoh:**
```python
teks = "  belajar meta language  "

meta(teks.jadikan_besar())      -- "  BELAJAR META LANGUAGE  "
meta(teks.jadikan_judul())      -- "  Belajar Meta Language  "
meta(teks.strip())              -- "belajar meta language"

kata = teks.strip().pisah(" ")
meta(kata)                      -- ["belajar", "meta", "language"]

gabung = "-".gabung(kata)
meta(gabung)                    -- "belajar-meta-language"
```

### Kelas dan OOP

```python
-- Definisi kelas
kelas Orang:
    modul __init__(diri, nama, umur):
        diri.nama = nama
        diri.umur = umur
    
    modul perkenalan(diri):
        kembalikan f"Nama saya {diri.nama}, umur {diri.umur} tahun"
    
    modul ulang_tahun(diri):
        diri.umur = diri.umur + 1
        meta(f"Selamat ulang tahun {diri.nama}!")

-- Inheritance
kelas Siswa(Orang):
    modul __init__(diri, nama, umur, kelas):
        super().__init__(nama, umur)
        diri.kelas = kelas
    
    modul perkenalan(diri):
        kembalikan f"{super().perkenalan()}, kelas {diri.kelas}"

-- Menggunakan kelas
orang1 = Orang("Budi", 25)
meta(orang1.perkenalan())
orang1.ulang_tahun()

siswa1 = Siswa("Ani", 16, "X IPA 1")
meta(siswa1.perkenalan())
```

### Penanganan Error

```python
-- Try-except-finally
coba:
    x = bilangan(masukan("Masukkan angka: "))
    y = bilangan(masukan("Masukkan pembagi: "))
    hasil = x / y
    meta(f"Hasil: {hasil}")
kecuali ZeroDivisionError:
    meta("Error: Tidak bisa membagi dengan nol!")
kecuali ValueError:
    meta("Error: Input harus berupa angka!")
kecuali Exception sebagai e:
    meta(f"Error tidak dikenal: {e}")
akhirnya:
    meta("Program selesai.")

-- Raise exception
modul validasi_umur(umur):
    jika umur < 0 maka:
        naikkan ValueError("Umur tidak boleh negatif!")
    jika umur > 150 maka:
        naikkan ValueError("Umur terlalu besar!")
    kembalikan benar

coba:
    validasi_umur(-5)
kecuali ValueError sebagai e:
    meta(f"Validasi gagal: {e}")
```

### Boolean dan Operator Logika

```python
-- Nilai boolean
aktif = benar
selesai = salah
data = kosong

-- Operator logika
jika aktif dan bukan selesai maka:
    meta("Sedang berjalan")

jika data adalah kosong maka:
    meta("Data kosong")

-- Operator perbandingan
x = 10
y = 5

jika x > y dan x != 0 maka:
    meta("x lebih besar dari y")

-- Operator keanggotaan
buah = ["apel", "jeruk"]
jika "apel" di buah maka:
    meta("Apel ada dalam list")
```

---

## 📝 Contoh Program

### 1. Program Tebak Angka

```python
-- Game Tebak Angka
-- File: tebak.meta

import random

modul main():
    meta("╔══════════════════════════════════════╗")
    meta("║        GAME TEBAK ANGKA              ║")
    meta("╚══════════════════════════════════════╝")
    meta("")
    
    angka_rahasia = random.randint(1, 100)
    percobaan = 0
    maks_percobaan = 7
    
    meta(f"Saya memikirkan angka antara 1-100")
    meta(f"Anda punya {maks_percobaan} kesempatan")
    meta("")
    
    selama percobaan < maks_percobaan:
        sisa = maks_percobaan - percobaan
        tebakan = bilangan(masukan(f"Tebakan Anda (sisa {sisa}): "))
        percobaan = percobaan + 1
        
        jika tebakan == angka_rahasia maka:
            meta(f"🎉 SELAMAT! Anda benar dalam {percobaan} tebakan!")
            kembalikan
        atau jika tebakan < angka_rahasia maka:
            meta("📈 Terlalu kecil! Coba angka yang lebih besar.")
        selain itu:
            meta("📉 Terlalu besar! Coba angka yang lebih kecil.")
        
        meta("")
    
    meta(f"😢 Game Over! Angkanya adalah {angka_rahasia}")

-- Jalankan game
jika __name__ == "__main__":
    main()
```

### 2. Program Manajemen Kontak

```python
-- Aplikasi Manajemen Kontak
-- File: kontak.meta

kontak_list = []

modul tambah_kontak():
    meta("\n--- TAMBAH KONTAK ---")
    nama = masukan("Nama: ")
    telepon = masukan("Telepon: ")
    email = masukan("Email: ")
    
    kontak = {
        "nama": nama,
        "telepon": telepon,
        "email": email
    }
    kontak_list.tambah(kontak)
    meta(f"✅ Kontak {nama} berhasil ditambahkan!")

modul lihat_kontak():
    meta("\n--- DAFTAR KONTAK ---")
    jika kontak_list.panjang() == 0 maka:
        meta("Belum ada kontak.")
        kembalikan
    
    untuk i, kontak dalam enumerasi(kontak_list):
        meta(f"\nKontak #{i+1}")
        meta(f"  Nama    : {kontak['nama']}")
        meta(f"  Telepon : {kontak['telepon']}")
        meta(f"  Email   : {kontak['email']}")

modul cari_kontak():
    meta("\n--- CARI KONTAK ---")
    keyword = masukan("Masukkan nama: ").jadikan_kecil()
    
    ditemukan = []
    untuk kontak dalam kontak_list:
        jika keyword di kontak["nama"].jadikan_kecil() maka:
            ditemukan.tambah(kontak)
    
    jika ditemukan.panjang() == 0 maka:
        meta("❌ Tidak ada kontak yang ditemukan.")
    selain itu:
        meta(f"\n📋 Ditemukan {ditemukan.panjang()} kontak:")
        untuk kontak dalam ditemukan:
            meta(f"  • {kontak['nama']} - {kontak['telepon']}")

modul hapus_kontak():
    meta("\n--- HAPUS KONTAK ---")
    nama = masukan("Nama kontak yang akan dihapus: ")
    
    untuk i, kontak dalam enumerasi(kontak_list):
        jika kontak["nama"].jadikan_kecil() == nama.jadikan_kecil() maka:
            kontak_list.pop(i)
            meta(f"✅ Kontak {nama} berhasil dihapus!")
            kembalikan
    
    meta(f"❌ Kontak {nama} tidak ditemukan.")

modul menu():
    meta("\n" + "="*40)
    meta("       APLIKASI MANAJEMEN KONTAK")
    meta("="*40)
    meta("1. Lihat Kontak")
    meta("2. Tambah Kontak")
    meta("3. Cari Kontak")
    meta("4. Hapus Kontak")
    meta("5. Keluar")
    meta("="*40)

modul main():
    meta("╔══════════════════════════════════════╗")
    meta("║    APLIKASI MANAJEMEN KONTAK v1.0   ║")
    meta("╚══════════════════════════════════════╝")
    
    selama benar:
        menu()
        pilihan = masukan("Pilih menu (1-5): ")
        
        jika pilihan == "1" maka:
            lihat_kontak()
        atau jika pilihan == "2" maka:
            tambah_kontak()
        atau jika pilihan == "3" maka:
            cari_kontak()
        atau jika pilihan == "4" maka:
            hapus_kontak()
        atau jika pilihan == "5" maka:
            meta("\n👋 Terima kasih! Sampai jumpa!")
            berhenti
        selain itu:
            meta("❌ Pilihan tidak valid!")

jika __name__ == "__main__":
    main()
```

### 3. Program Kalkulator BMI

```python
-- Kalkulator BMI (Body Mass Index)
-- File: bmi.meta

modul hitung_bmi(berat, tinggi):
    -- tinggi dalam meter
    kembalikan berat / (tinggi * tinggi)

modul kategori_bmi(bmi):
    jika bmi < 18.5 maka:
        kembalikan "Kurus"
    atau jika bmi < 25 maka:
        kembalikan "Normal (Ideal)"
    atau jika bmi < 30 maka:
        kembalikan "Kelebihan Berat Badan"
    selain itu:
        kembalikan "Obesitas"

modul main():
    meta("╔══════════════════════════════════════╗")
    meta("║         KALKULATOR BMI               ║")
    meta("║    Body Mass Index Calculator        ║")
    meta("╚══════════════════════════════════════╝")
    meta("")
    
    nama = masukan("Nama Anda: ")
    
    coba:
        berat = desimal(masukan("Berat badan (kg): "))
        tinggi_cm = desimal(masukan("Tinggi badan (cm): "))
        
        -- Konversi cm ke meter
        tinggi = tinggi_cm / 100
        
        jika berat <= 0 atau tinggi <= 0 maka:
            naikkan ValueError("Berat dan tinggi harus positif!")
        
        bmi = hitung_bmi(berat, tinggi)
        kategori = kategori_bmi(bmi)
        
        meta("")
        meta("="*40)
        meta(f"📊 HASIL PERHITUNGAN BMI - {nama}")
        meta("="*40)
        meta(f"Berat Badan  : {berat} kg")
        meta(f"Tinggi Badan : {tinggi_cm} cm")
        meta(f"Nilai BMI    : {bulatkan(bmi, 1)}")
        meta(f"Kategori     : {kategori}")
        meta("="*40)
        
        -- Saran berdasarkan kategori
        meta("")
        meta("💡 SARAN:")
        jika bmi < 18.5 maka:
            meta("   • Tingkatkan asupan kalori sehat")
            meta("   • Lakukan olahraga untuk membangun otot")
            meta("   • Konsultasikan dengan ahli gizi")
        atau jika bmi < 25 maka:
            meta("   • Pertahankan pola makan sehat")
            meta("   • Rutin berolahraga")
            meta("   • Jaga keseimbangan nutrisi")
        atau jika bmi < 30 maka:
            meta("   • Kurangi makanan tinggi kalori")
            meta("   • Tingkatkan aktivitas fisik")
            meta("   • Perbanyak sayur dan buah")
        selain itu:
            meta("   • Konsultasikan dengan dokter")
            meta("   • Atur pola makan dengan ahli gizi")
            meta("   • Mulai program penurunan berat badan")
        
    kecuali ValueError sebagai e:
        meta(f"❌ Error: {e}")
    kecuali Exception sebagai e:
        meta(f"❌ Terjadi kesalahan: {e}")

jika __name__ == "__main__":
    main()
```

---

## 🔄 Mode Interaktif (REPL)

Meta Language menyediakan mode REPL (Read-Eval-Print Loop) untuk eksperimen cepat.

### Memulai REPL

```bash
meta --repl
```

### Menggunakan REPL

```python
🔷 meta> meta("Hello World!")
Hello World!

🔷 meta> x = 10
🔷 meta> y = 20
🔷 meta> meta(f"Hasil: {x + y}")
Hasil: 30

🔷 meta> untuk i dalam rentang(3):
...      meta(f"Angka {i}")
... 
Angka 0
Angka 1
Angka 2

🔷 meta> --debug
🔧 Debug mode: AKTIF

🔶 meta (debug)> meta("Test")
Test
```

### Fitur REPL

- **Multi-line input** - Akhiri baris dengan `:` untuk input multi-baris
- **Toggle debug mode** - Ketik `--debug` untuk melihat hasil konversi
- **History** - Gunakan tombol panah atas/bawah
- **Auto-complete** - Tekan Tab (jika didukung terminal)

### Perintah Khusus REPL

| Perintah | Fungsi |
|----------|--------|
| `keluar` / `exit` / `quit` | Keluar dari REPL |
| `--debug` | Toggle debug mode |
| `Ctrl+C` | Keluar paksa |
| `Ctrl+D` | EOF (End of File) |

---

## 🐛 Debug Mode

Debug mode memungkinkan Anda melihat kode Python hasil konversi dari kode Meta.

### Mengaktifkan Debug Mode

```bash
# Debug file tertentu
meta --debug program.meta

# Debug main.meta
meta --debug
```

### Output Debug Mode

```
══════════════════════════════════════════════════════════════════════════════════════
📜 DEBUG MODE - HASIL KONVERSI META KE PYTHON
📁 File: program.meta
══════════════════════════════════════════════════════════════════════════════════════

  Baris   |            Meta Language             |                  Python
────────────────────────────────────────────────────────────────────────────────────
    1     | meta("Hello World")                  | print("Hello World")
    2     | nama = masukan("Nama: ")             | nama = input("Nama: ")
    3     | jika nama != "" maka:                | if nama != "":
    4     |     meta(f"Halo {nama}")             |     print(f"Halo {nama}")

══════════════════════════════════════════════════════════════════════════════════════
📝 KODE PYTHON LENGKAP:
══════════════════════════════════════════════════════════════════════════════════════
# -*- coding: utf-8 -*-
# Meta Language Generated Code
print("Hello World")
nama = input("Nama: ")
if nama != "":
    print(f"Halo {nama}")
══════════════════════════════════════════════════════════════════════════════════════
```

### Debug di REPL

```python
🔷 meta> --debug
🔧 Debug mode: AKTIF

🔶 meta (debug)> x = 5
# Generated Python:
x = 5

🔶 meta (debug)> meta(x * 2)
# Generated Python:
print(x * 2)
10
```

---

## ❌ Error Handling

Meta Language menyediakan pesan error dalam Bahasa Indonesia yang mudah dipahami.

### Jenis-jenis Error

| Error Type | Deskripsi | Contoh |
|------------|-----------|--------|
| `MetaSyntaxError` | Kesalahan sintaks | Kurung tidak berpasangan |
| `MetaNameError` | Variabel tidak dikenal | Nama variabel salah ketik |
| `MetaTypeError` | Tipe data salah | Operasi pada tipe tidak cocok |
| `MetaAttributeError` | Method tidak ada | Method tidak tersedia |
| `MetaZeroDivisionError` | Pembagian nol | x / 0 |
| `MetaRuntimeError` | Error runtime | Error umum saat eksekusi |

### Contoh Pesan Error

```python
-- NameError
meta(nama_tidak_ada)
-- Output:
-- ❌ ERROR - Meta Language
-- 📁 File: program.meta
-- 📛 Tipe Error: NameError
-- 📍 Lokasi: Baris 5
-- 💬 Pesan: Variabel atau fungsi 'nama_tidak_ada' tidak didefinisikan

-- AttributeError
list = [1, 2, 3]
list.panjang  -- Lupa kurung
-- Output:
-- ❌ ERROR - Meta Language
-- 📛 Tipe Error: AttributeError
-- 💬 Pesan: Objek tidak memiliki method 'panjang'
-- 💡 SARAN PERBAIKAN:
--    Method '.panjang()' digunakan untuk mendapatkan panjang list/string
--    ✅ Benar: buah.panjang()
--    ❌ Salah: buah.panjang (tanpa kurung)

-- ZeroDivisionError
x = 10 / 0
-- Output:
-- ❌ ERROR - Meta Language
-- 📛 Tipe Error: ZeroDivisionError
-- 💬 Pesan: Tidak bisa membagi dengan nol
-- 💡 SARAN PERBAIKAN:
--    Tambahkan pengecekan sebelum pembagian:
--    jika penyebut != 0 maka:
--        hasil = pembilang / penyebut
```

### Tips Debugging

1. **Gunakan Debug Mode**
   ```bash
   meta --debug program.meta
   ```

2. **Periksa Baris yang Disebutkan**
   - Error message selalu menyertakan nomor baris

3. **Cek Tanda Kurung**
   - Pastikan `()`, `[]`, `{}` berpasangan

4. **Periksa Indentasi**
   - Gunakan spasi atau tab secara konsisten

5. **Validasi Input**
   - Selalu konversi input ke tipe yang sesuai

---

## 📁 Struktur Proyek

```
meta-language/
├── meta.py                 # Interpreter utama
├── README.md               # Dokumentasi (file ini)
├── LICENSE                 # Lisensi MIT
├── lib/
│   └── meta_icon/
│       └── icon.ico        # Icon untuk Windows
├── examples/               # Contoh program
│   ├── halo.meta
│   ├── kalkulator.meta
│   ├── tebak.meta
│   ├── kontak.meta
│   └── bmi.meta
└── tests/                  # Unit tests
    └── test_meta.py
```

---

## ❓ FAQ

### Q: Apakah Meta Language bisa menjalankan kode Python langsung?

**A:** Ya, Meta Language adalah superset dari Python. Anda bisa mencampur sintaks Python dan Meta dalam satu file. Namun, disarankan untuk konsisten menggunakan sintaks Meta.

```python
-- Ini valid
meta("Hello")  -- Sintaks Meta
print("World")  -- Sintaks Python
```

### Q: Bagaimana cara menginstall package Python?

**A:** Gunakan sintaks import standar Python:

```python
import requests
import numpy sebagai np
dari datetime import datetime

-- Gunakan package
respons = requests.get("https://api.example.com")
data = respons.json()
```

### Q: Apakah bisa membuat aplikasi GUI?

**A:** Ya, Anda bisa menggunakan library GUI Python seperti tkinter, PyQt, atau Kivy:

```python
dari tkinter import *

jendela = Tk()
jendela.title("Aplikasi Meta")
jendela.geometry("300x200")

label = Label(jendela, teks="Halo dari Meta!")
label.pack()

jendela.mainloop()
```

### Q: Bagaimana cara membuat web server?

**A:** Gunakan framework seperti Flask atau FastAPI:

```python
dari flask import Flask

aplikasi = Flask(__name__)

@aplikasi.route('/')
modul home():
    kembalikan "Halo dari Meta Language!"

jika __name__ == "__main__":
    aplikasi.run()
```

### Q: Apakah performa Meta Language sama dengan Python?

**A:** Meta Language dikonversi menjadi Python murni sebelum dieksekusi, sehingga performanya sama dengan Python. Overhead konversi hanya terjadi sekali di awal.

### Q: Bagaimana cara debugging yang efektif?

**A:** 
1. Gunakan `meta --debug` untuk melihat kode Python hasil konversi
2. Tambahkan `meta()` untuk print debugging
3. Gunakan try-except untuk menangkap error
4. Periksa pesan error yang informatif

---

## 🤝 Kontribusi

Kami sangat menghargai kontribusi dari komunitas!

### Cara Berkontribusi

1. **Fork** repository ini
2. **Clone** repository hasil fork
3. **Buat branch** baru untuk fitur/perbaikan
4. **Commit** perubahan Anda
5. **Push** ke branch Anda
6. **Buat Pull Request**

### Area Kontribusi

- 📝 Menambah aturan konversi baru
- 🐛 Memperbaiki bug
- 📚 Menambah contoh program
- 🌐 Menerjemahkan error message
- 🎨 Memperbaiki UI/UX
- 📖 Memperbaiki dokumentasi

### Panduan Kontribusi

```python
-- Contoh menambah aturan konversi baru
-- Di dalam __init__ MetaInterpreter:

self.konversi_rules.extend([
    -- Keyword baru
    (r'\bkata_kunci_baru\b', 'python_keyword'),
    
    -- Fungsi baru  
    (r'\bfungsi_baru\s*\(', 'new_function('),
])
```

---

## 📄 Lisensi

MIT License

Copyright (c) 2026 Dwi Bakti N Dev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 📞 Kontak

**Dwi Bakti N Dev**

- 🌐 Website: [https://portofolio-dwi-bakti-n-dev-liard.vercel.app/](https://portofolio-dwi-bakti-n-dev-liard.vercel.app/)
- 📧 Email: Dwibakti76@gmail.com
- 💻 GitHub: [github.com/dwibakti](https://github.com/royhtml)

### Laporkan Bug atau Request Fitur

Silakan buat issue di GitHub repository:
[https://github.com/dwibakti/meta-language/issues](https://github.com/royhtml)

---

<div align="center">

**Dibuat dengan ❤️ untuk Komunitas Pemrograman Indonesia**

⭐ Star repository ini jika bermanfaat!

[⬆ Kembali ke Atas](#meta-language-v10)

</div>