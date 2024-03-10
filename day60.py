# Create a class representing a simple bank account with deposit and withdraw methods.


class BankAccount:
    """
    A class representing a simple bank account with deposit and withdraw methods.
    """

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount) -> int:
        """
        Deposit money into the account.

        Args:
            amount (int): The amount of money to deposit.

        Returns:
            int: The new balance.
        """
        self.balance += amount
        return self.balance

    def withdraw(self, amount) -> int:
        """
        Withdraw money from the account.

        Args:
            amount (int): The amount of money to withdraw.

        Returns:
            int: The new balance.
        """
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance


account = BankAccount(100)  # balance = 100
print(account.deposit(50))  # balance = 150
print(account.withdraw(100))  # balance = 50
print(account.withdraw(500))  # "Insufficient funds"
