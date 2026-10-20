
# SimpleCalc — DevSecOps Python Calculator

## 1. Deskripsi Aplikasi
SimpleCalc adalah aplikasi kalkulator berbasis command-line
yang melakukan operasi matematika dasar: penjumlahan,
pengurangan, perkalian, dan pembagian.

Aplikasi juga memvalidasi input angka, memeriksa operator,
dan mencegah pembagian dengan nol.

## 2. Teknologi
- Python 3.12
- Pytest untuk unit testing
- Bandit untuk Static Application Security Testing (SAST)
- GitHub Actions untuk Continuous Integration (CI)

## 3. Struktur Project
- `app/calculator.py`: logika perhitungan
- `app/validator.py`: validasi input
- `app/formatter.py`: format hasil
- `app/cli.py`: antarmuka command-line
- `app/__main__.py`: entry point
- `tests/`: unit test
- `.github/workflows/devsecops.yml`: pipeline CI dan SAST

## 4. Cara Menjalankan
Pastikan Python 3.12 telah terpasang.

Install dependency:
`python -m pip install -r requirements.txt`

Contoh penjumlahan:
`python -m app add 5 3`

Contoh pengurangan:
`python -m app subtract 10 4`

Contoh perkalian:
`python -m app multiply 6 7`

Contoh pembagian:
`python -m app divide 12 3`

Jalankan unit test:
`python -m pytest -q`

## 5. Overview Pipeline DevSecOps
Workflow GitHub Actions berjalan saat ada push ke
branch `main` atau pull request menuju `main`.

Pipeline terdiri atas dua job:
1. `build`: instalasi dependency dan menjalankan unit test.
2. `sast-scan`: menjalankan Bandit setelah job build sukses.

## 6. Quality Gate
Build harus berhasil dan semua unit test harus lulus.
Bandit memindai direktori aplikasi dengan ambang severity
dan confidence minimum medium. Jika pemeriksaan gagal,
job SAST juga gagal.

Branch protection dapat digunakan untuk mewajibkan
status check sebelum pull request digabungkan.
