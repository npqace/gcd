class Person:
    age = 19
    name: str
    
    def __init__(self, name_input):
        self.name = name_input
    
    def talking(self): # overriding
        return self.message()
    
    def talking(self, message): # overloading
        return message
    
    def sitdown():
        pass
    
    @staticmethod # ko liên quan đến đối tượng (phụ trợ cho method trong class)
    def message():
        return "Hello Morning"
    
    @classmethod # method riêng biệt, đại diện lớp đó thực hiện bên ngoài [hàm tính toán, đc xài mà ko cần khởi tạo đối tượng]
    def relation(cls, obj1, obj2):
        return f"{obj1.name} married {obj2.name}"

ace = Person(name_input= "Ace Nguyen")
duc = Person(name_input= "Nhân Đức")

print(Person.relation(ace, duc))

'''
tính chất trong OOP
tính đóng gói - quyền public, private, share v.v.
tính kế thừa - thừa hưởng attribute từ class cha
tính trừu tượng - tạo ra khuôn mẫu trừu tượng để class noi theo (ví dụ Animal - tạo ra lớp với attribute cần thiết để phát triển thêm)
tính đa hình - 

nguyên lý SOLID
'''