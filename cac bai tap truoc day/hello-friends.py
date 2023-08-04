# chương trình chào người bạn
import random 

def your_zodiac(birth_year):
    zodiac = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
    position = 4
    return zodiac[(birth_year - position) % 12]

greetings = ["Chào", "Hello", "Xin chào", "Hi"]
name = input("Nhập tên của bạn: ")
gender = input("Giới tính của bạn [Nam / Nữ / Khác]: ")

# xác định danh xưng dựa theo giới tính
if gender.lower() == "nam":
    pronoun = "anh"
elif gender.lower() == "nữ":
    pronoun = "chị"
else:
    pronoun = "bạn"

birth_year = int(input("Bạn sinh năm: "))
current_year = 2023

zodiac = your_zodiac(birth_year)
age = current_year - birth_year
random_greetings = random.choice(greetings)
message = (f"{random_greetings} {pronoun} {name}, {pronoun} tuổi {zodiac} à", f"{random_greetings} {pronoun} {name}, {pronoun} {age} tuổi à")
print(random.choice(message))