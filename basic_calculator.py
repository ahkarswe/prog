def basic_calculation():
    while True:
        print("This is a calculator program with Python.")
        try:
            num1 = int(input("Please enter the first number:\n"))
            user_choice = input("What do you want to do for a mathematical operation (+, -, *, /):\n")
            if user_choice in ["+", "-", "*", "/"]:                            
                num2 = int(input("Please enter the second number to calculate:\n"))
                
                if user_choice == "+":
                    result = num1 + num2
                elif user_choice == "-":
                    result = num1 - num2
                elif user_choice == "*":
                    result = num1 * num2
                elif user_choice == "/":
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        print("Division by zero is not allowed.")
                        continue

                print(f"Your answer is {result}\n")
            else:
                print("Please enter a valid operation (+, -, *, /).")        
        except ValueError:
            print("You need to input an integer number (e.g., 1, 2, 3...).")
    
        user_exit = input("Do you want to restart (y/n)? ")
        if user_exit.lower() != "y":
            break

basic_calculation()
