import csv

class Item:
    # Creating a class attribute
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
        
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)
            
        for i in items:
            Item(
                name=i.get('name'),
                price= float(i.get('price')),
                quantity=float(i.get('quantity'))
            )
        
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False     
                    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

'''item = Item('Apple', 100, 1)

item.apply_discount()
print(item.price)

item2 = Item('Sony', 100, 1)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)
'''
'''print(item.name)
print(item.price)
print(item.quantity)
print(item.calculate_total_price())

print(Item.__dict__) # All the attributes at Class level
print(item.__dict__) # All the attributes at instance level
'''

'''item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
'''
#print(Item.all)

'''for instance in Item.all:
    print(instance.name)'''
    
'''Item.instantiate_from_csv()
print(Item.all)
print(Item.is_integer(7.0))'''

class Phone(Item):     
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes/methods
        super().__init__(
            name, price, quantity
        )
        
        # Run validations to the received arguments
        assert broken_phones >= 0, f"Quantity {broken_phones} is not greater than or equal to zero"
        
        # Assign to self object
        self.broken_phones = broken_phones
        
'''phone1 = Phone("jscPhonev10", 500, 5, 1)

print(Item.all)
print(Phone.all)'''