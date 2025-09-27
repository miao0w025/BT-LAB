from order_module import create_order

# Test 1: mua 1 kính bơi
create_order(customer_id=1, product_id=2, quantity=1, payment_method="MOMO")

# Test 2: mua 5 phao bơi (quá tồn kho)
create_order(customer_id=1, product_id=3, quantity=5, payment_method="CASH")
