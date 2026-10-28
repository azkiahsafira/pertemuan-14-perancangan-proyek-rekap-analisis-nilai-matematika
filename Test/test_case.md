# Test Case
## Program Rekap dan Analisis Nilai Matematika Kelas

**Nama:** Azkiah Safira  
**NIM:** 2225250013  
**Kelas:** 3F  
**Pertemuan:** 14 — Perancangan Proyek Program Sederhana

---

### 1. Tujuan Pengujian

Pengujian dilakukan untuk memastikan program dapat menghitung rata-rata, nilai terendah, nilai tertinggi, dan jumlah siswa yang tuntas berdasarkan KKM 75.

### 2. Daftar Test Case

| No. | Data Masukan | KKM | Rata-rata yang Diharapkan | Nilai Minimum | Nilai Maksimum | Siswa Tuntas | Status |
|---|---|---:|---:|---:|---:|---:|---|
| 1 | 80, 70, 90 | 75 | 80 | 70 | 90 | 2 | Lulus |
| 2 | 85 | 75 | 85 | 85 | 85 | 1 | Lulus |
| 3 | 50, 60, 70 | 75 | 60 | 50 | 70 | 0 | Lulus |

### 3. Analisis Hasil Pengujian

**Test Case 1 — Data Normal**

Data nilai 80, 70, dan 90 menghasilkan rata-rata 80. Nilai minimum adalah 70, nilai maksimum 90, dan terdapat 2 siswa yang tuntas.

**Test Case 2 — Satu Data**

Data nilai 85 menghasilkan rata-rata 85. Nilai minimum dan maksimum sama-sama 85, serta terdapat 1 siswa yang tuntas.

**Test Case 3 — Semua Nilai di Bawah KKM**

Data nilai 50, 60, dan 70 menghasilkan rata-rata 60. Nilai minimum adalah 50, nilai maksimum 70, dan tidak ada siswa yang tuntas.

### 4. Kesimpulan

Ketiga test case memiliki hasil yang sesuai dengan perhitungan yang diharapkan. Pengujian ini menunjukkan bahwa fungsi analisis dapat menghitung statistik nilai dan menentukan ketuntasan siswa untuk ketiga skenario tersebut.