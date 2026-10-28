# ============================================================
# PERTEMUAN 14 | PERANCANGAN PROYEK PROGRAM SEDERHANA
# Program  : Analisis Statistik dan Ketuntasan Nilai
# File     : analisis.py
# Nama     : Azkiah Safira
# NIM      : 2225250013
# Kelas    : 3F
# ============================================================


# ------------------------------------------------------------
# MENGANALISIS DATA NILAI
# ------------------------------------------------------------
def analisis_nilai(daftar_nilai, kkm=75):
    """Menghitung statistik dan ketuntasan nilai siswa."""
    if not daftar_nilai:
        return None

    jumlah_data = len(daftar_nilai)
    total_nilai = sum(daftar_nilai)
    rata_rata = total_nilai / jumlah_data

    nilai_terendah = min(daftar_nilai)
    nilai_tertinggi = max(daftar_nilai)

    jumlah_tuntas = sum(nilai >= kkm for nilai in daftar_nilai)
    jumlah_belum_tuntas = jumlah_data - jumlah_tuntas

    return {
        "jumlah_data": jumlah_data,
        "total_nilai": total_nilai,
        "rata_rata": rata_rata,
        "nilai_terendah": nilai_terendah,
        "nilai_tertinggi": nilai_tertinggi,
        "kkm": kkm,
        "jumlah_tuntas": jumlah_tuntas,
        "jumlah_belum_tuntas": jumlah_belum_tuntas,
    }