# Meta Language Indonesia

<p align="center">
  <img src="https://github.com/Royhtml/Meta-Language-Indonesia/blob/main/icons/icon.png?raw=true" width="180">
</p>

<h1 align="center">Meta Language Indonesia</h1>

<p align="center">
  <img src="https://img.shields.io/badge/VS%20Code-1.60.0+-blue.svg?logo=visual-studio-code&logoColor=white" alt="VS Code Extension">
  <img src="https://img.shields.io/badge/version-1.0.0-green.svg" alt="Version">
  <img src="https://img.shields.io/badge/license-MIT-orange.svg" alt="License">
  <img src="https://img.shields.io/badge/Python-3.8+-yellow.svg?logo=python&logoColor=white" alt="Python Version">
</p>

<p align="center">
  <b>Compiler Bahasa Pemrograman berbasis Bahasa Indonesia yang mudah dipahami dan digunakan.</b>
</p>

<p align="center">
  <a href="https://marketplace.visualstudio.com/items?itemName=RoyHtml.meta-lang">
    <img src="https://img.shields.io/badge/Install_Extension-Visual_Studio_Code-blue?style=for-the-badge&logo=visual-studio-code&logoColor=white">
  </a>
  <a href="https://pypi.org/project/meta-language-indonesia/">
    <img src="https://img.shields.io/badge/Install_Package-PyPI-blue?style=for-the-badge&logo=pypi&logoColor=white">
  </a>
  <a href="https://github.com/Royhtml/Meta-Language-Indonesia">
    <img src="https://img.shields.io/badge/View_Repo-GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
  </a>
</p>

## 📖 Tentang Meta Language

**Meta Language** adalah bahasa pemrograman yang menggunakan sintaks dalam **Bahasa Indonesia**, dirancang untuk memudahkan pembelajaran pemrograman bagi penutur bahasa Indonesia. Ekstensi ini memberikan dukungan penuh untuk bahasa Meta di Visual Studio Code.

## ✨ Fitur Utama

### 🎨 **Sintaks Highlighting & Warna Kode**
- Pewarnaan sintaks yang jelas dan intuitif untuk semua keyword Bahasa Indonesia
- Membedakan antara fungsi, variabel, operator, dan keyword
- Highlight untuk string, angka, komentar, dan tipe data

### 📝 **Auto-Completion Cerdas**
- Saran kode otomatis saat mengetik keyword Bahasa Indonesia
- Auto-complete untuk fungsi bawaan seperti `cetak()`, `masukan()`, `rentang()`
- Saran untuk method seperti `.tambah()`, `.pisah()`, `.kunci()`

### 🔄 **Konversi Real-time ke Python**
- Terjemahan otomatis kode Meta ke Python
- Preview hasil konversi langsung di editor
- Dukung semua fitur: list comprehension, dictionary comprehension, OOP

### 🏷️ **Icon & File Association**
- Icon khusus untuk file dengan ekstensi `.meta`
- Pengenalan otomatis file Meta Language
- Integration dengan file explorer VS Code

### 📚 **Code Snippets Siap Pakai**
- Template fungsi: ketik `modul` + `Tab`
- Template percabangan: ketik `jika` + `Tab`
- Template perulangan: `untuk` atau `selama` + `Tab`
- Template class: `kelas` + `Tab`

### 🔍 **Error Highlighting**
- Mendeteksi kesalahan sintaks dasar
- Memberi tahu keyword yang tidak dikenal
- Saran perbaikan untuk keyword yang salah eja

### 📩 **Compile Meta To Exe**

**1. Language Meta**
```meta
meta -m pip install meta-language-indonesia
```
**Running**
```meta
meta_compile
```

**2. Language python**
```meta
pip install meta-language-indonesia
```
**Running**
```meta
meta_compile
```

### 🚀 **Fitur Lengkap Lainnya**

#### **Dukungan List Comprehension**
```meta
[kuadrat untuk i dalam range(10) jika i % 2 == 0]
```

#### **Dukungan Dictionary Comprehension**
```meta
{i: kuadrat untuk i dalam range(5)}
```

#### **Konversi Tipe Data**
- `teks()` → `str()`
- `bilangan()` / `angka()` → `int()`
- `desimal()` → `float()`
- `benar_salah()` → `bool()`

#### **Fungsi Matematika**
- `akar()` → `math.sqrt()`
- `pangkat()` → `pow()`
- `maksimal()` / `minimal()` → `max()` / `min()`
- `jumlah()` → `sum()`

#### **Method Lengkap untuk Tipe Data**

