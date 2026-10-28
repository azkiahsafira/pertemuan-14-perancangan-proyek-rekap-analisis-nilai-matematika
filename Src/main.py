# ============================================================
# PERTEMUAN 14 | PERANCANGAN PROYEK PROGRAM SEDERHANA
# Program  : Rekap dan Analisis Nilai Matematika Kelas
# File     : main.py
# Nama     : Azkiah Safira
# NIM      : 2225250013
# Kelas    : 3F
# ============================================================

from data_io import baca_data_nilai
from analisis import analisis_nilai
from utilitas import tampilkan_laporan, simpan_laporan


# ------------------------------------------------------------
# KONFIGURASI PROGRAM
# ------------------------------------------------------------
FILE_INPUT = "data/nilai_contoh.txt"
FILE_OUTPUT = "output/laporan_nilai.txt"
KKM = 75


# ------------------------------------------------------------
# PROGRAM UTAMA
# ------------------------------------------------------------
def main():
    """Mengatur alur utama program analisis nilai."""
    print("=" * 62)
    print("       PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA")
    print("=" * 62)

    print("\n[1] MEMBACA DATA NILAI")
    print("-" * 62)

    daftar_nilai = baca_data_nilai(FILE_INPUT)

    if not daftar_nilai:
        print("Tidak ada data nilai valid untuk dianalisis.")
        return

    print(f"Jumlah nilai valid : {len(daftar_nilai)}")
    print(f"Daftar nilai       : {daftar_nilai}")

    print("\n[2] MENGANALISIS DATA")
    print("-" * 62)

    hasil = analisis_nilai(daftar_nilai, KKM)
    tampilkan_laporan(hasil)

    print("\n[3] MENYIMPAN LAPORAN")
    print("-" * 62)

    if simpan_laporan(hasil, FILE_OUTPUT):
        print(f"Laporan tersimpan  : {FILE_OUTPUT}")
    else:
        print("Laporan gagal disimpan.")

    print("\n" + "=" * 62)
    print("                    PROGRAM SELESAI")
    print("=" * 62)


if __name__ == "__main__":
    main()