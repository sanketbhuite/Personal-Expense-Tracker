import datetime


expenses = []
def enter_data():
    catagary = input("Enter Catagary: ")
    amount = input("Enter amount: ")
    discription = input("Enter discription: ")
    return catagary,amount,discription

def add_expense(data):
    with open("expense.txt", "a+") as file:
        file.write("|".join(data) + "\n")

def view_expenses():
    with open("expense.txt", 'r') as file:
        print("catagary\tamount\tdiscription")
        for line in file:
            data = line.strip().split('|')
            if len(data) >= 3:
                print(data[0],"\t",data[1],"\t",data[2])
            else:
                print("Invalid data format in file.")

def view_summary():
    summary = {}
    try:
        with open("expense.txt", 'r') as file:
            for line in file:
                data = line.strip().split('|')
                if len(data) >= 3:
                    category, amount, _ = data
                    amount = float(amount)
                    if category in summary:
                        summary[category] += amount
                    else:
                        summary[category] = amount
    except FileNotFoundError:
        print("Expense file not found.")

    if summary:
        print("Category\tTotal Amount")
        for category, total in summary.items():
            print("",category,"\t",total)
    else:
        print("No expenses recorded.")
              
while True:
    print("\nPersonal Expense Tracker")
    print("1. Add Expense :")
    print("2. View Expenses :")
    print("3. View Summary :")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        data = enter_data()
        add_expense(data)
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        view_summary()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
