'''
Project Name : Personal Expense Tracker

'''
import json
import os
import datetime
import matplotlib.pyplot as plt


# File path for storing data
DATA_FILE = "expenses.json"


# 1. Module for Data Management
def load_data():
    """Load expense data from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error reading the data file. It may be corrupted.")
        return []


def save_data(expenses):
    """Save expense data to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)


# 2. Module for Adding, Editing, and Deleting Expenses
def add_expense(expenses):
    """Add a new expense."""
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g., Food, Transport): ").strip()
        description = input("Enter description: ").strip()
        date_str = input("Enter date (YYYY-MM-DD, leave blank for today): ").strip()
        if date_str:
            try:
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD.")
                return
        else:
            date = datetime.date.today()

        expenses.append({"amount": amount, "category": category, "description": description, "date": str(date)})
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input! Please try again.")


def delete_expense(expenses):
    """Delete an expense by index."""
    list_expenses(expenses)
    if not expenses:
        print("No expenses to delete!")
        return
    try:
        index = int(input("Enter the index of the expense to delete: "))
        if 0 <= index < len(expenses):
            expenses.pop(index)
            print("Expense deleted successfully!")
        else:
            print("Invalid index! Please try again.")
    except ValueError:
        print("Invalid input! Please Enter a Number.")


# 3. Module for Listing and Summarizing Expenses
def list_expenses(expenses):
    """Display all expenses."""
    if not expenses:
        print("No expenses to show!")
        return
    print("\n--- Expense List ---")
    for i, expense in enumerate(expenses):
        print(f"{i}. {expense['date']} | {expense['category']} | ${expense['amount']} | {expense['description']}")


def summarize_expenses(expenses):
    """Summarize expenses by category."""
    summary = {}
    for expense in expenses:
        summary[expense['category']] = summary.get(expense['category'], 0) + expense['amount']
    return summary


# 4. Module for Analytics
def show_category_summary(expenses):
    """Display a summary of expenses by category with a pie chart."""
    summary = summarize_expenses(expenses)
    if not summary:
        print("No expenses to summarize!")
        return
    if len(summary) < 2:
        print("Not enough data to show a meaningful pie chart.")
        return
    categories = list(summary.keys())
    amounts = list(summary.values())
    
    print("\n--- Expense Summary by Category ---")
    for category, amount in summary.items():
        print(f"{category}: ${amount:.2f}")

    # Plot pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title("Expense Breakdown by Category")
    plt.show()


def show_monthly_summary(expenses):
    """Display a summary of expenses by month."""
    monthly_summary = {}
    for expense in expenses:
        month = expense['date'][:7]  # Extract YYYY-MM
        monthly_summary[month] = monthly_summary.get(month, 0) + expense['amount']

    if not monthly_summary:
        print("No expenses to summarize!")
        return

    print("\n--- Monthly Expense Summary ---")
    for month, amount in monthly_summary.items():
        print(f"{month}: ${amount:.2f}")

    # Plot bar chart
    months = list(monthly_summary.keys())
    amounts = list(monthly_summary.values())
    plt.figure(figsize=(10, 6))
    plt.bar(months, amounts, color='skyblue')
    plt.xlabel("Month")
    plt.ylabel("Total Expenses ($)")
    plt.title("Monthly Expense Summary")
    plt.xticks(rotation=45)
    plt.show()


# 5. Main Menu
def main():
    expenses = load_data()
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. Delete Expense")
        print("3. View All Expenses")
        print("4. Show Category-wise Summary")
        print("5. Show Monthly Summary")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            delete_expense(expenses)
        elif choice == '3':
            list_expenses(expenses)
        elif choice == '4':
            show_category_summary(expenses)
        elif choice == '5':
            show_monthly_summary(expenses)
        elif choice == '6':
            save_data(expenses)
            print("Expenses saved. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


# Entry point
if __name__ == "__main__":
    main()
