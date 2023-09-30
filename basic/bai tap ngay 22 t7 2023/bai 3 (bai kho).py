n = int(input("Nhập số lượng phần tử trong màng: "))

lst = []
output_lst = []

for i in range(1, n+1):
    lst.append(i)
input_lst = input("Nhập danh sách: ")
splitted = input_lst.split(', ')
for number in splitted:
    num = int(number)
    output_lst.append(num)

print(f"Danh sách đã nhập: {output_lst}")

alter_lst = list(set(lst) ^ set(output_lst))

print(f"Các số bị khuyết là: ", end="")
for i in range(len(alter_lst) - 1):
    print(alter_lst[i], end=", ")
print(alter_lst[len(alter_lst) - 1])