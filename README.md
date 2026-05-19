# 📈 Analisis Komparatif Algoritma Machine Learning dan Deep Learning untuk Prediksi Harga Minyak Mentah Dunia (Brent Crude Oil)

[![Web App Status](https://img.shields.io/badge/Deployment-Railway-blueviolet?style=for-the-badge&logo=railway)](https://www.prediksiminyakbrent.my.id)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)](https://www.python.org)
[![Framework](https://img.shields.io/badge/Framework-Flask-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)

Repositori ini memuat kode sumber, dataset, serta proses eksperimen komparatif untuk memprediksi harga minyak mentah global (**Brent Crude Oil**). Menguji stabilitas 5 pendekatan lintas paradigma (Statistik, Clustering, Neural Network Manual, ANN, dan Deep Learning Rekuren). Seluruh sistem diintegrasikan ke dalam interface web berbasis **Flask** dan di-deploy menggunakan platform **Railway** dengan kustomisasi domain lokal.

---

## 👥 Identitas Peneliti / Mahasiswa
* **Nama Lengkap:** Wifa Saputra
* **NIM:** 301240063
* **Mata Kuliah:** KECERDASAN BUATAN
* **Status Tugas:** Ujian Tengah Semester (UTS)

---

## 🌐 Arsitektur Distribusi & Integrasi Custom Domain
Untuk memastikan aplikasi web Flask ini dapat diakses secara reliabel oleh publik dengan penamaan domain lokal yang profesional, dilakukan konfigurasi *Domain Name System* (DNS) pada panel **IDwebhost** yang diarahkan menuju infrastruktur produksi **Railway** dengan rincian arsitektur sebagai berikut:

* **Footprint Domain Utama (`@`):** Diarahkan menggunakan **A Record** menuju *Static IP Platform* Railway (`20.119.57.240`) untuk menangani *traffic* langsung tanpa prefix.
* **Subdomain Versi WWW (`www`):** Dikonfigurasi menggunakan **CNAME Record** yang di-alias-kan secara penuh ke *canonical name* target dari distribusi Railway (`uias98m1.up.railway.app`).
* **Verifikasi Keamanan Automated SSL/TLS:** Manajemen pembuktian kepemilikan domain diintegrasikan menggunakan instruksi **TXT Record** lewat host `_railway-verify.www` demi mengaktifkan enkripsi enkapsulasi HTTPS otomatis pada sisi server.

---

## 🔬 Ringkasan Eksperimen & Perbandingan Algoritma
Penelitian ini menguji stabilitas komparatif dari 5 algoritma berbeda menggunakan data runtun waktu (*univariate time-series*) pada dataset historis dengan metrik evaluasi **MAE (Mean Absolute Error)** dan **RMSE (Root Mean Squared Error)**:

1. **Linear Regression:** Baseline model statistik menggunakan metode *Ordinary Least Squares*.
2. **Artificial Neural Network (ANN):** Feed-forward MLP standar menggunakan optimasi Adam.
3. **RNN - Long Short-Term Memory (LSTM):** Jaringan saraf rekuren tingkat lanjut untuk menangkap ketergantungan temporal jangka panjang.
4. **K-Means Clustering:** Pendekatan spasial kontinu untuk segmentasi fase makroekonomi pasar.
5. **Backpropagation Manual:** Implementasi arsitektur neural network murni menggunakan operasi matriks dasar `NumPy` tanpa bantuan framework high-level.

> **📌 Hasil Terbaik:** Model **RNN-LSTM** terbukti menghasilkan tingkat galat minimum yang paling mendekati nol (paling presisi) karena kemampuannya memfilter noise volatilitas harian dan mengingat tren runtun waktu jangka panjang. Model inilah yang diekspor menjadi berkas biner `lstm_model.h5` sebagai mesin prediksi utama pada aplikasi web produksi.

---

## 📦 Struktur Repositori Resmi
Daftar berkas di bawah ini disusun secara modular sesuai dengan struktur aktual di dalam repositori:

```text
├── data/
│   └── BrentOilPrice.csv             # Dataset historis komoditas Brent Crude Oil
├── models/
│   ├── ann_model.h5                  # Hasil ekspor biner arsitektur model ANN
│   ├── kmeans_model.pkl              # Hasil serialisasi model K-Means Clustering
│   ├── linear_regression_model.pkl   # Hasil serialisasi model Linear Regression
│   ├── lstm_model.h5                 # Hasil ekspor biner arsitektur model LSTM terbaik
│   └── scaler.pkl                    # Objek transformasi skala data (MinMaxScaler)
├── notebooks/
│   └── eda.ipynb                     # Jupyter Notebook proses EDA & Pelatihan 5 Model
├── templates/
│   └── index.html                    # Antarmuka frontend web (HTML5 & Bootstrap 5)
├── .gitignore                        # Berkas konfigurasi pengabaian tracking Git
├── app.py                            # Kode utama backend Flask (Routing & Inference)
├── Procfile                          # Konfigurasi manajemen proses pelayan server Railway
├── requirements.txt                  # Daftar dependensi library Python
└── README.md                         # Dokumentasi utama proyek
