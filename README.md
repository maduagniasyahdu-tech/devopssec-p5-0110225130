# Aplikasi DevSecOps Python Demo (P5)

## 1. Nama Aplikasi & Fungsi
Aplikasi ini adalah REST API sederhana berbasis Python Flask yang menyediakan layanan kalkulasi matematika dasar melalui endpoint HTTP.

## 2. Bahasa & Framework
- **Bahasa Pemrograman**: Python
- **Framework**: Flask
- **Testing Framework**: Pytest

## 3. Cara Menjalankan Aplikasi
1. Install dependencies: `pip install -r requirements.txt`
2. Jalankan pengujian: `pytest`
3. Jalankan aplikasi: `flask --app app run`

## 4. Overview Pipeline CI/CD (DevSecOps)
Pipeline menggunakan **GitHub Actions**:
- **Build & Test Job**: Menginstal dependencies dan menjalankan unit test `pytest`.
- **SAST Scan Job**: Menggunakan **Bandit** untuk memindai keamanan kode Python.
