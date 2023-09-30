# tạo mảng
n = int(input("Nhập n: "))
arr = []

for i in range(n):
    arr.append(int(input("Nhập số: ")))

# tìm tổng số các hạng dương, số lượng các số hạng dương và trung bình cộng của mảng
avr = 0 # trung bình cộng 
count = 0 # đếm số lượng hạng dương
pos_sum = 0 # tổng của các số hạng dương

for j in arr:
    if j > 0:
        count += 1
        pos_sum += j
    avr = round(sum(arr) / n)
    
print(f"Positive sum: {pos_sum}")
print(f"Average: {avr}")
print(f"Count: {count}")

print()
print("-----------")
print()

# tìm vị trí của x và index của x
x = int(input("Nhập x: "))
for i in arr:
    if x == i:
        t = 1
    else:
        t = 0
if t == 1:
    print(f"Vị trí của x: {arr.index(x)}")
else:
    print(f"Số {x} không tồn tại trong mảng")
    
print()
print("-----------")
print()

arr_max = arr[0] #gán số đầu tiên trong mảng có giá trị lớn nhất
for k in arr:
    if k > arr_max:
        arr_max = k

print(arr_max)

arr_max_2 = arr[0]
for k in arr:
    if k > arr_max_2 and k != arr_max:
        arr_max_2 = k
        
print(f"Số lớn thứ hai trong mảng là: {arr_max_2}")