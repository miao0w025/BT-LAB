CREATE DATABASE swimclub_shop;
USE swimclub_shop;

-- Bảng users
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(64) NOT NULL
);

-- Bảng products
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    stock INT
);

-- Bảng orders
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    product_id INT,
    quantity INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert user demo (mật khẩu: 123456 -> sha256)
INSERT INTO users(username, password_hash)
VALUES ('nguoitest', SHA2('123456', 256));

-- Insert sản phẩm demo
INSERT INTO products(name, price, stock)
VALUES ('Áo thun CLB bơi lội', 200000, 10);