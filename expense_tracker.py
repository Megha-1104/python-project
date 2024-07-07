import json
from datetime import datetime


class Expense:
    """
    Represents a single expense record.

    Attributes:
        date (str): The date of the expense in YYYY-MM-DD format.
        category (str): The category of the expense.
        amount (float): The amount of the expense.
        description (str): An optional description of the expense.
    """


    def __init__(self, date, category, amount, description=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __repr__(self):
        return f"Expense(date={self.date}, category={self.category}, amount={self.amount}, description={self.description})"
    


class ExpenseManager:
    """
    Manages a collection of expenses.

    Methods:
        add_expense(expense): Adds an expense to the collection.
        load_expenses(): Loads expenses from a file.
        save_expenses(): Saves expenses to a file.
        get_expenses(): Returns all expenses.
        get_expenses_by_category(category): Returns expenses for a given category.
        get_monthly_summary(year, month): Returns the total and detailed expenses for a given month.
    """

    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Expense(**exp) for exp in data]
        except FileNotFoundError:
            return []

    def save_expenses(self):
        with open(self.filename, "w") as file:
            json.dump([exp.__dict__ for exp in self.expenses], file)

    def get_expenses(self):
        return self.expenses

    def get_expenses_by_category(self, category):
        return [exp for exp in self.expenses if exp.category == category]

    def get_monthly_summary(self, year, month):
        monthly_expenses = [exp for exp in self.expenses if exp.date.startswith(f"{year}-{month:02}")]
        total = sum(exp.amount for exp in monthly_expenses)
        return total, monthly_expenses
    

def input_expense():
    while True:
        try:
            date = input("Enter the date (YYYY-MM-DD): ")
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please try again.")

    category = input("Enter the category: ")

    while True:
        try:
            amount = float(input("Enter the amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    description = input("Enter a description (optional): ")
    return Expense(date, category, amount, description)


def main():
    manager = ExpenseManager()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Expenses by Category")
        print("4. View Monthly Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            expense = input_expense()
            manager.add_expense(expense)
        elif choice == '2':
            for expense in manager.get_expenses():
                print(expense)
        elif choice == '3':
            category = input("Enter category: ")
            expenses = manager.get_expenses_by_category(category)
            for expense in expenses:
                print(expense)
        elif choice == '4':
            year = int(input("Enter year: "))
            month = int(input("Enter month: "))
            total, expenses = manager.get_monthly_summary(year, month)
            print(f"Total Expenses for {year}-{month:02}: {total}")
            for expense in expenses:
                print(expense)

        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()