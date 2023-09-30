def input_num():
    lst = []
    for i in range(5):
        lst.append(int(input("Nhập phần tử vào mảng: ")))
    return lst

def comm_and_diff(lst1, lst2):
    for i in lst1:
        if i in lst2:
            common.append(i)

    for i in lst1:
        if i not in lst2:
            diff.append(i)
    for j in lst2:
        if j not in lst1:
            diff.append(j)
    # print("Các số giống nhau trong hai mảng:", common)
    print("Tổng các số giống nhau trong hai mảng:", sum(common))
    # print("Các số khác nhau trong hai mảng:", diff)
    print("Tổng các số khác nhau trong hai mảng:", sum(diff))

def find_K():
    k = int(input("Nhập số K: "))
    if k in common:
        print(f"{k} là số trùng lặp trong hai danh sách!")
    else:
        print(f"{k} không phải là số trùng lặp trong hai danh sách!")

print("Nhập phần tử vào mảng 1!")
lst1 = input_num()
print()

print("Nhập phần tử vào mảng 2!")
lst2 = input_num()
print()

common = []
diff = []

print("KẾT QUẢ!")
print("Mảng thứ nhất:",lst1)
print("Mảng thứ hai:",lst2)
comm_and_diff(lst1, lst2)
find_K()