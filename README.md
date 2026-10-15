# 📝 Daily Planner

Website sederhana untuk mencatat dan memantau tugas harian. Dibuat untuk belajar dasar pemrograman web dengan **Python (Flask)** sebagai backend dan **HTML, CSS, JavaScript** sebagai frontend.

## Fitur

- Tambah tugas (judul, prioritas, tenggat)
- Centang tugas selesai / batalkan centang
- Hapus tugas (dengan konfirmasi)
- Filter: Semua, Belum selesai, Selesai
- Progres bar jumlah tugas yang selesai
- Penanda "Terlambat" untuk tugas yang lewat tenggat
- Sapaan dan tanggal otomatis sesuai waktu
- Data tersimpan di file `tugas.json`, jadi tidak hilang saat program dimatikan

## Struktur Proyek

```
daily-planner/
├── app.py              # Backend Python: menyimpan dan mengolah data tugas
├── requirements.txt    # Daftar library yang dibutuhkan
├── README.md           # Panduan ini
├── tugas.json          # Dibuat otomatis saat tugas pertama ditambahkan
├── templates/
│   └── index.html      # Kerangka halaman (HTML)
└── static/
    ├── style.css       # Tampilan (CSS)
    └── script.js       # Interaksi di browser (JavaScript)
```

## Kebutuhan

- Python 3.8 atau lebih baru (cek dengan `python --version`)
- Koneksi internet hanya untuk menginstal Flask pertama kali

## Cara Menjalankan

Buka Command Prompt (Windows) atau Terminal (Mac/Linux), lalu masuk ke folder proyek:

```
cd daily-planner
```

**1. Instal library**

```
pip install -r requirements.txt
```

**2. Jalankan website**

```
python app.py
```

**3. Buka di browser**

```
http://127.0.0.1:5000
```

Untuk menghentikan website, tekan `Ctrl + C` di jendela Command Prompt.

> Jika `pip` atau `python` tidak dikenali di Windows, coba `py -m pip install -r requirements.txt` lalu `py app.py`.

## Cara Kerja Singkat

1. Browser membuka alamat `/` lalu `app.py` mengirim halaman `index.html` beserta data tugas.
2. Saat Anda menambah, mencentang, atau menghapus tugas, form mengirim data ke `app.py`.
3. `app.py` mengubah list `daftar_tugas`, menyimpannya ke `tugas.json`, lalu memuat ulang halaman.
4. `script.js` mengurus hal-hal di sisi browser: sapaan, tanggal, filter, dan konfirmasi hapus.

## Materi yang Dipakai

| Materi | Contoh di kode |
|---|---|
| Variable | `NAMA_FILE`, `judul`, `persen` |
| List / array | `daftar_tugas` (Python), `namaHari` (JavaScript) |
| Looping | `buat_id_baru()`, `hitung_selesai()`, `filterTugas()` |
| Function | semua fungsi di `app.py` dan `script.js` |
| If-else | `muat_data()`, `tandai_terlambat()`, sapaan berdasarkan jam |

Setiap function sudah diberi komentar penjelasan. Disarankan membaca `app.py` terlebih dahulu.

## Masalah Umum

| Masalah | Penyebab dan solusi |
|---|---|
| `ModuleNotFoundError: No module named 'flask'` | Flask belum terinstal. Jalankan `pip install -r requirements.txt`. |
| Halaman tidak bisa dibuka | Pastikan `python app.py` masih berjalan dan alamatnya benar. |
| `Address already in use` | Port 5000 dipakai program lain. Ubah baris terakhir `app.py` menjadi `app.run(debug=True, port=5001)`, lalu buka `http://127.0.0.1:5001`. |
| Perubahan CSS atau JS tidak terlihat | Muat ulang paksa di browser dengan `Ctrl + F5`. |
| Ingin menghapus semua data | Hentikan website, hapus file `tugas.json`, lalu jalankan lagi. |

## Ide Pengembangan Berikutnya

- Fitur edit tugas
- Pengurutan berdasarkan prioritas atau tenggat
- Kolom pencarian tugas
- Kategori tugas (kuliah, rumah, pribadi)

## Catatan

Proyek ini memakai `debug=True` supaya mudah belajar (halaman otomatis dimuat ulang saat kode diubah dan pesan error ditampilkan lengkap). Mode ini hanya untuk belajar di komputer sendiri, bukan untuk dipublikasikan ke internet.
