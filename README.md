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
 
