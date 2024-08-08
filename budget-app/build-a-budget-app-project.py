class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.ledger = []
    
    def __str__(self):
        obj_str=''
        num_of_star = 30-len(self.name)
        obj_str += '*' * int(num_of_star/2) + self.name + '*' * int(num_of_star - int(num_of_star/2))
        obj_str += '\n'
        for i in self.ledger:
            if len(i['description']) > 23:
                i['description'] = i['description'][:23]
            else:
                i['description'] += ' ' * int(23 - len(i['description']))
            obj_str += f"{i['description']}{i['amount']:>7.2f}"
            obj_str += '\n'
        obj_str += f"Total: {self.balance}"
        return obj_str
        

    def deposit(self, amount, description=''):
        self.balance += amount
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description=''):
        amount = -abs(amount)
        if self.balance + amount > 0:
            self.balance += amount
            self.ledger.append({'amount': amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, budget_category):
        if self.balance > amount:
            self.balance -= amount
            self.ledger.append({'amount': -amount, 'description': f'Transfer to {budget_category.name}'})
            
            budget_category.balance += amount
            budget_category.ledger.append({'amount': amount, 'description': f'Transfer from {self.name}'})
            return True
        return False
    
    def check_funds(self, amount):
        if self.balance < amount:
            return False
        return True

def create_spend_chart(categories):
    return_str = ''

    # 各カテゴリごとのspentを計算
    parts = []
    for category in categories:
        part = 0
        count = 0
        for i in category.ledger:
            if i['amount'] < 0:
                part += i['amount']
            if count == len(category.ledger)-1:
                parts.append(part)
            count += 1
    # カテゴリごとの割合を計算
    whole = sum(parts)
    for i, part in enumerate(parts):
        parts[i] = part/whole*100
    #print(parts)

    #バーチャート文字列を生成
    return_str += 'Percentage spent by category'
    return_str += '\n'
    for i in range(100,-1,-10):
        return_str += f"{str(i):>3}|"
        for part in parts:
            if part > i:
                return_str += f' o '
            else:
                return_str += ' '*3
        return_str += ' \n'
    
    #水平線
    return_str += ' ' * 4 + '---'*len(categories) + '-'
    return_str += '\n'

    # ラベル名の長さを一律に
    length = 0
    for i in categories:
        if len(i.name) > length:
            length = len(i.name)
    category_str = []
    for i in categories:
        if length > len(i.name):
            category_str.append(i.name+' '*int(length-len(i.name)))
        else:
            category_str.append(i.name)
    
    # カテゴリラベルの出力
    #print(category_str)
    return_str += ' '*4
    for i in range(length):
        for j in range(len(category_str)):
            return_str += f" {category_str[j][i]} "
        if j == len(category_str)-1 and i != length-1:
            return_str += ' \n'
            return_str += ' ' * 4
        else:
            return_str += ' '
    print(return_str)
    return(return_str)

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(2.00, 'handkerchief')
auto = Category('Auto')
auto.deposit(1000, 'deposit')
auto.withdraw(5.00, 'oil')
pc =  Category('PC')
pc.deposit(500,'PC')
pc.withdraw(100,'New PC')
print(food)
print(clothing)
print(auto)

create_spend_chart([food, clothing, auto, pc])