import json

expenses=[]
def add_expense(name, amount, category):
    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    return expense

def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def show_summary():
    if len(expenses) == 0:
        print("No expenses yet.")
        return
    print("\n--- Expenses ---")
    for e in expenses:
        print(f"{e['category']}: {e['name']} - Rs.{e['amount']}")
    print("----------------")

def show_total():
    total = 0
    for x in expenses:
        total += x["amount"]
    print(f"Total spending: Rs.{total}")

expenses = load_expenses()

while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Quit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        amount = input("Amount: ")
        category = input("Category: ")
        try:
            add_expense(name, float(amount), category)
            print("Added.")
            with open("expenses.json","w") as f:
                json.dump(expenses, f)
        except ValueError:
            print("Invalid amount, please enter a number")
    
    elif choice == "2":
        show_summary()
        show_total()

    elif choice == "3":
        break