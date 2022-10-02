"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, commission):
        self.name = name
        self.commission = commission

    def get_pay(self):
        pass

    def __str__(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, name, hours, rate, commission=""):
        super().__init__(name, commission)
        self.hours = hours
        self.rate = rate
    
    def get_pay(self):
        if self.commission != "":
            return (self.hours * self.rate) + self.commission.get_bonus()
        else:
            return self.hours * self.rate

    def __str__(self): 
        self.pay = self.get_pay()
        if self.commission != "":  
             return  f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and {self.commission} Their total pay is {self.pay}."
        else:   
            return f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour. Their total pay is {self.pay}."

class MonthlyEmployee(Employee):
    def __init__(self, name, salary, commission=""):
        super().__init__(name, commission)
        self.salary = salary

    def get_pay(self):
        if self.commission != "":
            return self.salary + self.commission.get_bonus()
        else:
            return self.salary

    def __str__(self):
        self.pay = self.get_pay()
        if self.commission != "":
            return f"{self.name} works on a contract of {self.salary} salary and {self.commission} Their total pay is {self.pay}."
        else:
            return f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.pay}."

class BonusCommission:
    def __init__(self, amount):
        self.amount = amount

    def get_bonus(self):
        return self.amount

    def __str__(self):
        return f"receives a bonus commission of {self.amount}"

class ContractCommission:
    def __init__(self, contract_amount, rate):
        self.contract_amount = contract_amount
        self.rate = rate
    
    def get_bonus(self):
        return self.contract_amount * self.rate

    def __str__(self):
        return f"receives a commission for {self.contract_amount} contract(s) at {self.rate}/contract."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlyEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlyEmployee('Renee', 3000, commission = ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee('Jan', 150, 25, commission = ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlyEmployee('Robbie', 2000, commission = BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee('Ariel', 120, 30, commission = BonusCommission(600))
