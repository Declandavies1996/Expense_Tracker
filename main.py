# Initializ an empty List
expenses = []

# Function To Add An Expense
def add_expense(amount, description):
    expenses.append({"amount":amount, "description": description})
    print("Expense Added Successfully!")

# Function To View All Expenses
def view_expenses():
    if expenses:
        print("Expenses:")
        for idx, expense in enumerate(expenses, start=1):
            print(f"{idx}. Amount : ${expense['amount']}, Description : ${expense['description']}")
    
    else:
        print("No Expenses Logged")

# Main Loop
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        amount = float(input("Enter expense amount: "))
        description = input("Enter expense description: ")
        add_expense(amount, description)
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Exiting the Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")