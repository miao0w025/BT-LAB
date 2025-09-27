# Lab 07 – Module Thanh toán (Cửa hàng lưu niệm CLB Bơi lội HNT)

## 📌 Yêu cầu
Mô phỏng chức năng **thanh toán đơn hàng** cho trang bán đồ lưu niệm CLB bơi lội HNT bằng Python + MySQL.

## 📂 Cấu trúc
- csdl.sql : tạo CSDL + dữ liệu demo  
- thanh_toan.py : code xử lý chính  
- test_thanh_toan.py : file test thanh toán  

## 🚀 Cách chạy
1. Tạo CSDL:
   ```bash
   mysql -u root -p < csdl.sql

2. Cài thư viện Python:

pip install mysql-connector-python

3. Chạy test:

python test_thanh_toan.py

📸 Kết quả

Nếu số dư đủ:

✅ Thanh toán thành công! Đơn hàng #1, số tiền: 300000


Nếu không đủ tiền:

❌ Lỗi: Số dư không đủ để thanh toán


Nếu sản phẩm sai:

❌ Lỗi: Sản phẩm không tồn tại