**List Methods:**
- `.tambah()` → `.append()`
- `.masukkan()` → `.insert()`
- `.hapus()` → `.remove()`
- `.bersihkan()` → `.clear()`
- `.urutkan()` → `.sort()`
- `.balik()` → `.reverse()`

**String Methods:**
- `.jadikan_besar()` → `.upper()`
- `.jadikan_kecil()` → `.lower()`
- `.ganti()` → `.replace()`
- `.pisah()` → `.split()`
- `.gabung()` → `.join()`
- `.cari()` → `.find()`

**Dictionary Methods:**
- `.ambil()` → `.get()`
- `.kunci()` → `.keys()`
- `.nilai()` → `.values()`
- `.item()` → `.items()`

#### **Exception Handling**
```meta
coba:
    hasil = 10 / 0
kecuali ZeroDivisionError:
    cetak("Tidak bisa dibagi nol!")
akhirnya:
    cetak("Selesai")
```

#### **Context Manager**
```meta
dengan buka(file.txt, r) sebagai f:
    isi = f.baca()
```

#### **Import Statements**
```meta
dari math import sqrt, pi
import random
import os as sistem
```

#### **Lambda Functions**
```meta
kali_dua = lambda x: x * 2
```

### 🎯 **Daftar Lengkap Keyword yang Didukung**

| Kategori | Keyword Indonesia | Konversi ke |
|----------|------------------|-------------|
| **Input/Output** | `cetak()`, `meta()`, `tulis()` | `print()` |
| | `masukan()`, `baca()` | `input()` |
| **Percabangan** | `jika`, `maka` | `if` |
| | `atau jika` | `elif` |
| | `selain itu` | `else` |
| **Perulangan** | `untuk`, `dalam` | `for`, `in` |
| | `selama` | `while` |
| | `berhenti`, `lanjut` | `break`, `continue` |
| **Fungsi** | `modul`, `fungsi` | `def` |
| | `kembalikan` | `return` |
| **Boolean** | `benar`, `salah` | `True`, `False` |
| | `kosong`, `null` | `None` |
| **Operator Logika** | `dan`, `atau`, `tidak` | `and`, `or`, `not` |
| | `di`, `adalah` | `in`, `is` |
| **OOP** | `kelas` | `class` |
| | `diri` | `self` |
| **Exception** | `coba`, `kecuali` | `try`, `except` |
| | `akhirnya`, `naikkan` | `finally`, `raise` |
| **Lainnya** | `rentang()`, `panjang()` | `range()`, `len()` |
| | `tipe()`, `zip()` | `type()`, `zip()` |
| | `petakan()`, `saring()` | `map()`, `filter()` |

### ⚡ **Fitur Produktivitas**
- **Bracket matching** untuk kurung, kurung siku, dan kurung kurawal
- **Auto-indentation** untuk blok kode (if, for, while, modul)
- **Folding regions** untuk menyembunyikan blok kode
- **Comment toggling** dengan `Ctrl+/`

### 🎨 **Customization**
- Atur warna sintaks sesuai preferensi di `settings.json`
- Tambahkan keyword kustom
- Konfigurasi indentasi (tab vs spasi)

## 🚀 Instalasi

### Dari VS Code Marketplace
1. Buka VS Code
2. Tekan `Ctrl+Shift+X` (Windows/Linux) atau `Cmd+Shift+X` (Mac)
3. Cari "Meta Language Indonesia"
4. Klik **Install**

### Manual
```bash
# Clone repository
git clone https://github.com/dwibakti/meta-lang-vscode.git

# Pindah ke folder ekstensi VS Code
cd ~/.vscode/extensions/  # Linux/Mac
cd %USERPROFILE%\.vscode\extensions\  # Windows

# Copy folder ekstensi
cp -r /path/to/meta-lang-vscode .
```

## 🎯 Contoh Kode Lengkap

### Program Kalkulator Sederhana
```meta
modul kalkulator():
    cetak("=== KALKULATOR SEDERHANA ===")
    cetak("1. Tambah")
    cetak("2. Kurang")
    cetak("3. Kali")
    cetak("4. Bagi")
    
    pilihan = bilangan(masukan("Pilih operasi (1-4): "))
    a = desimal(masukan("Masukkan angka pertama: "))
    b = desimal(masukan("Masukkan angka kedua: "))
    
    jika pilihan == 1 maka:
        hasil = a + b
        cetak(f"Hasil: {a} + {b} = {hasil}")
    atau jika pilihan == 2 maka:
        hasil = a - b
        cetak(f"Hasil: {a} - {b} = {hasil}")
    atau jika pilihan == 3 maka:
        hasil = a * b
        cetak(f"Hasil: {a} × {b} = {hasil}")
    atau jika pilihan == 4 maka:
        coba:
            hasil = a / b
            cetak(f"Hasil: {a} ÷ {b} = {hasil}")
        kecuali ZeroDivisionError:
            cetak("Error: Tidak bisa membagi dengan nol!")
    selain itu:
        cetak("Pilihan tidak valid!")
    
    kembalikan hasil

# Panggil fungsi
kalkulator()
```

