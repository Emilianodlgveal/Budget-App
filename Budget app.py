class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = list()

    def __str__(self):
        self.printing = list()
        self.printing.append(str(self.category).center(30, '*') + '\n')
        for i in range(len(self.ledger)):
            self.printing.append(
                str(self.ledger[i]['description']).ljust(23)[0:23] + str(f'{self.ledger[i]["amount"]:.2f}').rjust(
                    7) + '\n')
        self.printing.append('Total: ' + str(f'{self.get_balance():.2f}'))
        return ''.join(self.printing)

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        return self.ledger

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for transactions in self.ledger:
            try:
                balance += (transactions['amount'])
            except:
                continue
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, description='Transfer to ' + category.category)
            category.deposit(amount, 'Transfer from ' + self.category)
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False


def create_spend_chart(categories):
    all_withdraw = 0

    finalist = list()
    chart = {'100| ': [' '] * len(categories), '90| ': [' '] * len(categories), '80| ': [' '] * len(categories),
             '70| ': [' '] * len(categories), '60| ': [' '] * len(categories), '50| ': [' '] * len(categories),
             '40| ': [' '] * len(categories), '30| ': [' '] * len(categories), '20| ': [' '] * len(categories),
             '10| ': [' '] * len(categories), '0| ': [' '] * len(categories)}

    for category in categories:
        for i in range(len(category.ledger)):
            if category.ledger[i]['amount'] < 0:
                all_withdraw += abs(category.ledger[i]['amount'])

    for category in categories:
        if (abs(category.ledger[1]['amount']) / all_withdraw) * 100 >= 100:
            chart['100| '][categories.index(category)] = 'o'
        if (abs(category.ledger[1]['amount']) / all_withdraw) * 100 >= 90:
            chart['90| '][categories.index(category)] = 'o'
        if (abs(category.ledger[1]['amount']) / all_withdraw) * 100 >= 80:
            chart['80| '][categories.index(category)] = 'o'
        if (abs(category.ledger[1]['amount']) / all_withdraw) * 100 >= 70:
            chart['70| '][categories.index(category)] = 'o'
        if (abs(category.ledger[1]['amount']) / all_withdraw) * 100 >= 60:
            chart['60| '][categories.index(category)] = 'o'
        if (abs(category.ledger[1]['amount']) / all_withdraw) * 100 >= 50:
            chart['50| '][categories.index(category)] = 'o'
        if (abs(category.ledger[1]['amount']) / all_withdraw) * 100 >= 40:
            chart['40| '][categories.index(category)] = 'o'
        if (abs(category.ledger[1]['amount']) / all_withdraw) * 100 >= 30:
            chart['30| '][categories.index(category)] = 'o'
        if (abs(category.ledger[1]['amount']) / all_withdraw) * 100 >= 20:
            chart['20| '][categories.index(category)] = 'o'
        if (abs(category.ledger[1]['amount']) / all_withdraw) * 100 >= 10:
            chart['10| '][categories.index(category)] = 'o'
        if (abs(category.ledger[1]['amount']) / all_withdraw) * 100 > 0:
            chart['0| '][categories.index(category)] = 'o'
    for key, item in chart.items():
        finalist += (key.rjust(5, ' ') + str('  '.join(item)) + '  \n')
    return 'Percentage spent by category' + '\n' + (''.join(finalist)) + \
           (str('   ' + '-----' + ('--') * len(categories)).rjust(10)) + '\n' + 'B  F  E  '.rjust(
        14) + '\n' + 'u  o  n  '.rjust(14) + \
           '\n' + 's  o  t  '.rjust(14) + '\n' + 'i  d  e  '.rjust(14) + '\n' + 'n     r  '.rjust(
        14) + '\n' + 'e     t  '.rjust(14) + '\n' + \
           's     a  '.rjust(14) + '\n' + 's     i  '.rjust(14)+ '\n'+ '     n  '.rjust(14)+ '\n'+ '      m  '.rjust(14)+\
           '\n'+'      e  '.rjust(14)+ '\n'+'      n  '.rjust(14)+ '\n'+'      t  '.rjust(14)


food = Category("Food")
entertainment = Category("Entertainment")
business = Category("poop")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))

# food = Category("Food")
# (food.deposit(1000, 'Initial deposit'))
# (food.withdraw(10.15, "groceries"))
# (food.withdraw(15.89, "restaurant and more food for dessert"))
# (food.get_balance())
# clothing = Category("Clothing")
# (food.transfer(50, clothing))
# (food.check_funds(20))
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)
#
# print(food.ledger)
# print(food)
