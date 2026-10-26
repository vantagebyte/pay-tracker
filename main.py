
pay = 0
expense = 0


while True:
        

    print('1. Add pay')
    print('2. Add expense')
    print('3. View')
    print('4. Quit')

    choice = input('Pick an option: ')

    if choice == '4':
        break
    elif choice == '1':
        pay += float(input('Add pay: '))
    elif choice == '2':
        expense += float(input('Add expense: '))
    elif choice == '3':
        print(f'Pay total is : ${pay:.2f}')
        print(f'Expense total is : ${expense:.2f}')
    else:
        print('Invalid input. Please select a number from the menu.')

