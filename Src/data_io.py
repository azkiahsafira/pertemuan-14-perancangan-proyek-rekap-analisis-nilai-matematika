# ============================================================
# PERTEMUAN 14 | PERANCANGAN PROYEK PROGRAM SEDERHANA
# Program  : Pembacaan dan Validasi Data Nilai
# File     : data_io.py
# Nama     : Azkiah Safira
# NIM      : 2225250013
# Kelas    : 3F
# ============================================================

from pathlib import Path


# ------------------------------------------------------------
# MEMBACA DAN MEMVALIDASI DATA
# ------------------------------------------------------------
def baca_data_nilai(nama_file):
    """Membaca nilai dari file dan menyimpan data yang valid."""
    lokasi_file = Path(nama_file)
    daftar_nilai = []

    try:
        with lokasi_file.open("r", encoding="utf-8") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                isi = baris.strip()

                if not isi:
                    continue

                try:
                    nilai = float(isi)
                except ValueError:
                    print(
                        f"Peringatan: baris {nomor_baris} "
                        "bukan angka yang valid."
                    )
                    continue

                if 0 <= nilai <= 100:
                    daftar_nilai.append(nilai)
                else:
                    print(
                        f"Peringatan: nilai {nilai:g} "
                        "berada di luar rentang 0–100."
                    )

    except FileNotFoundError:
        print(f"File tidak ditemukan: {lokasi_file}")

    except OSError as error:
        print(f"Gagal membaca file: {error}")

    return daftar_nilai