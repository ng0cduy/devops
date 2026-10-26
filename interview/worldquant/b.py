import sys
import time

# Case 1: Dùng LIST (Eager)
t1 = time.time()
my_list = [x * x for x in range(10_000_000)] # Tạo 10 triệu số
t2 = time.time()
print(f"List tạo mất: {t2 - t1} giây")
print(f"List tốn RAM: {sys.getsizeof(my_list) / 1024 / 1024} MB")
# Kết quả: Tốn khoảng 3-4 giây và gần 400MB RAM

print("-" * 30)

# Case 2: Dùng GENERATOR (Yield)
t3 = time.time()
my_gen = (x * x for x in range(10_000_000)) # Ngoặc tròn là generator expression
t4 = time.time()
print(f"Gen tạo mất: {t4 - t3} giây")
print(f"Gen tốn RAM: {sys.getsizeof(my_gen)} Bytes")
# Kết quả: Tốn 0.000 giây (tức thì) và chỉ khoảng 100 Bytes RAM