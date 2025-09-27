```sql
-- Tạo database
CREATE DATABASE IF NOT EXISTS cua_hang_luu_niem;
USE cua_hang_luu_niem;

-- Bảng thành viên (khách hàng)
CREATE TABLE thanh_vien (
    thanhvien_id INT AUTO_INCREMENT PRIMARY KEY,
    ten VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    matkhau VARCHAR(100) NOT NULL,
    sdt VARCHAR(15),
    diaChi VARCHAR(200)
);

-- Bảng sản phẩm
CREATE TABLE san_pham (
    productId INT AUTO_INCREMENT PRIMARY KEY,
    ten VARCHAR(100) NOT NULL,
    gia DOUBLE NOT NULL,
    soLuongTon INT NOT NULL
);

-- Bảng đơn hàng
CREATE TABLE don_hang (
    orderId INT AUTO_INCREMENT PRIMARY KEY,
    thanhvien_id INT,
    ngayDat DATETIME,
    tongTien DOUBLE,
    trangThai VARCHAR(50),
    FOREIGN KEY (thanhvien_id) REFERENCES thanh_vien(thanhvien_id)
);

-- Bảng giao dịch (thanh toán)
CREATE TABLE giao_dich (
    paymentId INT AUTO_INCREMENT PRIMARY KEY,
    orderId INT,
    phuongThuc VARCHAR(50),
    soTien DOUBLE,
    trangThai VARCHAR(50),
    FOREIGN KEY (orderId) REFERENCES don_hang(orderId)
);

-- Thêm dữ liệu mẫu
INSERT INTO thanh_vien(ten, email, matkhau, sdt, diaChi) VALUES
('Nguyễn Văn A', 'a@gmail.com', '123456', '0901234567', 'Hà Nội'),
('Trần Thị B', 'b@gmail.com', 'abcdef', '0907654321', 'TP.HCM');

INSERT INTO san_pham(ten, gia, soLuongTon) VALUES
('Áo thun CLB Bơi Lội HNT', 120000, 10),
('
```
