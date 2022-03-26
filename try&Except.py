def divide(a, b):
     try:
         return a/b
     except:
         print("You can't divide by zero.")


print(divide(5,4))
print(divide(3,0))
print(divide("a", 3))
