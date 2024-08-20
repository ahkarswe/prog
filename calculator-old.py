def basic_calculation():
    while True:
        print("this is calculator program with python")
        try:
            num1 = int(input("Please enter Number:\n"))
            user_choice = (
                input("what do you want to do for mathematics operation (+, -, *, /)\n"))
            if user_choice in ["+", "-", "*", "/"]:
                num2 = int(input("Please Enter Number to culculate:\n"))

                if user_choice == "+":
                    add = num1 + num2
                    print(f"your answer is {add}\n")
                elif user_choice == "-":
                    subtract = num1 - num2
                    print(f"your answer is {subtract}\n")
                elif user_choice == "*":
                    multiply = num1*num2
                    print(f"your answer is {multiply}\n")
                elif user_choice == "/" and num2 != 0:
                    Reminder = num1/num2
                    modulus = num1 % num2
                    print(
                        f"your answer is {Reminder} and modulus is {modulus}\n")
                else:
                    print("Devided by 0 is not Allowed")
            else:
                print("please put correct operation")
        except ValueError:
            print("you need to put interger number eg. 1,2,3..")

        user_exit = input("Do you want to restart (y,n) ")

        if user_exit != "y":
            break


basic_calculation()
