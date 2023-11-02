class Account():
    def __init__(self, id):
        self._id = id
        # with open('knights.txt') as knights:
        #     for rLine in knights:
        #         line = rLine.strip()
        #         id, balance, description = line.split(":")
        #         if id == self._id:
        #             self._balance = balance
        #             self._decription = description
        #             break

    # Id Getters & Setters
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    
    # Balance Getters & Setters
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, balance):
        self._balance = balance
    

    # Description Getters & Setters
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, description):
        self._description = description


    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount MUST be Greater than 0")
    
    def withdraw(self, amount):
        if amount > 0 and amount < self._balance:
            self._balance -= amount
        else:
            print("Deposit amount MUST be Greater than 0")
    

    def transfer(self, amount, toAccount):
        if self._balance > amount:
            self._balance -= amount
            toAccount.deposit(amount)
        else:
            print("You MUST have the FUNDS to TRANSFER")
    
    def print(self):
        print(f"Id: {self.id}")
        print(f"Balance: {self.balance}")
        print(f"Description: {self.description}")

b1 = Account(1)
b2 = Account(2)
b1._balance = 1000
b1.description = "Savings"
b1.deposit(100)
b1.withdraw(2000)
print(b1.print())
