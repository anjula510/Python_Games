
## Parent Class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_user_details(self):
        print('Personal details')
        print('')
        print(f'Name; {self.name}')
        print(f'Age; {self.age}')
        print(f'Gender; {self.gender}')


##Child Class
class Bank(User):
    def __init__(self, name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposite(self,amount):
        self.amount = amount
        self.balance = self.balance + amount
        print(f'Account balance has updated:{self.balance}')

    def withdraw(self,amount):
        self.amount = amount
        if self.balance < self.amount:
            print(f'This amount can not be withdrawed. Your balance is {self.balance} ')

        else:
            self.balance = self.balance - self.amount
            print(f"Amount is updated. Your Current balance is {self.balance}")

    def view_balance(self):
        self.show_user_details()
        print(f"Amount is updated. Your Current balance is {self.balance}")





main = Bank('Jane', 23, 'Male')
main.deposite(100)
main.deposite(50)
main.deposite(60)
main.withdraw(180)
main.view_balance()