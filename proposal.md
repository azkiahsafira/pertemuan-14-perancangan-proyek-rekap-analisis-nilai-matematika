# Proposal Proyek
## Program Rekap dan Analisis Nilai Matematika Kelas

### 1. Latar Belakang
Pengolahan nilai siswa perlu dilakukan secara teliti agar informasi hasil belajar dapat diketahui dengan mudah. Penghitungan jumlah nilai, rata-rata, nilai tertinggi, nilai terendah, dan ketuntasan secara manual dapat memerlukan waktu serta berisiko menimbulkan kesalahan.

Oleh karena itu, proyek ini merancang program sederhana menggunakan Python untuk membantu proses rekap dan analisis nilai matematika siswa secara terstruktur.

### 2. Tujuan
1. Membaca data nilai siswa dari file teks.
2. Memvalidasi nilai agar berada dalam rentang 0–100.
3. Menghitung jumlah data, total nilai, rata-rata, nilai tertinggi, dan nilai terendah.
4. Menentukan jumlah siswa yang tuntas dan belum tuntas berdasarkan KKM.
5. Menyimpan hasil analisis dalam bentuk laporan teks.

### 3. Deskripsi Program
Program menerima data nilai dari file `nilai_contoh.txt`. Data yang valid kemudian dianalisis menggunakan fungsi-fungsi Python. Program menggunakan KKM sebesar 75 sebagai batas ketuntasan dan menghasilkan laporan yang disimpan pada file `output/laporan_nilai.txt`.

### 4. Rancangan Program
Program dibagi menjadi beberapa bagian:

- `main.py`: mengatur alur utama program.
- `data_io.py`: membaca dan memvalidasi data nilai.
- `analisis.py`: menghitung statistik dan ketuntasan nilai.
- `laporan.py`: menampilkan serta menyimpan laporan hasil analisis.
- `test/test_case.py`: menguji fungsi analisis menggunakan beberapa kasus pengujian.

### 5. Data Masukan
Data masukan berupa angka nilai siswa yang disimpan satu nilai per baris dalam file `data/nilai_contoh.txt`.

Contoh data:

```text
80
70
90
65
75
100
55
85
```

### 6. Keluaran Program
Program menghasilkan informasi berupa:

1. Jumlah nilai yang valid.
2. Total nilai.
3. Rata-rata nilai.
4. Nilai tertinggi dan terendah.
5. KKM yang digunakan.
6. Jumlah siswa tuntas dan belum tuntas.
7. Laporan hasil analisis dalam file teks.

### 7. Pengujian
Pengujian dilakukan menggunakan beberapa test case, yaitu data normal, satu data nilai, dan seluruh nilai berada di bawah KKM. Hasil aktual dibandingkan dengan hasil yang diharapkan untuk memastikan fungsi analisis berjalan sesuai rancangan.

### 8. Penutup
Proyek ini diharapkan menghasilkan program sederhana yang membantu proses rekap dan analisis nilai matematika siswa. Pembagian program menjadi beberapa modul juga memudahkan pengujian, pemeliharaan, dan pengembangan fitur pada tahap berikutnya.