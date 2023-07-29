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
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
        
    @property
    def price(self):
        return self.__price
        
    @property
    # Property decorator = Read-only Attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    def calculate_total_price(self):
        return self.__price * self.quantity
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
        
    def apply_increment(self, inc_value):
        self.__price = self.__price + self.__price * inc_value
            
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
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
    
    def __connect(self, smtp_server):
        pass
    
    def __prepare_body(self):
        return f"""
        Hello Someone.
        We have {self.name} {self.quantity} times.
        Regards, Sohail
        """
        
    def __send(self):
        pass
    
    def send_email(self):
        self.__connect("")
        self.__prepare_body()
        self.__send()
        