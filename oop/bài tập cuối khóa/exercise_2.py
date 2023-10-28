class ThoiGian:
    def __init__(self, gio, phut, giay):
        self.gio = gio
        self.phut = phut
        self.giay = giay
    
    def __str__(self):
        return f"{self.gio:02d}:{self.phut:02d}:{self.giay:02d}"
    
    def __add__(self, other):
        self.giay += 1
        if self.giay == 60:
            self.giay = 0
            self.phut += 1
        if self.phut == 60:
            self.phut = 0
            self.gio += 1
        return self

    def __lshift__(self, other):
        self.giay += 1
        return f"{self.gio:02d}:{self.phut:02d}:{self.giay:02d}"
    
    def __rshift__(self, other):
        self.giay += 1
        return f"{self.gio:02d}:{self.phut:02d}:{self.giay:02d}"

if __name__ == "__main__":
    thoigian = ThoiGian(11, 59, 59)
    print(thoigian)
    thoigian += 1
    print(thoigian)
    print(thoigian >> 1)
    print(thoigian << 1)