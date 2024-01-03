class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def add_income(self, amount, description):
        if description not in self.incomes:
            self.incomes[description] = amount
        else:
            self.incomes[description] += amount

    def add_expense(self, amount, description):
        if description not in self.expenses:
            self.expenses[description] = amount
        else:
            self.expenses[description] += amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        print(f"Account Holder: {self.firstname} {self.lastname}")
        print(f"Total Income: {self.total_income()}")
        print(f"Total Expense: {self.total_expense()}")
        print(f"Account Balance: {self.account_balance()}")

# Example usage:
person_account = PersonAccount("John", "Doe")

person_account.add_income(1000, "Salary")
person_account.add_income(200, "Freelance Work")

person_account.add_expense(300, "Rent")
person_account.add_expense(50, "Groceries")

person_account.account_info()
