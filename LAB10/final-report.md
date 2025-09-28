# FINAL REPORT

**Đề tài:** Hệ thống bán hàng trực tuyến của CLB bơi lội

**Nhóm:** 30

**Thành viên:**
  - Trần Thanh Hà - N23DCPT018
  - Phan Phương Nghi - N23DCPT037
  - Đỗ Ngọc Cát Tường - N23DCPT055

---

## 1. Giới thiệu đề tài

* **Bối cảnh:** CLB bơi lội muốn mở rộng kênh bán hàng trực tuyến nhằm quảng bá hình ảnh, tăng doanh thu từ đồng phục, phụ kiện bơi, vé sự kiện, và khóa học bơi.
* **Mục tiêu:** Xây dựng một hệ thống web bán hàng trực tuyến, giúp người dùng dễ dàng tìm kiếm sản phẩm, đặt hàng, thanh toán và theo dõi đơn hàng.
* **Phạm vi:** Người dùng (khách hàng), quản trị viên (admin CLB), hệ thống quản lý sản phẩm, đơn hàng và tài khoản, hệ thống thanh toán.

---

## 2. Khảo sát thực tế & Vấn đề đặt ra

* CLB hiện chỉ bán hàng trực tiếp tại bể bơi, khó tiếp cận khách hàng xa.
* Quản lý thủ công đơn hàng dễ sai sót, không theo dõi được tồn kho.
* Chưa có kênh online để quảng bá sản phẩm và sự kiện.

---

## 3. Yêu cầu hệ thống

### 3.1. Chức năng chính

* **Đối với khách hàng:**

  * Đăng ký/đăng nhập tài khoản.
  * Xem và tìm kiếm sản phẩm.
  * Thêm sản phẩm vào giỏ hàng.
  * Đặt hàng và thanh toán.
  * Theo dõi trạng thái đơn hàng.

* **Đối với quản trị viên:**

  * Quản lý sản phẩm (thêm, sửa, xóa).
  * Quản lý đơn hàng.
  * Quản lý tài khoản khách hàng.
  * Thống kê doanh thu.

### 3.2. Yêu cầu phi chức năng

* Giao diện thân thiện, dễ sử dụng.
* Bảo mật thông tin khách hàng.
* Hệ thống hoạt động ổn định, xử lý nhanh.

---

## 4. Thiết kế hệ thống

### 4.1. Use Case Diagram

* Mô tả mối quan hệ giữa các tác nhân (khách hàng, quản trị viên) và chức năng hệ thống.

