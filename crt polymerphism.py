class Calculator:
     def add(self,a,b=0):
          return a+b 
c = Calculator()
print(c.add(10))
print(c.add(10,20))


class Calculator:
        def add(self, *numbers):
            print(sum(numbers))
obj = Calculator()
obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30)
obj.add(10, 20, 30, 40)
obj.add(10, 20, 30, 40, 50)

