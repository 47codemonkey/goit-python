while True:
        
    try:
        oper = input("Enter a number: ")
        operand1 = float(oper)
        break          
    except ValueError:
        print(f'{oper} is not a number!')
        
    
while True:
        
    operator = input("Enter an operator: ")
    if operator in ('+', '-', '*', '/'):
        operator = operator
            
    elif operator == ('='):
        print(operand1)
        break
    else:
        print(f'{operator} is not correct!')
        continue


    while True:
        
        try:
            oper = input("Enter a number: ")
            operand2 = float(oper)
            break          
        except ValueError:
            print(f'{oper} is not a number!')

    if operator == "+":
        operand1 = operand1 + operand2
    if operator == "-":
        operand1 = operand1 - operand2
    if operator == "*":
        operand1 = operand1 * operand2
    try:
        if operator == "/":
            operand1 = operand1 / operand2
    except ZeroDivisionError:
        print(f'division on {operand2} is not possible')
        continue
    