![ucl2](https://github.com/miao0w025/BT-LAB/blob/main/LAB02/UseCaseDiagram.png?raw=true)

### 4.2. Sequence Diagram

![scl3](https://github.com/miao0w025/BT-LAB/blob/main/LAB03/SequenceDiagram.png?raw=true)

### 4.3. Class Diagram

* Các lớp chính: `KhachHang`, `SanPham`, `DonHang`, `ChiTietDonHang`, `Admin`.
* Quan hệ: 1 khách hàng có nhiều đơn hàng, 1 đơn hàng có nhiều chi tiết đơn hàng, 1 admin quản lý nhiều sản phẩm.

![class](https://github.com/miao0w025/BT-LAB/blob/main/LAB06/class-swimmingclub.png?raw=true)

### 4.4. Database Design (MySQL)

* Bảng **KhachHang(id, ten, email, matkhau, sdt, diachi)**
* Bảng **SanPham(id, ten, mota, gia, soluong, hinhanh)**
* Bảng **DonHang(id, idKhachHang, ngayDat, trangThai, tongTien)**
* Bảng **ChiTietDonHang(id, idDonHang, idSanPham, soLuong, gia)**
* Bảng **Admin(id, tenDangNhap, matkhau)**

### 4.5. Cơ sở dữ liệu & code minh hoạ

4.5.1. ERD & script tạo bảng (Lab 05).

  1. Các bảng chính trong ERD

- khach_hang

- san_pham

- don_hang

- chi_tiet_don_hang (bảng trung gian giữa đơn hàng và sản phẩm)

- thanh_toan

- kho

2. ERD (mối quan hệ)

* khach_hang (1) ───< (n) don_hang (1) ───< (n) chi_tiet_don_hang (n) >─── (1) san_pham

* don_hang (1) ─── (1) thanh_toan

* kho (1) ───< (n) san_pham

3. Script tạo bảng

```

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

```

4.5.2. Demo code: form login (Lab 04), đặt hàng (Lab 07).

* Form login HTML (Lab 04)

```

<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Đăng nhập - HNT Swim Club</title>
  <link rel="stylesheet" href="style.css">

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
  <video autoplay muted loop id="bg-video">
    <source src="istockphoto-849810160-640_adpp_is.mp4" type="video/mp4">
  </video>

  <div class="login-container">
    <h1 class="club-name"> HNT SWIM CLUB</h1>
    <h2>Đăng nhập tài khoản</h2>

    <form>
      <div class="input-group">
        <label for="username">Tên đăng nhập</label>
        <div class="input-wrapper">
          <i class="fa fa-user"></i>
          <input type="text" id="username" placeholder="Nhập tên đăng nhập">
        </div>
      </div>

      <div class="input-group">
        <label for="password">Mật khẩu</label>
        <div class="input-wrapper">
          <i class="fa fa-lock"></i>
          <input type="password" id="password" placeholder="Nhập mật khẩu">
        </div>
      </div>

      <div class="remember-me">
        <input type="checkbox" id="remember">
        <label for="remember">Ghi nhớ đăng nhập</label>
      </div>

      <div class="button-group">
        <button type="submit" id="loginBtn">Đăng nhập</button>
        <button type="button" id="cancelBtn">Hủy</button>
      </div>

      <div class="links">
        <a href="#">Quên mật khẩu?</a> | <a href="#">Đăng ký</a>
      </div>
    </form>
  </div>
</body>
</html>

```

* Order module (Lab 7)

```

import mysql.connector

def create_order(customer_id, product_id, quantity, payment_method):
    conn = mysql.connector.connect(
        user="root", password="123456", database="hnt_shop"
    )
    cur = conn.cursor()
    try:
        conn.start_transaction()

        # Kiểm tra sản phẩm
        cur.execute("SELECT gia, soLuongTon FROM SanPham WHERE productId=%s FOR UPDATE", (product_id,))
        row = cur.fetchone()
        if not row:
            raise Exception("Sản phẩm không tồn tại")
        gia, ton = row
        if ton < quantity:
            raise Exception("Không đủ hàng tồn kho")

        # Tính tiền
        tong_tien = gia * quantity

        # Tạo đơn hàng
        cur.execute("INSERT INTO DonHang(customerId, tongTien, trangThai) VALUES (%s,%s,'PENDING')",
                    (customer_id, tong_tien))
        order_id = cur.lastrowid

        # Thêm chi tiết đơn hàng
        cur.execute("INSERT INTO DonHangItem(orderId, productId, soLuong, thanhTien) VALUES (%s,%s,%s,%s)",
                    (order_id, product_id, quantity, tong_tien))

        # Cập nhật tồn kho
        cur.execute("UPDATE SanPham SET soLuongTon=soLuongTon-%s WHERE productId=%s",
                    (quantity, product_id))

        # Thanh toán
        cur.execute("INSERT INTO ThanhToan(orderId, phuongThuc, soTien, trangThai) VALUES (%s,%s,%s,'SUCCESS')",
                    (order_id, payment_method, tong_tien))

        # Cập nhật trạng thái đơn hàng
        cur.execute("UPDATE DonHang SET trangThai='PAID' WHERE orderId=%s", (order_id,))

        conn.commit()
        print("Đặt hàng thành công! Mã đơn:", order_id)

    except Exception as e:
        conn.rollback()
        print("Lỗi:", e)
    finally:
        conn.close()

```

=> Test:

![ordertest](https://github.com/miao0w025/BT-LAB/blob/main/LAB07/Images/run_test_order.png?raw=true)

### 4.6. Kết quả test & báo cáo sprint

4.6.1. Test case (Lab 08).

![pass](https://github.com/miao0w025/BT-LAB/blob/main/LAB08/report-test-OrderFunction.png?raw=true)

4.6.2. Jira backlog, sprint report (Lab 09).

* Jira backlog

Backlog (User Stories):

1. Epic Quản lý sản phẩm: thêm/sửa/xóa, khách xem danh sách & chi tiết.

2. Epic Giỏ hàng & đặt hàng: thêm, chỉnh sửa, checkout, nhập thông tin giao hàng.

3. Epic Thanh toán & đơn hàng: chọn phương thức, xác nhận, tạo & cập nhật đơn.

4. Epic Người dùng: đăng ký, đăng nhập, quản lý thông tin, đổi mật khẩu.

5. Epic Giao diện: trang chủ, tìm kiếm/lọc, responsive.

6. Epic Báo cáo: doanh thu, đơn hàng, sản phẩm bán chạy.

 ![blog](https://github.com/miao0w025/BT-LAB/blob/main/LAB09/jiraimages/1.1.png?raw=true)

* Sprint report

Sprint Planning:

1. Sprint 1 (Tuần 1–2): Xây dựng chức năng xác thực, giao diện cơ bản, khách xem sản phẩm.

2. Sprint 2 (Tuần 3–4): Quản lý sản phẩm và giỏ hàng (thêm, sửa, checkout).

3. Sprint 3 (Tuần 5–6): Thanh toán, quản lý đơn hàng và báo cáo thống kê.

 ![sprint](https://github.com/miao0w025/BT-LAB/blob/main/LAB09/jiraimages/2.1.png?raw=true)

---

## 5. Triển khai

* **Ngôn ngữ & Công nghệ:**

  * Backend: Java.
  * Frontend: HTML, CSS, JavaScript.
  * Database: MySQL.
* **Giao diện mẫu:**

  * Trang đăng ký:
 
  ![loginui](https://github.com/miao0w025/BT-LAB/blob/main/LAB04/loginUI.png?raw=true)

---

## 6. Đánh giá & Kết quả đạt được

* Hệ thống giúp khách hàng dễ dàng mua sắm trực tuyến.
* Admin quản lý hiệu quả sản phẩm, đơn hàng, doanh thu.
* Góp phần quảng bá hình ảnh CLB bơi lội.

---

## 7. Hướng phát triển

* Tích hợp cổng thanh toán online (MoMo, ZaloPay, Visa).
* Tích hợp chatbot hỗ trợ khách hàng.
* Ứng dụng mobile song song với website.
* Tích hợp hệ thống tích điểm thành viên.

---

## 8. Kết luận 

Đề tài đã xây dựng thành công một hệ thống bán hàng trực tuyến cơ bản cho CLB bơi lội. Hệ thống giúp giải quyết hạn chế trong quản lý thủ công, mở rộng kênh bán hàng và mang lại trải nghiệm thuận tiện cho khách hàng.
