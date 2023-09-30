'''
4 tính chất trong OOP

1. tính đóng gói (encapsulation)
2. tính kế thừa (inheritance)
3. tính trừu tượng (abstraction)
4. tính đa hình (polymorphism)
'''

# tính đóng gói

class Parent:
    name: str # public
    __age: int # private
    _address: int # protected
    
    def __init__(self, name: str):
        self.name = name
        self._age = 22
    
    def public_method(self):
        print("Public")
    
    def __private_method(self):
        pass
    
    def _protected_method(self):
        return 1


ace = Parent("Ace")
print(ace.name)




# tính kế thừa
class Children(Parent): #kế thừa class Parent
    _address: str
    
    def children_method(self):
        self.name = "Children"
        self.public_method()
        self._address = "Da Nang"
    
    # def get_address(self):
    #     return self._address
    
    # def set_address(self, value):
    #     self._address = value
    #     return self._address
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value):
        self._address = value
        return self._address
    
    # ghi đè
    def public_method(self):
        super().public_method()
        print("Children")
    
    def __init__(self, toy: str, class_name: str):
        super().__init__(class_name)
        self.toy = toy
        self.class_name = class_name
        pass


children = Children(name="Ace")
children.children_method()
print(children.name)

children.address = "Ryazan"
print(children.address)

children.public_method()