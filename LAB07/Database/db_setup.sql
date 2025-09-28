CREATE DATABASE IF NOT EXISTS hnt_shop;
USE hnt_shop;

CREATE TABLE KhachHang (
    customerId INT AUTO_INCREMENT PRIMARY KEY,
    ten VARCHAR(100),
    email VARCHAR(100),
    diaChi VARCHAR(200),
    sdt VARCHAR(20)
);

CREATE TABLE SanPham (
    productId INT AUTO_INCREMENT PRIMARY KEY,
    ten VARCHAR(100),
    gia DOUBLE,
    soLuongTon INT
);

CREATE TABLE DonHang (
    orderId INT AUTO_INCREMENT PRIMARY KEY,
    customerId INT,
    ngayDat TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tongTien DOUBLE,
    trangThai VARCHAR(50),
    FOREIGN KEY (customerId) REFERENCES KhachHang(customerId)
);

CREATE TABLE DonHangItem (
    itemId INT AUTO_INCREMENT PRIMARY KEY,
    orderId INT,
    productId INT,
    soLuong INT,
    thanhTien DOUBLE,
    FOREIGN KEY (orderId) REFERENCES DonHang(orderId),
    FOREIGN KEY (productId) REFERENCES SanPham(productId)
);

CREATE TABLE ThanhToan (
    paymentId INT AUTO_INCREMENT PRIMARY KEY,
    orderId INT,
    phuongThuc VARCHAR(50),
    soTien DOUBLE,
    trangThai VARCHAR(50),
    FOREIGN KEY (orderId) REFERENCES DonHang(orderId)
);

-- Dữ liệu mẫu
INSERT INTO KhachHang(ten,email,diaChi,sdt) 
VALUES ('Nguyen Van A','a@example.com','Ha Noi','0123456789');

INSERT INTO SanPham(ten,gia,soLuongTon) VALUES 
('Áo bơi HNT', 200000, 10),
('Kính bơi HNT', 150000, 5),
('Phao bơi HNT', 100000, 2);
