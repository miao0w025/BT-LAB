import mysql.connector
import hashlib

def verify_user(username, password):
    conn = mysql.connector.connect(user="root", password="123456", database="swimclub_shop")
    cur = conn.cursor()
    cur.execute("SELECT user_id, password_hash FROM users WHERE username=%s", (username,))
    row = cur.fetchone()
    conn.close()
    if row and row[1] == hashlib.sha256(password.encode()).hexdigest():
        return row[0]   # trả về user_id
    return None

def place_order(user_id, product_id, quantity):
    conn = mysql.connector.connect(user="root", password="123456", database="swimclub_shop")
    cur = conn.cursor()
    try:
        conn.start_transaction()

        # check stock
        cur.execute("SELECT stock FROM products WHERE product_id=%s FOR UPDATE", (product_id,))
        row = cur.fetchone()
        if not row:
            raise Exception("Product not found")
        stock = row[0]

        if stock < quantity:
            raise Exception("Not enough stock")

        # update stock
        cur.execute("UPDATE products SET stock = stock - %s WHERE product_id=%s", (quantity, product_id))

        # insert order
        cur.execute("""INSERT INTO orders(user_id, product_id, quantity)
                       VALUES (%s,%s,%s)""", (user_id, product_id, quantity))

        conn.commit()
        print(f"✅ Order success! {quantity} sản phẩm đã được đặt.")
    except Exception as e:
        conn.rollback()
        print("❌ Error:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    # test đăng nhập
    uid = verify_user("nguoitest", "123456")
    if uid:
        print("🔑 Login success, user_id =", uid)
        # test order
        place_order(uid, 1, 2)  # mua 2 cái áo
    else:
        print("Login failed")
