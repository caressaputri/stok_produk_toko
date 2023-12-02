Aplikasi saya masih dalam proses deployment di Adaptable\

1. Cara saya mengimplementasikan checklist pada deskripsi Tugas 2 
   adalah dengan cara membuat proyek django terlebih dahulu dan memastikan
   sudah menginstal virtual env, setelah itu baru membuat main dan memastikan
   settings.py sudah sesuai
2. request clinent ke web aplikasi tersebut akan menampilkan sebuah halaman dari template
   html yang telah dibuat dengan views.py sedangkan urls.py adalah path yang akan menampilkan halaman tersebut
   . Atribut atribut yang ada di halaman web tersebut diatur dalam file models.py
3. Perlu menggunakna virtual environment agar tidak langsung akses di dalam sistem komputer,
   hal ini membuat proyek kita lebih aman jika sewaktu waktu ingin diubah atau diperbaiki.
   Di sisi lain perlu virtual environment juga untuk mendeploy aplikasi ke adaptable.
4. MVT yang sekarang digunakan dengan model-view-tamplate yang menampilkan sebuah web
   dari file html yang ditampulkan oleh view dan atributnya diatur di models
   MVC, antara view dan model sangat berkaitan erat
   jadi sulit untuk diubah atau dimodifikasi, satu controller dapat memilih view yang
   berbeda berdasarkan operasi yang ditentukan, input user diatur oleh contoller
   yang memerlukan alur atau control untuk menjalankannya.
   MVVM, model-view-viewmodel, menggunakan pengikatan data dan mudah untuk memisahkan core business logic dari View
   , banyak View bisa dipetakan dengan satu ViewModel dan bisa satu hingga banyak
   relasi yang ada antara View dan ViewModel, mudah untuk memeodifikasi aplikasinya,
   View mengambil input user dan bertindak sebagai entry point pada aplikasi tsb
   perberdaan ketiganya adalah pada fungsi atau jenis dan kompleksitas dari aplikasi dan yang akan dibuat

 TUGAS 3
 1. Perbedaan antara POST dan GET adalah format URLnya. GET menampilkan data data kedalam string URL sedangkan POST tidak. GET menampilkan URL dalam pengiriman data dalam teks ASCII sedangkan POST bisa dengan gambar, dan lain lain.
 2. Perbedaan utama antara XML, JSON, HTML adalah XML memiliki tampilan yang mirip dengan HTML namun fungsi XML adalah untuk menyimpan data sedangkan HTML memberikan tampilan webnya. JSON juga untuk menyimpan/merepresentasikan data dengan format yang lebih terstruktur daripada XML karena terlihat seperti teks biasa
 3. Karena struktur sintaks JSON lebih mudah dibaca dan diterjemahkan dan jelas pengklasifikasiannya dan lebih cepat dalam parsing data oleh server karena menyimpan datanya dlam bentuk array jadi transfer datanya lebih mudah
 4. Cara saya mengimplementasikan checklist diatas adalah dengan melihat kembali berdasarkan tugas 2 kemaren dan apa saja yang harus ditambahkan di tugas 3 ini sesuai yang sudah diajarkan sebelumnya.

TUGAS 4
1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
   Jawab : Django UserCreationForm sesuai namanya adalah produk dari Django untuk membuat user authentication system dengan membuat user login dengan mengimport modul-modul user authentication. User Objects adalah komponen utama pada sistem autentikasi user yang memiliki atribut seperti username, password, email, first_name, dan last_name. Manfaat dari menggunakan Django UserCreationForm adalah semua syarat untuk autentikasi user sudah dihandle langsung oleh django seperti syarat digit password, format input, dll.

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Djando, dan mengapa keduanya penting?
   Jawab : Sesuai namanya autentikasi berasal dari akta autentik adalah pembuatan hal yang unik atau satu username untuk satu pengguna dan siapa pengguna tersebut, sedangakan otorisasi adalah aturan yang diperlukan dalam autentikasi dan hal apa yang bisa diakses oleh user dan tidak bisa diubah ubah oleh user. Keudanya penting karena menyangkut data privasi pengguna, setiap pengguna yang ingin memasukkan data dirinya pasti memiliki kepentiangan di dalamnya sehingga sangat diperlukan otorisasi untuk menunjang keamanan dan kenyamanan user.

