import math

# nhập và suất phân số
def input_fraction():
    numerator = int(input("Nhập tử số: "))
    denominator = int(input("Nhập mẫu số: "))
    while denominator == 0:
        print("Mẫu số không thể là số 0")
        denominator = int(input("Mời nhập lại mẫu số: "))
    return {'numerator' : numerator, 'denominator' : denominator}


def fract_formating(fraction):
    return f"{fraction['numerator']}/{fraction['denominator']}"

print("Nhập tử số và mẫu số của phân số thứ nhất")
fraction1 = input_fraction()

print("Nhập tử số và mẫu số của phân số thứ hai")
fraction2 = input_fraction()

print(f"Phân số thứ nhất là: {fract_formating(fraction1)}")
print(f"Phân số thứ hai là: {fract_formating(fraction2)}")

print()
print("----------")
print()

# rút gọn phân số
def find_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def reduce_fract(fraction):
    common_divisor = find_common_divisor(fraction['numerator'], fraction['denominator'])
    reduced_num = fraction['numerator'] // common_divisor
    reduced_den = fraction['denominator'] // common_divisor
    return {'numerator' : reduced_num, 'denominator' : reduced_den}

print(f"Phân số thứ nhất sau khi rút gọn: {fract_formating(reduce_fract(fraction1))}")
print(f"Phân số thứ hai sau khi rút gọn: {fract_formating(reduce_fract(fraction2))}")

print()
print("----------")
print()

# so sánh phân số
def compare_fract(fraction1, fraction2):
    mult1 = fraction1['numerator'] * fraction2['denominator']
    mult2 = fraction2['numerator'] * fraction2['denominator']
    if mult1 > mult2:
        return "Phân số 1 > phân số 2"
    elif mult2 > mult1:
        return "Phân số 2 > phân số 1"
    else:
        return "Hai phân số bằng nhau"

print(compare_fract(fraction1, fraction2))

print()
print("----------")
print()

# tính tổng 2 phân số
def fraction_sum(fraction1, fraction2):
    num_sum = fraction1['numerator'] * fraction2['denominator'] + fraction1['denominator'] * fraction2['numerator']
    den_sum = fraction1['denominator'] * fraction2['denominator']
    return {'numerator' : num_sum, 'denominator' : den_sum}

fract_sum = fraction_sum(fraction1, fraction2)
print(f"Tổng 2 phân số là: {fract_formating(fract_sum)}")

# nhập dãy phân số
def fraction_list():
    n = int(input("Nhập số lượng phân số trong dãy: "))
    lst = []
    for i in range(n):
        print(f"Nhập tử số và mẫu số của phân số {i+1}")
        fraction = input_fraction()
        lst.append(fraction)
    return lst

fract_lst = fraction_list()
proper_lst = []
for fraction in fract_lst:
    proper_lst.append(fract_formating(fraction))

fract_str = ', '.join(proper_lst)
print(f"Danh sách phân số mới nhập: {fract_str}")

# tìm phân số lớn nhất trong dãy phân số
def max_fraction(fraction_lst):
    max_fraction = fraction_lst[0]
    for fraction in fraction_lst:
        if compare_fract(fraction, max_fraction) == "Phân số 1 > phân số 2":
            max_fraction = fraction
    return max_fraction

print(f"Phân số lớn nhất là: {fract_formating(max_fraction(fract_lst))}")

# tổng các phân số trong dãy
sum_fract = {'numerator' : 0, 'denominator' : 1}
for fraction in fract_lst:
    sum_fract = fraction_sum(sum_fract, fraction)
print(fract_formating(sum_fract))