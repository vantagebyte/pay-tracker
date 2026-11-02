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
    
def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
        except ValueError:
            print('Please enter a number, e.g. 250 or 49.95')
            continue
        if amount <= 0:
            print('Amount must be more than 0')
            continue
        return amount
    
def choose_entry(prompt):
    try:
        number = int(input(prompt))
    except ValueError:
        print('Please enter a number.')
        return None
    if number < 1 or number > len(entries):
        print('No entry with that number.')
        return None
    return number - 1

entries = load_entries()    

while True:
        

    print('1. Add pay')
    print('2. Add expense')
    print('3. View')
    print('4. Delete entry')
    print('5. Edit entry')
    print('6. Quit')

    choice = input('Pick an option: ')

    if choice == '6':
        save_entries()
        break
    elif choice == '1':
        amount = get_amount('Pay: ')
        category = input('Category: ')
        entry = {'type': 'pay', 'amount': amount, 'category': category}
        entries.append(entry)
        save_entries()

    elif choice == '2':
        amount = get_amount('Amount: ')
        category = input('Category: ')
        entry = {'type': 'expense', 'amount': amount, 'category': category}
        entries.append(entry)
        save_entries()
       
    elif choice == '3':
        pay_total = 0
        expense_total = 0
        
        for i, entry in enumerate(entries, start=1):
            print(f"{i}. {entry['type']} - ${entry['amount']:.2f} - {entry['category']}")
            if entry['type'] == 'pay':
                pay_total +=  entry['amount']
            else:
                expense_total += entry['amount']
                
            

        print(f'Pay total is : ${pay_total:.2f}')
        print(f'Expense total is : ${expense_total:.2f}')
        balance_total = pay_total - expense_total
        print(f'Balance is : ${balance_total:.2f}')
        if balance_total < 0 :
            print("You're over budget")

    elif choice == '4':
        index = choose_entry('Entry number to delete: ')
        if index is None:
            continue
        removed = entries.pop(index)
        save_entries()
        print(f"Deleted: {removed['type']} - ${removed['amount']:.2f}")    

    elif choice == '5':
        index = choose_entry('Entry number to edit: ')
        if index is None:
            continue
        entry = entries[index]
        print(f"Editing: {entry['type']} - ${entry['amount']:.2f} - {entry['category']}")
        entry['amount'] = get_amount('New amount: ')
        entry['category'] = input('New category: ')
        save_entries()
        print('Entry updated.')


            
    else:
        print('Invalid input. Please select a number from the menu.')

