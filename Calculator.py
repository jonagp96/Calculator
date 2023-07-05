file = open('equation.txt', 'w')     #creation of file 'equation.txt'

while True:
    
    operator = input("Please insert the operation that would like to do (+, -, *, /): ")

    if operator in ("+", "-", "*", "/"):     #Choice of operation that would like to do
        try:
            number1 = float(input("Please enter your first number: "))
            number2 = float(input("Please enter your second number: "))

        except Exception:
            print("Invalid input. Please enter a number")
            continue
        
        #Sum function
        if operator == "+":
            result = number1 + number2
            equation = (f"{number1} {operator} {number2} = {result} \n")
            print(equation)


        #Substract function
        elif operator == "-":
            result = number1 - number2
            equation = (f"{number1} {operator} {number2} = {result} \n")
            print(equation)


        #Multiply function
        elif operator == "*":
            result = number1 * number2
            equation = (f"{number1} {operator} {number2} = {result} \n")
            print(equation)


        #Division function
        elif operator == "/":
            #ZeroDivisionError
            try:
                number1/number2
                pass
            except ZeroDivisionError:
                print("Error:Division by 0")
                continue
            result = number1 / number2
            equation = (f"{number1} {operator} {number2} = {result} \n")
            print(equation)
        
        file.write(equation)     #Add all equations entered into the text file 'equation.txt'
        
        #Ask user if would like to do another calculation or create a file to display all equations entered
        next_equation = input("Insert 1 create a new text file and display all equations or press any other key to continue with more operations ")
        
        #Creation of new file to store all ecuations entered. If file exists the ecuations will be inserted at the end of the data existed. 
        if next_equation == "1":
            new_text_file = input("Please enter the name of the new text file: ")
            file.close()
            with open('equation.txt', 'r') as file1: 
                with open(new_text_file, 'w') as file2:
                    for line in file1:
                        file2.write(line)
                        file.close()
                
                #Displays to user ecuations that were entered
                with open(new_text_file) as i:
                    display = i.read()
                    print("The following ecuations were entered:")
                    print(display)
                    
            break
            


          
            
    #Prints out a message if user entered a different symbol or key        
    else: 
        print("Invalid operation please make sure that you use the symbol (+) for add, (-) for substract, (*) for multyply or (/) for division")


file.close()
open('equation.txt', 'r')     #Allows user to read text file 'equation.txt'

       

    