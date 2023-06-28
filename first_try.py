
#functions

def transaction_type():
    print('1. Purchases')
    print('2. Sale')
    print('3. Purchases Return')
    print('4. Sales Return')

print('Hello, Welcome to Accounting Bookkeeping software')
transaction_type()
transaction_type_input = input('Enter Transaction type: ')
if transaction_type_input == '1':
    customer_name = input("Enter Customer's Name: ")
    item_purchased_name = input('Enter Item Name: ')
    price_of_purchased_item = input('Enter Price: ')
print(customer_name)
print(item_purchased_name)
print(price_of_purchased_item)
elif transaction_type_input == '2':

