class Vehicle:
    def _init_(self,brand):
        self.brand=brand
class Car(Vehicle):
    def _init_(self,brand,model):
        super()._init_(brand)
        self.model=model
    def display_info(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
car=Car("Toyota","Innova")
car.display_info()                                  