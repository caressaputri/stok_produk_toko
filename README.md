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
