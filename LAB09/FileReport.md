# Lab 09 – Quản lý dự án Website Bán hàng CLB Bơi lội HNT (Agile/Scrum)

## 1. Thông tin dự án

* **Tên dự án:** Website bán hàng cho Câu lạc bộ Bơi lội HNT
* **Nhóm thực hiện:** Nhóm 30 – 3 thành viên
* **Thời gian:** 6 tuần (3 Sprint, mỗi Sprint 2 tuần)
* **Công cụ:** Jira Software, GitHub, VS Code

---

## 2. Mục tiêu

* Xây dựng website bán hàng trực tuyến cho CLB Bơi lội HNT.
* Cho phép **khách hàng** xem, tìm kiếm, thêm sản phẩm vào giỏ, đặt hàng, thanh toán, theo dõi trạng thái đơn.
* Cho phép **admin** quản lý sản phẩm, đơn hàng và xem báo cáo/thống kê.

---

## 3. Phạm vi chức năng

### Khách hàng

* Đăng ký / đăng nhập
* Xem danh sách + chi tiết sản phẩm
* Thêm / chỉnh sửa giỏ hàng
* Đặt hàng & thanh toán
* Theo dõi trạng thái đơn

### Admin

* CRUD sản phẩm
* Quản lý đơn hàng (duyệt, cập nhật trạng thái)
* Xem báo cáo / thống kê

---

## 4. Cấu trúc Epic

1. Quản lý sản phẩm
2. Giỏ hàng & đặt hàng
3. Thanh toán & xử lý đơn
4. Quản lý người dùng / xác thực
5. Giao diện & trải nghiệm
6. Báo cáo & thống kê

---

## 5. Backlog (User Stories)

### Epic 1: Quản lý sản phẩm

* **US-Prod-01:** Admin thêm sản phẩm mới
* **US-Prod-02:** Admin chỉnh sửa sản phẩm
* **US-Prod-03:** Admin xóa/ẩn sản phẩm
* **US-Prod-04:** Khách xem danh sách sản phẩm
* **US-Prod-05:** Khách xem chi tiết sản phẩm

### Epic 2: Giỏ hàng & đặt hàng

* **US-Cart-01:** Khách thêm sản phẩm vào giỏ
* **US-Cart-02:** Khách xem/chỉnh sửa giỏ hàng
* **US-Cart-03:** Khách checkout giỏ hàng
* **US-Order-01:** Khách nhập thông tin giao hàng, thanh toán

### Epic 3: Thanh toán & xử lý đơn

* **US-Pay-01:** Khách chọn phương thức thanh toán
* **US-Pay-02:** Hệ thống xác nhận kết quả thanh toán
* **US-Order-02:** Hệ thống tạo đơn hàng
* **US-Order-03:** Admin cập nhật trạng thái đơn

### Epic 4: Quản lý người dùng / xác thực

* **US-Auth-01:** Đăng ký tài khoản
* **US-Auth-02:** Đăng nhập/đăng xuất
* **US-Auth-03:** Quản lý thông tin cá nhân
* **US-Auth-04:** Quên/đổi mật khẩu

### Epic 5: Giao diện & trải nghiệm

* **US-UI-01:** Trang chủ hiển thị sản phẩm nổi bật
* **US-UI-02:** Bộ lọc & tìm kiếm sản phẩm
* **US-UI-03:** Giao diện responsive

### Epic 6: Báo cáo & thống kê

* **US-Report-01:** Admin xem doanh thu theo ngày/tháng
* **US-Report-02:** Admin xem số đơn theo trạng thái
* **US-Report-03:** Admin xem sản phẩm bán chạy

---

## 6. Sprint Planning

### Sprint 1 (Tuần 1–2): Cơ bản & xác thực

* US-Auth-01, US-Auth-02, US-Auth-03
* US-UI-01
* US-Prod-04

### Sprint 2 (Tuần 3–4): Sản phẩm & giỏ hàng

* US-Prod-01, US-Prod-02, US-Prod-05
* US-Cart-01, US-Cart-02, US-Cart-03

### Sprint 3 (Tuần 5–6): Thanh toán & báo cáo

* US-Pay-01
* US-Order-02, US-Order-03
* US-UI-03
* US-Report-01, US-Report-02, US-Report-03

---

## 7. Phân công thành viên

* **Trần Thanh Hà:** Backend (Auth, Product CRUD, Order API)
* **Phan Phương Nghi:** Frontend (UI Auth, Product List, Checkout)
* **Đỗ Ngọc Cát Tường:** Admin Dashboard, Reporting, Responsive Design

---

## 8. Acceptance Criteria

Mỗi User Story phải:

* Có giao diện đầy đủ theo yêu cầu
* Xử lý dữ liệu chính xác (CRUD, giỏ hàng, thanh toán)
* Kết nối database + GitHub repo
* Được kiểm thử với cả “happy path” và lỗi phổ biến

---

## 9. Evidence từ Jira

* Backlog (Epic + User Stories)
![BL](main/LAB09/jiraimages/1.1.png)
![BL](main/LAB09/jiraimages/1.2.png)

* Sprint Board (To Do → In Progress → Done)
  

* Burndown Chart
 

---

## 10. Sprint Report & Retrospective

* **Sprint 1:**

  * ✅ Hoàn thành Auth cơ bản + hiển thị danh sách sản phẩm
  * ⚠️ Gặp khó khăn kết nối DB, fix xong ở cuối sprint

* **Sprint 2:**

  * ✅ CRUD sản phẩm, giỏ hàng hoạt động ổn
  * ⚠️ Checkout còn thiếu xác thực thanh toán → chuyển sang Sprint 3

* **Sprint 3:**

  * ✅ Thanh toán + báo cáo cơ bản chạy được
  * ⚠️ Responsive chưa tối ưu trên mobile nhỏ → cần cải tiến thêm

**Retrospective:**

* Daily stand-up giúp nhóm sync tốt hơn
* Cần ước tính effort kỹ hơn cho task backend
* Tiếp tục giữ workflow Jira + GitHub để dễ tracking

---

## 11. Kết luận

* Dự án Website Bán hàng CLB Bơi lội HNT đã hoàn thành các chức năng cốt lõi.
* Hướng phát triển tiếp theo: cải thiện UI, tích hợp cổng thanh toán nâng cao (VNPay/MoMo), tối ưu responsive.

---
