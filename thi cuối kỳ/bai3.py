def product():
    product_id = input("Nhập ID sản phẩm: ")
    product_name = input("Nhập tên sản phẩm: ")
    product_price = int(input("Nhập giá sản phẩm: "))
    product_quantity = int(input("Nhập số lượng sản phẩm: "))
    return {'product_id': product_id, 'product_name': product_name, 'product_price': product_price, 'product_quantity': product_quantity}

def print_info(product):
    print(f"Product ID: {product['product_id']}")
    print(f"Product Name: {product['product_name']}")
    print(f"Product Price: {product['product_price']}")
    print(f"Product Quantity: {product['product_quantity']}")

productlst = []
n = int(input("Nhập số lượng mặt hàng: "))
print("Xin mời nhập thông tin mặt hàng!")
for i in range(n):
    print(f"Nhập thông tin cho mặt hàng {i+1}:")
    prd = product()
    productlst.append(prd)

print()
print("----------")
print()

# tổng giá trị mặt hàng
def product_sum(product_id):
    for product in productlst:
        if product['product_id'] == product_id:
            return product['product_price'] * product['product_quantity']
    return 0 # trả về 0 nếu không tìm thấy sản phẩm

prd_sum = input("Nhập ID sản phẩm bạn muốn tính tổng giá trị: ")
total_price = product_sum(prd_sum)

if total_price > 0:
    print("Tổng giá trị mặt hàng là:", total_price)
else:
    print("Không tìm thấy mặt hàng!")

print()
print("----------")
print()

# đối tượng mặt hàng với thông tin tương ứng
def print_product_by_name(productlst, product_name):
    product_by_name = []
    for product in productlst:
        if product['product_name'] == product_name:
            product_by_name.append(product)
    return product_by_name

print_product_name = input("Nhập tên sản phẩm bạn muốn xem thông tin: ")
product_by_name = print_product_by_name(productlst, print_product_name)

print()

if product_by_name:
    print("Thông tin sản phẩm:")
    for product in product_by_name:
        print_info(product)
else:
    print("Không tìm thấy sản phẩm!")

print()
print("----------")
print()

# tính tổng giá trị toàn bộ kho hàng
def total_value(productlst):
    total_vl = 0 
    for product in productlst:
        product_value = product['product_price'] * product['product_quantity']
        total_vl += product_value
    return total_vl


print("Tổng giá trị toàn bộ kho hàng:",total_value(productlst))

print()
print("----------")
print()

# thông tin mặt hàng có giá trị lớn nhất

max_price = 0
max_product = None

for product in productlst:
    if product['product_price'] > max_price:
        max_price = product['product_price']
        max_product = product

if max_product:
    print("Thông tin mặt hàng có giá trị lớn nhất")
    print_info(max_product)

print()
print("----------")
print()

# thông tin mặt hàng có giá trị nhỏ nhất
min_price = float("inf")
min_product = None

for product in productlst:
    if product['product_price'] < min_price:
        min_price = product['product_price']
        min_product = product

if min_product:
    print("Thông tin mặt hàng có giá trị nhỏ nhất:")
    print_info(min_product)