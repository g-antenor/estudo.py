from abc import ABC, abstractmethod
from datetime import datetime

class Client:
    def __init__(self, address):
        self._address = address
        self._account = []
    
    def transaction(self, account, transaction):
        transaction.register(account)

    def add_account(self, account):
        self._account.append(account)

class Person(Client):
    def __init__(self, cpf, name, date_birth, address):
        self._name = name
        self._date_birth = date_birth
        self._cpf = cpf
        self.address = address

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def name(self):
        return self._name

class Account:
    def __init__(self, number, client):
        self._funds = 0
        self._number = number
        self._agency = '0001'
        self._client = client
        self._historic = Historic()

    @classmethod
    def new_account(cls, client, number):
        return cls(client, number)
    
    @property
    def funds(self):
        return self._funds

    @property
    def number(self):
        return self._number
    
    @property
    def agency(self):
        return self._agency
    
    @property
    def client(self):
        return self._client
    
    @property
    def historic(self):
        return self._historic
    
    def withdraw(self, value):
        balance = self.funds
        if value > balance:
            print("Insufficient funds")
            
        elif value > 0:
            self._funds -= value
            print('Withdrawal successfully!')
            return True
        else:
            print('Withdraw fail, try again!')

        return False
    
    def deposit(self, value):
        if value > 0:
            self._funds += value
            print('Deposit successfully!')
            return True
        else:
            print('Deposit fail, try again!')

        return False
            
class CheckingAccount(Account):
    def __init__(self, number, client):
        super().__init__(number, client)
        self.minimum_value = 500
        self.limit_withdraw = 3

    def withdraw(self, value):
        cont_withdraw = len(
            [times for times in self.historic.transactions if times['types'] == Withdraw.__name__]
        )

        if cont_withdraw > self.limit_withdraw:
            print('Number maximum withdraw!')
        elif value > self.minimum_value:
            print('Amount greater than withdrawal limit')
        else:
            return super().withdraw(value)

        return False
    
    def __str__(self):
        return f"""\
        Agency: {self.agency}
        C/C: {self.number}
        Owner: {self.client} 
        """

class Historic:
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions
    
    def add_transactions(self, transaction):
        self.transactions.append(
            {
                'type': transaction.__class__.__name__,
                'value': transaction.value,
                'date': datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            }
        )

    def view_transactions(self):
        for list in self.transactions:
            for key, value in list.items():
                print(f"""
                {value}:
                R${value:.2f}
                Date: {value}
                """)
            
class Transactions(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod 
    def register(self, account):
        pass

class Withdraw(Transactions):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
    
    def register(self, account):
        result_withdraw = account.withdraw(self.value)

        if result_withdraw:
            account.historic.add_transactions(self)

class Deposit(Transactions):

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
    
    def register(self, account):
        result_deposit = account.deposit(self.value)

        if result_deposit:
            account.historic.add_transactions(self)

def menu():
    return """
    Select Operation:

    [1] - Deposit
    [2] - Withdraw
    [3] - Extract

    [NA] - New Account
    
    [x] - Exit
    
    >>> """

def new_user(users):
    cpf = input('CPF: ')
    result_verify = filter_user(cpf, users)
    if result_verify:
        print(f'User with CPF: {cpf}, already registred!')
        return
    
    name = input('Full name: ')
    date_birth = input('Date birth: ')
    address = input('Address: ')
    Person(name = name, cpf = cpf, date_birth = date_birth, address = address)
    print('Successfully registered!')
    return { 'Name': name, 'cpf': cpf, 'date_birth': date_birth, 'address': address }

def create_account(users, accounts):
    number = 0
    for item in users:
        number += 1
    
    cpf = input('CPF: ')
    cliente = filter_user(cpf, users)
    if cliente:
        account = CheckingAccount.new_account(client=cliente, number=number)
        accounts.append(account)
        print('Successfully create Account!')
        return
    else:
        print('Customer not found!')

def filter_user(user_cpf, users):
    teste = None
    for list_users in users:
        for key, value in list_users.items():
            if key == 'cpf' and user_cpf == value:
                teste = value
    return teste
                
def withdraw(account):
    value = float(input("""
    Value for withdraw:
            
    >>> """))
    trasation = Withdraw(value)
    Client.transaction(account, trasation)

def deposit(account):
    value = float(input("""
    Value for deposit:
            
    >>> """))
    trasation = Deposit(value)
    Client.transaction(account, trasation)

def main():
    users = []
    accounts = []

    user = new_user(users)
    users.append(user)
    confirm_create = input("""
    Create account?\t
    [Y] - Yes\t [N] - No\t
    
    >>> """)
    if confirm_create == 'y':
        create_account(users, accounts)
    elif confirm_create == 'n':
        print('Goodbye!')
    else:
        print('Try again!')
        return

    while True:
        option = input(menu())
        if option == '1':
            deposit(accounts)
        elif option == '2':
            withdraw(accounts)
        elif option == '3':
            Historic.view_transactions()
        elif option == 'na':
            create_account(users, accounts)
        elif option == 'x':
            break
        else:
            print('Error')

main()