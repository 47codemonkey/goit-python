first_number = int(input('Enter first number: '))
operator = input('Enter operator: ')
second_number = int(input('Enter second number: '))

if operator == '+':
    sign_equally = input("Enter '=' if u wanna see result: ")
    if sign_equally == '=':
        print(first_number + second_number)
    else: 
        print('better luck next time')
elif operator == '-':
    sign_equally = input("Enter '=' if u wanna see result: ")
    if sign_equally == '=':
        print(first_number - second_number)
    else: 
        print('bye bye')  
elif operator == '/':
    sign_equally = input("Enter '=' if u wanna see result: ")
    if sign_equally == '=':
        print(first_number // second_number)
    else: 
        print('go to hell')  
elif operator == '*':
    sign_equally = input("Enter '=' if u wanna see result: ")
    if sign_equally == '=':
         print(first_number * second_number)
    else: 
        print("I like u, I'll kill u last") 
