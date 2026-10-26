import json

def save_entries():
    with open('data.json', 'w') as file:
        json.dump(entries, file)

pay = 0
expense = 0
entries = []    

while True:
        

    print('1. Add pay')
    print('2. Add expense')
    print('3. View')
    print('4. Quit')

    choice = input('Pick an option: ')

    if choice == '4':
        save_entries()
        break
    elif choice == '1':
        amount = float(input('Pay: '))
        category = input('Category: ')
        entry = {'type': 'pay', 'amount': amount, 'category': category}
        entries.append(entry)
        pay += amount
        save_entries()

    elif choice == '2':
        amount = float(input('Amount: '))
        category = input('Category: ')
        entry = {'type': 'expense', 'amount': amount, 'category': category}
        entries.append(entry)
        expense += amount
        save_entries()
       
    elif choice == '3':
        for entry in entries:
            print(f"{entry['type']} - ${entry['amount']:.2f} - {entry['category']}")

        print(f'Pay total is : ${pay:.2f}')
        print(f'Expense total is : ${expense:.2f}')
    else:
        print('Invalid input. Please select a number from the menu.')

