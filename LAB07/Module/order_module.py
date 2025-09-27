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
