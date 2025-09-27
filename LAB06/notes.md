# Ghi chú Lab 06 – Hệ thống bán hàng lưu niệm trực tuyến CLB bơi lội

## Class Diagram
- Các lớp chính: KhachHang, SanPham, DonHang, GioHang, ThanhToan, Kho.
- Mỗi lớp có thuộc tính và phương thức chính để hỗ trợ quy trình đặt hàng và thanh toán.
- Quan hệ:
  - Khách hàng có giỏ hàng và đơn hàng.
  - Đơn hàng liên kết với sản phẩm và thanh toán.
  - Kho quản lý tồn kho sản phẩm.

## Package Diagram
- UI: giao diện cho khách hàng thao tác (trang chủ, giỏ hàng, thanh toán).
- Controller: điều khiển luồng nghiệp vụ (đơn hàng, sản phẩm, thanh toán).
- Service: xử lý nghiệp vụ (logic).
- Data: các lớp dữ liệu chính (khách hàng, sản phẩm, đơn hàng, kho, thanh toán).
