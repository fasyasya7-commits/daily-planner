# ==========================================================
# app.py  -  BACKEND (otak) dari website Daily Planner
# ----------------------------------------------------------
# Materi yang dipakai: variable, list, looping, function, if-else
# Tugas backend: menyimpan data tugas, mengolahnya, lalu
# mengirimnya ke halaman HTML untuk ditampilkan.
# ==========================================================

import json                    # untuk menyimpan/membaca data dalam format .json
import os                      # untuk mengecek apakah sebuah file sudah ada
from datetime import date      # untuk mengetahui tanggal hari ini
from flask import Flask, render_template, request, redirect

app = Flask(__name__)          # membuat aplikasi web Flask

# VARIABLE: nama file tempat data tugas disimpan
NAMA_FILE = "tugas.json"


# ----------------------------------------------------------
# FUNCTION 1: muat_data
# Membaca tugas dari file supaya data tidak hilang
# saat program dimatikan dan dijalankan lagi.
# ----------------------------------------------------------
def muat_data():
    # IF-ELSE: kalau file sudah ada, baca isinya. Kalau belum, mulai dari list kosong.
    if os.path.exists(NAMA_FILE):
        # "with open" membuka file dan otomatis menutupnya setelah selesai
        with open(NAMA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)       # ubah isi file menjadi list
    else:
        return []                        # list kosong = belum ada tugas


# ----------------------------------------------------------
# FUNCTION 2: simpan_data
# Menulis isi daftar_tugas ke file. Dipanggil setiap kali
# ada perubahan (tambah, selesai, hapus).
# ----------------------------------------------------------
def simpan_data():
    with open(NAMA_FILE, "w", encoding="utf-8") as file:
        json.dump(daftar_tugas, file, ensure_ascii=False, indent=2)


# LIST: tempat semua tugas disimpan.
# Setiap tugas berupa "dictionary" (data berlabel), contohnya:
# {"id": 1, "judul": "Belajar Python", "prioritas": "tinggi",
#  "tenggat": "2026-10-20", "selesai": False}
daftar_tugas = muat_data()


# ----------------------------------------------------------
# FUNCTION 3: buat_id_baru
# Setiap tugas butuh nomor unik (id). Kita cari id terbesar
# yang ada, lalu tambah 1.
# ----------------------------------------------------------
def buat_id_baru():
    id_terbesar = 0
    # LOOPING: periksa tugas satu per satu
    for tugas in daftar_tugas:
        if tugas["id"] > id_terbesar:
            id_terbesar = tugas["id"]
    return id_terbesar + 1


# ----------------------------------------------------------
# FUNCTION 4: hitung_selesai
# Menghitung berapa tugas yang sudah selesai.
# ----------------------------------------------------------
def hitung_selesai():
    jumlah = 0
    for tugas in daftar_tugas:
        if tugas["selesai"]:             # True = sudah selesai
            jumlah += 1                  # tambah 1 ke hitungan
    return jumlah


# ----------------------------------------------------------
# FUNCTION 5: tandai_terlambat
# Tugas dianggap terlambat jika tenggatnya sudah lewat
# dan tugas belum selesai.
# ----------------------------------------------------------
def tandai_terlambat():
    hari_ini = date.today().isoformat()  # hasilnya seperti "2026-10-15"
    for tugas in daftar_tugas:
        # Tanggal berformat tahun-bulan-hari bisa dibandingkan langsung dengan < dan >
        if tugas["tenggat"] != "" and tugas["tenggat"] < hari_ini and not tugas["selesai"]:
            tugas["terlambat"] = True
        else:
            tugas["terlambat"] = False


# ==========================================================
# ROUTE = alamat (URL) yang bisa dibuka di browser.
# Baris yang diawali @app.route adalah "label" yang
# menghubungkan alamat dengan function di bawahnya.
# ==========================================================

# Halaman utama: menampilkan semua tugas
@app.route("/")
def halaman_utama():
    tandai_terlambat()
    total = len(daftar_tugas)            # len() = jumlah isi list
    selesai = hitung_selesai()

    # IF-ELSE: hindari pembagian dengan nol saat belum ada tugas
    if total == 0:
        persen = 0
    else:
        persen = round(selesai / total * 100)

    # Kirim semua data ke index.html
    return render_template("index.html",
                           daftar_tugas=daftar_tugas,
                           total=total,
                           selesai=selesai,
                           persen=persen)


# Menambah tugas baru (dipanggil saat tombol "Tambah" diklik)
@app.route("/tambah", methods=["POST"])
def tambah_tugas():
    # Ambil isi form yang diketik pengguna
    judul = request.form["judul"].strip()      # strip() membuang spasi berlebih
    prioritas = request.form["prioritas"]
    tenggat = request.form["tenggat"]

    # IF: hanya simpan kalau judul tidak kosong
    if judul != "":
        tugas_baru = {
            "id": buat_id_baru(),
            "judul": judul,
            "prioritas": prioritas,
            "tenggat": tenggat,
            "selesai": False
        }
        daftar_tugas.append(tugas_baru)        # append() = tambah ke akhir list
        simpan_data()

    return redirect("/")                       # kembali ke halaman utama


# Mengubah status tugas: belum selesai <-> selesai
@app.route("/selesai/<int:id_tugas>", methods=["POST"])
def ubah_status(id_tugas):
    for tugas in daftar_tugas:
        if tugas["id"] == id_tugas:            # cari tugas dengan id yang cocok
            tugas["selesai"] = not tugas["selesai"]   # True jadi False, False jadi True
    simpan_data()
    return redirect("/")


# Menghapus tugas
@app.route("/hapus/<int:id_tugas>", methods=["POST"])
def hapus_tugas(id_tugas):
    for tugas in daftar_tugas:
        if tugas["id"] == id_tugas:
            daftar_tugas.remove(tugas)         # remove() = buang dari list
            break                              # break = hentikan looping, tugas sudah ketemu
    simpan_data()
    return redirect("/")


# Baris ini menjalankan website saat file dijalankan: python app.py
if __name__ == "__main__":
    app.run(debug=True)
