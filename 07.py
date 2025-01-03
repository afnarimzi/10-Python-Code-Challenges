class calculator:
    def add(self):
        return a+b
    def substract(self):
        return a-b 
    def divide(self):
        return a/b
cal=calculator()
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=input("Enter a choice(+,- or /): ")  
if c=='+':
    add=cal.add()
    print(add) 
elif c=='-':
    substract=cal.substract()
    print(substract) 
else:
    divide=cal.divide()
    print(divide)

