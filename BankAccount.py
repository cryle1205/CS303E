class BankAccount:
    # REMEMBER TO MAKE YOUR DATA MEMBERS PRIVATE
    def __init__(self, name, initialAmount):
        self.__name = name 
        self.__initialAmount = initialAmount

    def withdraw(self, amount):
        self.withdraw = amount
        if self.withdraw >= self.__initialAmount:
            return self.__initialAmount
            self.__initialAmount -= amount
        else:
            return self.withdraw
            self.__initialAmount -= amount

    def deposit(self, amount):
        self.__initialAmount += amount

    def getAmount(self):
        return float(format(self.__initialAmount, ".2f"))

    def __str__(self):
        return "The " +  self.__name + " account currently has $" + str(self.getAmount())
