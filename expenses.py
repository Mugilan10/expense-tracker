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
add_expense("Rice", 50, "Food")
add_expense("Bus",20,"Travel")
print(expenses)

with open("expenses.json","w")as f:
    json.dump(expenses, f)
print("Saved.")