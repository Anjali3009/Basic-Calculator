def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        try:
            choice = input("Enter choice (1/2/3/4): ")
            if choice in ['1', '2', '3', '4']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"The result of addition is: {add(num1, num2)}")
                elif choice == '2':
                    print(f"The result of subtraction is: {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"The result of multiplication is: {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"The result of division is: {divide(num1, num2)}")
                
                # Ask if the user wants to perform another calculation
                next_calculation = input("Do you want to perform another calculation? (yes/no): ")
                if next_calculation.lower() != 'yes':
                    break
            else:
                print("Invalid Input")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