### Program Data Mahasiswa
```meta
kelas Mahasiswa:
    modul __init__(diri, nama, nim, nilai):
        diri.nama = nama
        diri.nim = nim
        diri.nilai = nilai
    
    modul info(diri):
        kembalikan f"{diri.nama} ({diri.nim}) - Nilai: {diri.nilai}"
    
    modul lulus(diri):
        kembalikan diri.nilai >= 60

# Data mahasiswa
data_mahasiswa = []

# Input data
n = bilangan(masukan("Jumlah mahasiswa: "))
untuk i dalam rentang(n):
    cetak(f"\nData mahasiswa ke-{i+1}")
    nama = masukan("Nama: ")
    nim = masukan("NIM: ")
    nilai = desimal(masukan("Nilai: "))
    
    m = Mahasiswa(nama, nim, nilai)
    data_mahasiswa.tambah(m)

# Tampilkan hasil
cetak("\n=== DAFTAR MAHASISWA ===")
untuk m dalam data_mahasiswa:
    status = "LULUS" jika m.lulus() selain itu "TIDAK LULUS"
    cetak(f"{m.info()} - {status}")

# Statistik
nilai_list = [m.nilai untuk m dalam data_mahasiswa]
cetak(f"\nRata-rata nilai: {jumlah(nilai_list) / panjang(nilai_list)}")
cetak(f"Nilai tertinggi: {maksimal(nilai_list)}")
cetak(f"Nilai terendah: {minimal(nilai_list)}")
```

## ⌨️ Shortcut & Snippets

| Shortcut | Hasil |
|----------|-------|
| `modul` + Tab | Template fungsi lengkap |
| `jika` + Tab | Template if-else |
| `untuk` + Tab | Template for loop |
| `selama` + Tab | Template while loop |
| `kelas` + Tab | Template class dengan constructor |
| `coba` + Tab | Template try-except |
| `cetak` + Tab | `cetak("")` |
| `masukan` + Tab | `masukan("")` |
| `utama` + Tab | Template main function |
| `listcomp` + Tab | Template list comprehension |

## 🛠️ Konfigurasi

Di `settings.json`:
```json
{
    "files.associations": {
        "*.meta": "meta"
    },
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "editor.formatOnSave": true,
    "[meta]": {
        "editor.defaultFormatter": "dwibakti.meta-lang",
        "editor.wordBasedSuggestions": false
    }
}
```

## 📁 Struktur Ekstensi

```
meta-lang/
├── .vscode/
│   └── launch.json          # Debug configuration
├── syntaxes/
│   └── meta.tmLanguage.json # Syntax highlighting rules (25+ patterns)
├── language-configuration.json  # Language config (brackets, comments, etc.)
├── package.json             # Extension manifest
├── README.md               # This file
├── CHANGELOG.md            # Version history
└── icons/
    └── icon.png            # Extension icon (64x64)
```

## 🔄 Konversi ke Python

Ekstensi ini secara otomatis dapat mengkonversi kode Meta ke Python:

**Input (Meta):**
```meta
modul hitung_luas(panjang, lebar):
    kembalikan panjang * lebar

cetak(hitung_luas(5, 3))
```

**Output (Python):**
```python
def hitung_luas(panjang, lebar):
    return panjang * lebar

print(hitung_luas(5, 3))
```

## 🐛 Pelaporan Bug

Jika menemukan bug atau memiliki saran fitur, silakan buat issue di:
[GitHub Issues](https://github.com/dwibakti/meta-lang-vscode/issues)

## 🤝 Kontribusi

Kontribusi sangat diterima! Langkah-langkah:

1. Fork repository
2. Buat branch baru (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -m 'Menambah fitur X'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

### Area yang Butuh Kontribusi:
- Menambah keyword baru
- Meningkatkan syntax highlighting
- Membuat dokumentasi lebih lengkap
- Contoh program tambahan

## 📜 Lisensi

MIT License - Copyright (c) 2026 dwibakti

## 🙏 Terima Kasih

- Penyedia API
- Komunitas Python Indonesia
- Semua kontributor dan pengguna Meta Language

---

**Meta Language** - Belajar pemrograman lebih mudah dengan bahasa Indonesia! 🇮🇩

*"Pemrograman untuk semua, tanpa hambatan bahasa"*
