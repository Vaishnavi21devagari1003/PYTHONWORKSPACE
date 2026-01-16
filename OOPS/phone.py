class Phone:
    def show_details(self):
        return f"Details of phone"

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def pho(self):
        print(f"The {self.color} {self.brand} is now Good!")

class TouchScreenPhone(Phone):
    def __init__(self, brand, color, screen_size):
        super().__init__(brand, color)   
        self.screen_size = screen_size   

    def show_details(self):
        return f"{self.brand} ({self.color}) with {self.screen_size}-inch touchscreen"

class StoragePhone(Phone):
    def __init__(self, brand, color, storage_capacity):
        super().__init__(brand, color)  
        self.storage_capacity = storage_capacity 

    def show_details(self):
        return f"{self.brand} ({self.color}) with {self.storage_capacity}GB storage"


# ---------- Example usage ----------
my_phone = Phone("RealMe", "White")
print(my_phone.brand)
print(my_phone.color)
my_phone.pho()

touch_phone = TouchScreenPhone("Samsung", "Black", 6.5)
print(touch_phone.show_details())

storage_phone = StoragePhone("iPhone", "Silver", 256)
print(storage_phone.show_details())