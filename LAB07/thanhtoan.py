Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import mysql.connector
... 
... def ket_noi():
...     return mysql.connector.connect(
...         host="localhost",
...         user="root",
...         password="123456",
...         database="cua_hang_luu_niem"
...     )
... 
... def thanh_toan(ma_tv, ma_sp, so_luong):
...     conn = ket_noi()
...     cur = conn.cursor()
...     try:
...         conn.start_transaction()
...         
...         # Lấy giá sản phẩm
...         cur.execute("SELECT gia FROM san_pham WHERE ma_sp=%s", (ma_sp,))
...         sp = cur.fetchone()
...         if not sp:
...             raise Exception("❌ Sản phẩm không tồn tại")
...         gia = sp[0]
...         tong_tien = gia * so_luong
... 
...         # Kiểm tra số dư
...         cur.execute("SELECT so_du FROM thanh_vien WHERE ma_tv=%s FOR UPDATE", (ma_tv,))
...         tv = cur.fetchone()
...         if not tv:
...             raise Exception("❌ Thành viên không tồn tại")
...         so_du = tv[0]
... 
...         if so_du < tong_tien:
...             raise Exception("❌ Số dư không đủ để thanh toán")
... 
...         # Cập nhật số dư
...         cur.execute("UPDATE thanh_vien SET so_du=so_du-%s WHERE ma_tv=%s", (tong_tien, ma_tv))

        # Tạo đơn hàng
        cur.execute("""
            INSERT INTO don_hang(ma_tv, ma_sp, so_luong, tong_tien)
            VALUES (%s, %s, %s, %s)
        """, (ma_tv, ma_sp, so_luong, tong_tien))
        ma_dh = cur.lastrowid

        # Ghi log giao dịch
        cur.execute("""
            INSERT INTO giao_dich(ma_tv, ma_dh, loai_gd, so_tien, so_du_con)
            VALUES (%s, %s, 'THANH_TOAN', %s, %s)
        """, (ma_tv, ma_dh, tong_tien, so_du - tong_tien))

        conn.commit()
        print(f"✅ Thanh toán thành công! Đơn hàng #{ma_dh}, số tiền: {tong_tien}")
    except Exception as e:
        conn.rollback()
        print("❌ Lỗi:", e)
    finally:
        conn.close()
