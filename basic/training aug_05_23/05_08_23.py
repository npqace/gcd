# bài học về file
#
# # Read
# f = open("store.txt", "r", encoding="utf-8")
# a = f.readlines()
# for i in a:
#     print(i)
#
# # Create
# f2 = open("store2.txt", "w")
# b = ["jkhlkjnd", "aksdfahds;", "fahssihsdk"]
# f2.writelines(b)
#
# # Update
# f3 = open("store3.txt", "w")
# c = ["jkhlkjnd", "aksdfahds;", "fahssihsdk"]
# f3.write("123123123ggio")
#
# f.close()
# f2.close()
# f3.close()
#


# Dạng read/write hay xài
# with open("store2.txt", "r+") as f:
#     # print(f.read())
#     f.write("Xe34676")

# Xử lý ngoại lệ
try:
    f = open("store6.txt", "r")
except FileNotFoundError as e:
    f = open("store6.txt", "w+")
    f.write(f"{e}")
finally:
    f = open("store6.txt", "r")
    print(f.read())