3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
   Jawab : Cookies dalam konteks aplikasi web adalah teks kecil yang dikirimkan kepada browser oelah website yang dikunjungi yang dapat membantu website tersebut untuk mengingat informasi yang pernah dikunjungi, management sesi, personalisasi, dan tracking. Django mengelola sesi dengan cara cookies membiarkan website mengenali pengguna dan mengingat informasi login individual dan preferensi pengguna.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada resiko potensial yang harus diwaspadai?
   Jawab : Jika pada konteksnya kuliah PBP sepertinya masih menggunakan cookies first-party dimana cookies untuk management sesi, pesonalisasi, dan trackingnya akan secara langsung dibuat pada website yang digunakan dan relatif lebih aman selama menggunakan web yang bereputasi baik atau yang belum pernah terkena cyberatatck. Sebaliknya jika memakai 3rd party cookies atau sudah menggunakan iklan, data personalisasi pengguna bisa saja digunakan untuk memunculkan iklan yang lebih relevan sehingga lebih rentan dan harus lebih diwaspadai.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekedar mengikuti tutorial).
   a. Membuat tampilan html bernama register dan login
   b. Untuk menjalankan fungsi dari tampilan html diperlukan modifikasi views.py dengan  membuat fungsi register, login_user, logout_user.
   c. Jika pengguna belum memiliki akun maka pada register digunakan UserCreationForm, jika sudah pengguna bisa login dengan memasukkan username dan passwords. nah jika proses autentikasi sukses bisa masuk dan akan terilhat sesion cokkiesnya juga.
   d. Setelah memiliki akun dan login, untuk menambah product dan mengubungkan product dengan user, pada models.py di subdirektori main import form django.contrib.auth.models import user dan mendambahkan Class Product kemudian pada views.py membuat fungsi create_product dan mengexportnya ke show_main. 
   e. untuk Django Cookie, pada views.py menggunakan HttpResponseRedirect dengan menerapkan set_cookies untuk menentukan sesi dan create productnya juga.
   f. Apabila log out akan otomatis terhapus tulisannya pada cookies dan sudah otomatis log out dengan sistem Djangonya.

TUGAS 5
1. **Element Selector:**
   - **ID Selector (#):** Berfungsi memberikan identitas unik pada suatu elemen, memungkinkan penetapan gaya yang bersifat eksklusif.
     ```css
     #header {
       color: blue;
     }
     ```

   - **Class Selector (.):** Membantu dalam pengelompokan elemen dengan atribut yang serupa, memungkinkan penetapan gaya secara kolektif.
     ```css
     .btn {
       background-color: #3498db;
     }
     ```

   - **Tag Selector (nama tag):** Menargetkan semua elemen dengan tag tertentu, memberikan kemampuan untuk penyesuaian gaya secara global.
     ```css
     p {
       font-size: 16px;
     }
     ```

   - **Universal Selector (*):** Merupakan instruksi untuk seluruh elemen dalam dokumen, berguna dalam menginisialisasi atau mengatur ulang properti-properti tertentu.
     ```css
     * {
       margin: 0;
       padding: 0;
     }
     ```

2. **HTML5 Tags:**
   - `<header>`: Menetapkan bagian puncak dokumen atau sebagian yang kritis.
   - `<nav>`: Menetapkan area navigasi atau menu.
   - `<section>`: Membagi bagian dalam dokumen.
   - `<article>`: Menetapkan artikel yang dapat berdiri sendiri dalam dokumen.
   - `<footer>`: Menetapkan bagian bawah dokumen atau sebagian penutup.
   - `<figure>` dan `<figcaption>`: Digunakan untuk menyisipkan gambar dan keterangan.
   - `<main>`: Menetapkan isi utama dalam dokumen.

3. **Perbedaan antara Margin dan Padding:**
   - **Margin:** Menetapkan jarak di luar batas elemen, tidak memiliki warna latar belakang dan tidak bersentuhan dengan elemen tetangga.
     ```css
     .box {
       margin: 10px;
     }
     ```

   - **Padding:** Menetapkan ruang di dalam batas elemen, antara batas elemen dan kontennya, memiliki warna latar belakang dan bersentuhan dengan elemen tetangga.
     ```css
     .box {
       padding: 10px;
     }
     ```

4. **Perbedaan antara Tailwind dan Bootstrap:**
   - **Tailwind CSS:**
     - Mengadopsi paradigma utility-first, memberikan fleksibilitas tinggi untuk menyesuaikan desain secara rinci.
     - Menawarkan keunggulan dalam hal keringanan karena hanya memuat komponen yang benar-benar diperlukan.

   - **Bootstrap:**
     - Menyediakan pengalaman "out of the box" dengan komponen dan gaya bawaan yang siap pakai.
     - Cocok untuk proyek yang membutuhkan desain cepat tanpa perlu menyesuaikan secara mendalam.

   - **Pilihan:**
     - Pilih Bootstrap jika prioritasnya implementasi cepat dan kebutuhan desain yang sudah terdefinisi.
     - Pilih Tailwind jika kontrol yang lebih rinci dan desain yang unik menjadi preferensi.
    
Implementasi checklist 
### Kustomisasi Desain:

1. **Halaman Login, Register, dan Tambah Inventori:**
   - Pilih CSS atau framework (Bootstrap, Tailwind, Bulma).
   - Sesuaikan warna, font, dan layout.
   - Tambahkan gambar atau ikon yang relevan.
   - Animasi atau transisi opsional.

2. **Halaman Daftar Inventori:**
   - Gunakan Card untuk tata letak informasi.
   - Berikan warna dan estetika yang menyenangkan.
   - Pemformatan jelas dan responsif.
   - Gaya tambahan seperti bayangan atau efek hover opsional.
