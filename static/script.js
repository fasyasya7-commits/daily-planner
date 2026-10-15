// ==========================================================
// script.js - JAVASCRIPT: membuat halaman "hidup" di browser
// ----------------------------------------------------------
// Materi yang dipakai: variable, array, looping, function, if-else
// ==========================================================


// ----------------------------------------------------------
// FUNCTION 1: tampilkanSapaan
// Menampilkan sapaan sesuai jam dan tanggal hari ini.
// ----------------------------------------------------------
function tampilkanSapaan() {
  // ARRAY (list): daftar nama hari dan bulan.
  // Nomor urutan array dimulai dari 0.
  const namaHari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"];
  const namaBulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
                     "Juli", "Agustus", "September", "Oktober", "November", "Desember"];

  // VARIABLE: menyimpan tanggal dan jam saat ini
  const sekarang = new Date();
  const jam = sekarang.getHours();       // angka 0 sampai 23

  // IF-ELSE: pilih sapaan sesuai jam
  let sapaan;                            // "let" dipakai karena nilainya akan diisi nanti
  if (jam < 11) {
    sapaan = "Selamat pagi";
  } else if (jam < 15) {
    sapaan = "Selamat siang";
  } else if (jam < 18) {
    sapaan = "Selamat sore";
  } else {
    sapaan = "Selamat malam";
  }

  // Ambil nama hari dan bulan dari array memakai nomor urutnya
  const hari = namaHari[sekarang.getDay()];
  const bulan = namaBulan[sekarang.getMonth()];
  const teksTanggal = hari + ", " + sekarang.getDate() + " " + bulan + " " + sekarang.getFullYear();

  // Tulis hasilnya ke elemen HTML yang punya id "sapaan" dan "tanggal"
  document.getElementById("sapaan").textContent = sapaan + "! Apa rencanamu hari ini?";
  document.getElementById("tanggal").textContent = teksTanggal;
}


// ----------------------------------------------------------
// FUNCTION 2: filterTugas
// Menampilkan tugas sesuai tombol filter yang diklik.
// Parameter status: "semua", "belum", atau "selesai"
// Parameter tombol: tombol yang sedang diklik
// ----------------------------------------------------------
function filterTugas(status, tombol) {
  // ARRAY: ambil semua elemen tugas (<li class="tugas-item">)
  const semuaTugas = document.querySelectorAll(".tugas-item");

  // LOOPING: periksa tugas satu per satu
  for (let i = 0; i < semuaTugas.length; i++) {
    const statusTugas = semuaTugas[i].dataset.status;   // isinya "belum" atau "selesai"

    // IF-ELSE: tampilkan tugas yang cocok, sembunyikan yang tidak cocok
    if (status === "semua" || statusTugas === status) {
      semuaTugas[i].style.display = "flex";
    } else {
      semuaTugas[i].style.display = "none";
    }
  }

  // LOOPING lagi: hapus tanda "aktif" dari semua tombol filter...
  const semuaTombol = document.querySelectorAll(".btn-filter");
  for (let i = 0; i < semuaTombol.length; i++) {
    semuaTombol[i].classList.remove("aktif");
  }
  // ...lalu beri tanda "aktif" hanya pada tombol yang diklik
  tombol.classList.add("aktif");
}


// ----------------------------------------------------------
// FUNCTION 3: konfirmasiHapus
// Menampilkan kotak tanya "OK / Batal" sebelum menghapus.
// Mengembalikan true (lanjut hapus) atau false (batal).
// ----------------------------------------------------------
function konfirmasiHapus() {
  return confirm("Yakin ingin menghapus tugas ini?");
}


// Jalankan function sapaan saat halaman dibuka
tampilkanSapaan();
