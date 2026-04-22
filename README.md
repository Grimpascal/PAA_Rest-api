# 🛒 Simple Store API

## a) Deskripsi Project

Simple Store API adalah RESTful API berbasis FastAPI yang digunakan untuk mengelola sistem toko sederhana.
Sistem ini mencakup manajemen **produk, kategori, pengguna, dan transaksi**.

Domain yang dipilih adalah **sistem toko (retail sederhana)**, di mana:

* Admin dapat mengelola produk dan kategori
* User dapat melihat produk dan melakukan transaksi
* Sistem secara otomatis menghitung total harga dan mengurangi stok

---

## b) Teknologi yang Digunakan

* **Bahasa Pemrograman**: Python
* **Framework**: FastAPI
* **Database**: PostgreSQL
* **ORM**: SQLAlchemy
* **Authentication**: JWT (OAuth2 Password Flow)
* **Password Hashing**: bcrypt (passlib)

---

## c) Instalasi dan Menjalankan Project

### 1. Clone Repository

```bash
git clone <repo-url>
cd project
```

### 2. Install Dependency

```bash
pip install -r requirements.txt
```

### 3. Konfigurasi Database

Edit file `database.py`:

```python
DATABASE_URL = "postgresql://username:password@localhost:5432/nama_database"
```

---

### 4. Jalankan Server

```bash
uvicorn main:app --reload
```

---

### 5. Akses API Documentation (Swagger)

```
http://127.0.0.1:8000/docs
```

---

## d) Cara Import Database

### Opsi 1: Menggunakan SQL File

Jika tersedia file `.sql`, jalankan:

```bash
psql -U username -d nama_database -f database.sql
```

---

### Opsi 2: Otomatis dari SQLAlchemy

Pastikan di `main.py` terdapat:

```python
from models import Base
from database import engine

Base.metadata.create_all(bind=engine)
```

Kemudian jalankan server untuk membuat tabel otomatis.

Lalu insert ke database:

```sql
INSERT INTO users (nama, email, password, role)
VALUES ('admin', 'admin@mail.com', '<hashed_password>', 'admin');
```

---

## e) Daftar Endpoint

| Method | URL              | Keterangan                      |
| ------ | ---------------- | ------------------------------- |
| POST   | /auth/register   | Register user baru              |
| POST   | /auth/login      | Login dan mendapatkan token     |
| GET    | /products        | Menampilkan semua produk        |
| GET    | /products/{id}   | Detail produk                   |
| POST   | /products        | Menambahkan produk (admin only) |
| PUT    | /products/{id}   | Update produk (admin only)      |
| DELETE | /products/{id}   | Hapus produk (admin only)       |
| POST   | /transactions    | Membuat transaksi (user login)  |
| GET    | /transactions    | Melihat semua transaksi         |

---

## f) Link Video Presentasi

Silakan masukkan link video presentasi di bawah ini:

```
https://link-video-presentasi-anda
```

---

## 🔐 Cara Authentication di Swagger

1. Klik tombol **Authorize**
2. Masukkan:

   * username → email
   * password → password
3. Klik Authorize

Token akan digunakan otomatis untuk endpoint yang dilindungi.

---

## 📌 Catatan

* Password disimpan dalam bentuk hash (bcrypt)
* Endpoint tertentu dilindungi dengan JWT dan role-based access
* Transaksi akan otomatis:

  * menghitung total harga
  * mengurangi stok produk

---
