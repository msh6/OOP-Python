from item import Item
from phone import Phone

item1 = Item("MyItem", 750, 6)

# Setting an Attribute
item1.name = "OtherItem"

# Getting an Attribute
print(item1.name)

print(item1.price)

item1.apply_increment(0.2)
item1.apply_discount()

print(item1.price)

item1.send_email()
