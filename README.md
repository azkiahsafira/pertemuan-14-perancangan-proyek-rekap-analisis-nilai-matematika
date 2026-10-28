# Pertemuan 14 — Perancangan Proyek Program Sederhana
Nama: Azkiah Safira
NIM: 2225250013
Kelas: 3F

## Deskripsi Proyek
**Program Rekap dan Analisis Nilai Matematika Kelas** merupakan rancangan program sederhana untuk membantu guru mengelola dan menganalisis nilai matematika siswa secara terstruktur. Program dirancang untuk membaca data nilai, memvalidasi data, menghitung statistik, menentukan ketuntasan berdasarkan Kriteria Ketuntasan Minimal (KKM), serta menyimpan hasil analisis dalam bentuk laporan teks.

## Tujuan
1. Merancang program untuk mengolah data nilai matematika siswa.
2. Menerapkan fungsi dan struktur data agar program lebih modular.
3. Merancang proses validasi data untuk mencegah kesalahan input.
4. Menentukan algoritma dan struktur program sebelum implementasi.
5. Menyusun test case awal untuk memeriksa ketepatan rancangan.
6. Mendokumentasikan rancangan proyek menggunakan Git dan GitHub.

## Fitur Proyek
1. Membaca data nilai siswa dari file.
2. Memvalidasi nilai dalam rentang 0–100.
3. Menghitung rata-rata, nilai minimum, dan nilai maksimum.
4. Menghitung jumlah siswa tuntas dan belum tuntas berdasarkan KKM.
5. Menyimpan hasil analisis ke dalam file laporan.

## Struktur Folder
```text
pertemuan 14 perancangan proyek/
├── README.md
├── .gitignore
├── proposal.md
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── laporan.py
├── test/
│   └── test_case.py
└── output/
    └── laporan_nilai.txt
```

## Kebutuhan Sistem
- Python 3
- Visual Studio Code
- Git
- Akun GitHub

## Spesifikasi Input, Proses, dan Output
| Komponen | Keterangan |
|---|---|
| Input | Data nilai siswa dari file teks |
| Proses | Membaca dan memvalidasi data, menghitung statistik, menentukan ketuntasan |
| Output | Ringkasan statistik dan laporan hasil analisis dalam file teks |

## Rancangan Algoritma
1. Mulai program.
2. Baca data nilai dari file.
3. Periksa apakah file tersedia dan format data valid.
4. Validasi setiap nilai agar berada pada rentang 0–100.
5. Simpan nilai valid ke dalam struktur data list.
6. Hitung rata-rata, nilai minimum, dan nilai maksimum.
7. Tentukan jumlah siswa yang tuntas dan belum tuntas berdasarkan KKM.
8. Tampilkan ringkasan hasil analisis.
9. Simpan laporan ke file teks.
10. Selesai.

## Rancangan Struktur Program
| File | Tanggung Jawab |
|---|---|
| `main.py` | Mengatur alur utama program |
| `data_io.py` | Membaca dan memvalidasi data nilai |
| `analisis.py` | Menghitung statistik dan ketuntasan |
| `laporan.py` | Menampilkan dan menyimpan laporan |
| `test_case.py` | Menguji hasil sesuai test case awal |

## Test Case Awal
| ID | Kondisi Pengujian | Expected Result |
|---|---|---|
| TC01 | Nilai 80, 70, 90 | Rata-rata 80 |
| TC02 | Nilai 0 | Diterima sebagai nilai valid |
| TC03 | Nilai 100 | Diterima sebagai nilai valid |
| TC04 | Nilai 105 | Ditolak dengan pesan validasi |
| TC05 | File tidak ditemukan | Kesalahan ditangani dengan pesan yang jelas |
| TC06 | Semua nilai memenuhi KKM | Jumlah siswa tuntas sama dengan jumlah data valid |

## Cara Menjalankan
Pada tahap Pertemuan 14, proyek masih berupa rancangan. Setelah file implementasi dibuat pada Pertemuan 15, program utama direncanakan dijalankan melalui terminal VS Code dengan perintah:

```bash
python src/main.py
```

## Rencana Milestone
1. **Pertemuan 14:** menyelesaikan proposal, algoritma, struktur folder, test case, dan pembagian tugas.
2. **Antara Pertemuan 14–15:** mulai mengimplementasikan fitur wajib.
3. **Pertemuan 15:** mengintegrasikan modul, menjalankan pengujian, memperbaiki bug, dan melengkapi dokumentasi.
4. **Pertemuan 16:** mempersiapkan demonstrasi dan presentasi proyek.

## Refleksi
Melalui perancangan proyek ini, saya mempelajari bahwa pembuatan program perlu diawali dengan identifikasi masalah, kebutuhan pengguna, serta batasan fitur. Perancangan input, proses, output, algoritma, struktur program, dan test case membantu memastikan bahwa implementasi memiliki arah yang jelas. Rancangan ini akan menjadi pedoman untuk mengembangkan program yang dapat dijalankan dan diuji pada Pertemuan 15.