import json

def save_entries():
    with open('data.json', 'w') as file:
        json.dump(entries, file)

def load_entries():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

entries = load_entries()    

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
        save_entries()

    elif choice == '2':
        amount = float(input('Amount: '))
        category = input('Category: ')
        entry = {'type': 'expense', 'amount': amount, 'category': category}
        entries.append(entry)
        save_entries()
       
    elif choice == '3':
        pay_total = 0
        expense_total = 0
        
        for entry in entries:
            print(f"{entry['type']} - ${entry['amount']:.2f} - {entry['category']}")
            if entry['type'] == 'pay':
                pay_total +=  entry['amount']
            else:
                expense_total += entry['amount']
            

        print(f'Pay total is : ${pay_total:.2f}')
        print(f'Expense total is : ${expense_total:.2f}')
    else:
        print('Invalid input. Please select a number from the menu.')

