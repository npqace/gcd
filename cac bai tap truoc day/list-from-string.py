# chương trình nhận diện list từ 1 string
str = "[12, 25, 38, 18, 16]"
n_list = str.replace(",", "").replace("[", "").replace("]", "")
list = n_list.split()

for i  in list:
    print(i)
    
print()
print("-----------")
print()

# chương trình nhận diện công thức toán học
import math

x = int(input("Nhập giá trị x: "))

formula_str = "sin^2x + cos^2x"
n_formula = formula_str.replace("sin^2x", "math.sin(x)**2").replace("cos^2x", "math.cos(x)**2")
formula = math.ceil(eval(n_formula))

print(f"sin^2x + cos^2x = {formula}")