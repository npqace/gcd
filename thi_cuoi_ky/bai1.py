# bai 1
import math

# n = int(input("Nhập số: "))

lst = []
for i in range(1,11):
    lst.append(i)
# for i in range(n):
#     num = int(input("Nhập số vào danh sách: "))
#     lst.append(num)

lst.sort(reverse=True)
print(lst)

# tim so nguyen
def prime(n):
    for i in lst:
        a = 0
        for j in range(1, i):
            if i % j == 0:
                a += 1
        if a == 1:
            prime_lst.append(i)

prime_lst = []
prime(lst)
print("Số nguyên tố trong mảng: ", prime_lst)

# tim boi so
multiples_lst = []
for i in lst:
    if i % 3 == 0:
        multiples_lst.append(i)

print("Bội số của 3:", multiples_lst)