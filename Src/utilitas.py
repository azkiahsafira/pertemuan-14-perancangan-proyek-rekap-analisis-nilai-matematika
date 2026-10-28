# ============================================================
# PERTEMUAN 14 | PERANCANGAN PROYEK PROGRAM SEDERHANA
# Program  : Utilitas Tampilan dan Penyimpanan Laporan
# File     : utilitas.py
# Nama     : Azkiah Safira
# NIM      : 2225250013
# Kelas    : 3F
# ============================================================

from pathlib import Path
from datetime import datetime


# ------------------------------------------------------------
# MEMBUAT ISI LAPORAN
# ------------------------------------------------------------
def buat_isi_laporan(hasil):
    """Menyusun hasil analisis menjadi laporan teks."""
    waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    isi = (
        "=" * 58 + "\n"
        "           LAPORAN ANALISIS NILAI MATEMATIKA\n"
        "=" * 58 + "\n"
        f"Tanggal laporan       : {waktu}\n"
        "-" * 58 + "\n"
        f"Jumlah siswa          : {hasil['jumlah_data']}\n"
        f"Total nilai           : {hasil['total_nilai']:.2f}\n"
        f"Rata-rata             : {hasil['rata_rata']:.2f}\n"
        f"Nilai terendah        : {hasil['nilai_terendah']:g}\n"
        f"Nilai tertinggi       : {hasil['nilai_tertinggi']:g}\n"
        f"KKM                   : {hasil['kkm']}\n"
        f"Siswa tuntas          : {hasil['jumlah_tuntas']}\n"
        f"Siswa belum tuntas    : {hasil['jumlah_belum_tuntas']}\n"
        "=" * 58 + "\n"
    )

    return isi


# ------------------------------------------------------------
# MENAMPILKAN LAPORAN
# ------------------------------------------------------------
def tampilkan_laporan(hasil):
    """Menampilkan ringkasan analisis nilai ke terminal."""
    print("\n" + "=" * 58)
    print("                 HASIL ANALISIS NILAI")
    print("=" * 58)

    print(f"{'Jumlah siswa':<25}: {hasil['jumlah_data']}")
    print(f"{'Total nilai':<25}: {hasil['total_nilai']:.2f}")
    print(f"{'Rata-rata':<25}: {hasil['rata_rata']:.2f}")
    print(f"{'Nilai terendah':<25}: {hasil['nilai_terendah']:g}")
    print(f"{'Nilai tertinggi':<25}: {hasil['nilai_tertinggi']:g}")
    print(f"{'KKM':<25}: {hasil['kkm']}")
    print(f"{'Siswa tuntas':<25}: {hasil['jumlah_tuntas']}")
    print(f"{'Siswa belum tuntas':<25}: {hasil['jumlah_belum_tuntas']}")

    print("=" * 58)


# ------------------------------------------------------------
# MENYIMPAN LAPORAN
# ------------------------------------------------------------
def simpan_laporan(hasil, nama_file):
    """Menyimpan laporan ke dalam file teks."""
    lokasi_file = Path(nama_file)

    try:
        lokasi_file.parent.mkdir(parents=True, exist_ok=True)

        isi_laporan = buat_isi_laporan(hasil)
        lokasi_file.write_text(isi_laporan, encoding="utf-8")

        return True

    except OSError as error:
        print(f"Kesalahan saat menyimpan laporan: {error}")
        return False