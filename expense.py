import os
import json
import matplotlib.pyplot as plt

# Expense categories (can be expanded)
categories = ["Groceries", "Transportation", "Utilities", "Entertainment", "Others"]

# Expense Data Storage
expense_data = {}

# File path for saving data
data_file = 'expenses.json'

# Function to load data from file
def load_data():
    global expense_data
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            expense_data = json.load(file)

# Function to save data to a file
def save_data():
    with open(data_file, 'w') as file:
        json.dump(expense_data, file)

# Function to add a new category
def add_category():
    new_category = input("Enter the new category name: ").strip()
    categories.append(new_category)
    print(f"New category '{new_category}' added successfully!")

# Function to record a new expense
def record_expense():
    try:
        amount = float(input("Enter the amount spent: "))
        if amount <= 0:
            print("Please enter a positive amount.")
            return
        
        print("Select an expense category:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        
        category_choice = int(input("Enter the number corresponding to your category: "))
        
        if category_choice < 1 or category_choice > len(categories):
            print("Invalid choice. Please try again.")
            return
        
        category = categories[category_choice - 1]
        description = input("Enter a brief description of the expense: ").strip()
        
        # Get today's date
        from datetime import date
        today = str(date.today())
        
        # Record the expense
        if today not in expense_data:
            expense_data[today] = []
        
        expense_data[today].append({
            "amount": amount,
            "description": description,
            "category": category
        })
        
        print(f"Expense recorded: {amount} for {category} - {description}")
        save_data()
    
    except ValueError:
        print("Invalid input! Please enter a valid number for the amount.")

# Function to show expense summary
def show_summary():
    print("\n---- Expense Summary ----")
    total_spent = 0
    category_totals = {category: 0 for category in categories}
    
    for date, expenses in expense_data.items():
        for expense in expenses:
            total_spent += expense["amount"]
            category_totals[expense["category"]] += expense["amount"]
    
    print(f"Total Amount Spent: ${total_spent:.2f}")
    print("Spending Breakdown by Category:")
    for category, total in category_totals.items():
        print(f"  {category}: ${total:.2f}")
    
    print("\nSelect a period for detailed view:")
    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")
    period_choice = input("Enter choice: ").strip()

    if period_choice == '1':
        date = input("Enter the date (YYYY-MM-DD): ").strip()
        if date in expense_data:
            daily_expenses = expense_data[date]
            print(f"\nExpenses for {date}:")
            for expense in daily_expenses:
                print(f"  - {expense['amount']} for {expense['category']} - {expense['description']}")
        else:
            print("No expenses recorded for this date.")
    elif period_choice == '2':
        print("Weekly summary feature is under development.")
    elif period_choice == '3':
        print("Monthly summary feature is under development.")
    else:
        print("Invalid choice.")

# Function to visualize expenses
def visualize_expenses():
    category_totals = {category: 0 for category in categories}
    
    for date, expenses in expense_data.items():
        for expense in expenses:
            category_totals[expense["category"]] += expense["amount"]
    
    categories_list = list(category_totals.keys())
    totals_list = list(category_totals.values())
    
    plt.figure(figsize=(8, 6))
    plt.pie(totals_list, labels=categories_list, autopct='%1.1f%%', startangle=140)
    plt.title("Expenses Breakdown by Category")
    plt.show()

# Main menu
def main_menu():
    load_data()
    
    while True:
        print("\n----- Expense Recording System -----")
        print("1. Record a new expense")
        print("2. View expense summary")
        print("3. Add a new category")
        print("4. View expense visualization (Pie chart)")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            record_expense()
        elif choice == '2':
            show_summary()
        elif choice == '3':
            add_category()
        elif choice == '4':
            visualize_expenses()
        elif choice == '5':
            print("Exiting the system...")
            break
        else:
            print("Invalid choice, please try again.")

# Start the program
if __name__ == "__main__":
    main_menu()
