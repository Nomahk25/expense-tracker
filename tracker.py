import csv
import os

FILENAME = 'expenses.csv'
FIELDS = ['date', 'category', 'description', 'amount']

def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()

def add_expense():
    date = input('Enter date (YYYY-MM-DD): ').strip()
    category = input('Enter category (e.g., Food, Transport): ').strip()
    description = input('Enter description: ').strip()
    while True:
        amount = input('Enter amount: ').strip()
        try:
            amount = float(amount)
            break
        except ValueError:
            print('Please enter a valid number for amount.')

    with open(FILENAME, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow({'date': date, 'category': category, 'description': description, 'amount': amount})
    print('Expense added successfully.')

def view_expenses():
    if not os.path.exists(FILENAME):
        print('No expenses recorded yet.')
        return
    with open(FILENAME, 'r') as f:
        reader = csv.DictReader(f)
        print(f'{"Date":<12} {"Category":<15} {"Description":<25} {"Amount":>10}')
        print('-'*65)
        total = 0
        for row in reader:
            print(f'{row["date"]:<12} {row["category"]:<15} {row["description"]:<25} {float(row["amount"]):>10.2f}')
            total += float(row["amount"])
        print('-'*65)
        print(f'{"Total":<52} {total:>10.2f}')

def main():
    initialize_file()
    while True:
        print('\nExpense Tracker Menu')
        print('1. Add Expense')
        print('2. View Expenses')
        print('3. Exit')
        choice = input('Choose an option (1-3): ').strip()
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print('Goodbye!')
            break
        else:
            print('Invalid option. Try again.')

if __name__ == '__main__':
    main()
