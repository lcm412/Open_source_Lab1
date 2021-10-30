def add(x, y):
  return x + y

def subtract(x, y):
  return x - y
  

#---------------------------------
print("Select operation.")
print("1.Add")
print("2.Subtract")

choice = input("Enter choice(1/2): ")

num1 = float(input("첫번째 숫자를 입력하시오: "))
num2 = float(input("두번째 숫자를 입력하시오: "))num1,"+",

if choice == '1':
  print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
  print(num1, "-", num2, "=", subtract(num1, num2))
  
else:
  print("틀린 입력을 하였습니다.")
