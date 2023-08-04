# Bai tap 1
# đơn vị tiền tệ = triệu VND
loan = 400
monthlyPayment = 10
year2Interest = 0.1
year = 0
month = 0

monthlyInterest = year2Interest/12
remainLoan = loan

while remainLoan > 0:
    # số tiền lãi hàng tháng
    interest = remainLoan * monthlyInterest
    # số tiền còn nợ 
    remainLoan = remainLoan + interest - monthlyPayment
    month += 1
    
while month >= 12:
    year += 1
    month -= 12
    
print(f"Thời gian trả nợ: {year} năm {month} tháng")



# Bai tap 2
# đơn vị tiền tệ = triệu VND
saving = 100
interestRate = 0.03
for i in range(1,11):
    profit = saving * interestRate
    saving += profit
    
print(f"Số tiền sau kỳ hạn {i}: {round(saving,3)} VND")

# Bai tap 3
ngay = int(input("Ngay: "))
thang = int(input("Thang: "))
nam = int(input("Nam: "))

if nam >= 2001 and nam <= 2100:
    if thang >= 1 and thang <= 12:
        if thang in [1,3,5,7,8,10,12]:
            if ngay >= 1 and ngay <= 31:
                print("Dung ngay")
            else:
                if ngay >= 1 and ngay <= 30:
                    if nam % 4 == 0:
                        if thang == 2:
                            if ngay >= 1 and ngay <= 29:
                                print("Dung ngay")
                            else:
                                print("Sai ngay")
                        else:
                            print("Sai ngay")
                    else:
                        print("Dung ngay")
                else:
                    print("Dung ngay")
        else:
            print("Sai ngay")
else:
    print("Sai ngay")