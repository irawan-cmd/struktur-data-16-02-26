1. Dedupikasi List

Program ini bertujuan untuk menghapus elemen yang duplikat dalam sebuah list tanpa mengubah urutan kemunculan pertamanya. Caranya adalah dengan menggunakan set untuk mencatat elemen yang sudah pernah muncul. Saat program membaca setiap elemen, jika elemen tersebut belum pernah disimpan di dalam set, maka elemen akan dimasukkan ke dalam list hasil. Jika sudah pernah muncul, maka dilewati. Dengan cara ini, urutan tetap sesuai awal tetapi tidak ada data yang berulang.

2. Intersection Dua Array

Soal ini meminta kita mencari elemen yang sama di dua list berbeda. Konsepnya adalah mencari irisan (intersection). Biasanya digunakan set karena set secara otomatis menangani keunikan data dan memiliki operasi irisan. Hasil akhirnya adalah list yang berisi elemen-elemen yang muncul di kedua list tersebut.

3. Anagram Check

Anagram adalah dua kata yang memiliki huruf yang sama dengan jumlah yang sama, tetapi urutannya berbeda. Untuk mengeceknya, kita menghitung jumlah setiap karakter pada string pertama menggunakan dictionary. Kemudian jumlah tersebut dibandingkan dengan string kedua. Jika semua huruf dan jumlahnya sama, maka kedua string tersebut adalah anagram. Jika ada huruf yang berbeda atau jumlahnya tidak sama, maka bukan anagram.

4. First Recurring Character

Soal ini meminta kita mencari karakter pertama dalam sebuah string yang muncul lebih dari satu kali. Caranya adalah dengan membaca string dari kiri ke kanan, lalu menyimpan setiap karakter yang sudah pernah muncul ke dalam set. Jika saat membaca ditemukan karakter yang sudah ada di dalam set, berarti itulah karakter pertama yang berulang.

5. Simulasi Buku Telepon

Program ini mensimulasikan buku telepon sederhana dengan fitur tambah kontak, cari kontak, dan menampilkan semua kontak. Data biasanya disimpan menggunakan dictionary karena strukturnya cocok untuk pasangan nama dan nomor telepon. Program berjalan menggunakan menu (perulangan), sehingga pengguna bisa memilih tindakan yang ingin dilakukan. Saat menambah kontak, data disimpan. Saat mencari, program mengecek apakah nama tersebut ada di dictionary. Jika ingin melihat semua kontak, program menampilkan seluruh isi dictionary.# struktur-data-16-02-26
