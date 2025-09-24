* Use Case 1: Đặt hàng & Thanh toán
- Actor chính: Khách hàng
- Mục tiêu: Mua sản phẩm lưu niệm trực tuyến.
- Tiền điều kiện: Khách hàng đã đăng nhập, có sản phẩm trong giỏ hàng.
- Luồng chính:
    1. Khách hàng mở giỏ hàng và nhấn “Thanh toán”.
    2. Hệ thống hiển thị thông tin đơn hàng (sản phẩm, số lượng, giá).
    3. Khách hàng nhập địa chỉ giao hàng, chọn phương thức thanh toán.
    4. Hệ thống kết nối với hệ thống thanh toán trực tuyến.
    5. Sau khi thanh toán thành công, hệ thống tạo đơn hàng và gửi thông báo.
- Luồng thay thế:
    Nếu thanh toán thất bại → báo lỗi, cho phép khách hàng chọn lại phương thức.


* Use Case 2: Quản lý sản phẩm
- Actor chính: Quản trị viên
- Mục tiêu: Quản lý danh mục sản phẩm lưu niệm.
- Tiền điều kiện: Quản trị viên đã đăng nhập.
- Luồng chính:
    1. Quản trị viên chọn menu “Quản lý sản phẩm”.
    2. Hệ thống hiển thị danh sách sản phẩm hiện tại.
    3. Quản trị viên có thể thêm mới sản phẩm (tên, giá, mô tả, hình ảnh).
    4. Quản trị viên có thể chỉnh sửa hoặc xóa sản phẩm.
    5. Hệ thống lưu thông tin và cập nhật giao diện cho khách hàng.
- Luồng thay thế:
    Nếu nhập thiếu thông tin sản phẩm → hệ thống báo lỗi.

