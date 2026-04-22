--Semua password "12345678"

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    nama VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    nama_kategori VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    category_id INT,
    nama_produk VARCHAR(100) NOT NULL,
    harga DECIMAL(10,2),
    stock INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_category
        FOREIGN KEY(category_id) 
        REFERENCES categories(id)
        ON DELETE SET NULL
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    user_id INT,
    total_price DECIMAL(10,2),
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_user
        FOREIGN KEY(user_id)
        REFERENCES users(id)
        ON DELETE SET NULL
);

CREATE TABLE transaction_details (
    id SERIAL PRIMARY KEY,
    transaction_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_transaction
        FOREIGN KEY(transaction_id)
        REFERENCES transactions(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_product
        FOREIGN KEY(product_id)
        REFERENCES products(id)
        ON DELETE SET NULL
);

INSERT INTO users (nama, email, password, role) VALUES
('Admin', 'admin@mail.com', '$2a$12$LcV2WDBvf/qJfWxjVKYYaufymfXraz/4cnF.CyGm4jxnIzdaUw4aG', 'admin'),
('User1', 'user1@mail.com', '$2a$12$LcV2WDBvf/qJfWxjVKYYaufymfXraz/4cnF.CyGm4jxnIzdaUw4aG', 'user'),
('User2', 'user2@mail.com', '$2a$12$LcV2WDBvf/qJfWxjVKYYaufymfXraz/4cnF.CyGm4jxnIzdaUw4aG', 'user'),
('User3', 'user3@mail.com', '$2a$12$LcV2WDBvf/qJfWxjVKYYaufymfXraz/4cnF.CyGm4jxnIzdaUw4aG', 'user'),
('User4', 'user4@mail.com', '$2a$12$LcV2WDBvf/qJfWxjVKYYaufymfXraz/4cnF.CyGm4jxnIzdaUw4aG', 'user');

INSERT INTO categories (nama_kategori) VALUES
('Makanan'),
('Minuman'),
('Elektronik'),
('Pakaian'),
('Aksesoris');

INSERT INTO products (category_id, nama_produk, harga, stock) VALUES
(1, 'Indomie', 3000, 100),
(2, 'Teh Botol', 5000, 50),
(3, 'Headphone', 150000, 20),
(4, 'Kaos', 75000, 30),
(5, 'Jam Tangan', 200000, 10);

INSERT INTO transactions (user_id, total_price, status) VALUES
(2, 11000, 'paid'),
(3, 150000, 'paid'),
(4, 75000, 'pending'),
(5, 200000, 'paid'),
(2, 3000, 'pending');

INSERT INTO transaction_details (transaction_id, product_id, quantity, price) VALUES
(1, 1, 2, 3000),
(1, 2, 1, 5000),
(2, 3, 1, 150000),
(3, 4, 1, 75000),
(4, 5, 1, 200000);