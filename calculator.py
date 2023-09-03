def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error"
    
def modulus(x, y):
    return x % y
    

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. modulus")

choice = input("Enter any one choice(1,2,3,4,5): ")

n1 = int(input("Enter first number: "))
n2= int(input("Enter second number: "))

if choice == '1':
    result = add(n1, n2)
    operation = '+'
elif choice == '2':
    result = subtract(n1, n2)
    operation = '-'
elif choice == '3':
    result = multiply(n1, n2)
    operation = '*'
elif choice == '4':
    result = divide(n1, n2)
    operation = '/'
elif choice == '5':
    result = modulus(n1, n2)
    operation = '%'    
else:
    print("Invalid choice")
    exit()

print(f"{n1} {operation} {n2} = {result}")
