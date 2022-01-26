# Exercise 1

def shopping_cart():
    cart = []
    while True:
        print("\nWelcome to the shopping cart. What would you like to do?")
        choice = input("To add an item, enter 'a'\nTo remove an item, enter 'r'\nTo view all items, enter 'v'\nTo quit, enter 'q' ")
        if choice.lower() == 'a':
            new_item = input("What item would you like to add to your cart? ")
            cart.append(new_item)
            print(f'{new_item} has been added.')
        elif choice.lower() == 'r':
            remove_item = input("What item would you like to remove from to your cart? ")
            if remove_item in cart:
                cart.remove(remove_item)
                print(f'{remove_item} has been removed.')
            else:
                print(f'That item is not in your cart.')
                continue    
        elif choice.lower() == 'v':
            print (f'The items in your cart are: {cart}')
        elif choice.lower() == 'q':
            print (f'The items in your cart are: {cart}. Goodbye!')
            break
        else:
            print ("Please choose an option from above.")

shopping_cart()


#########################################
# Exercise 2
from calculations import sq_footage
from calculations import circumference

print(sq_footage())

print(circumference())


