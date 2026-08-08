class Car:
    def _init_(self,brand,model):
        self.brand=brand
        self.model=model
    def _str_(self):
        return f"Car(Brand:{self.brand},Model:{self.model})"
c=Car("BMW","Innova")
print(c)