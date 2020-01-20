'''CAFE BILLING SYSTEM'''

from time import sleep#to bringout more reality ;)

#adding items to the system in the way to access from array

#drinks
orange_juice = 0
apple_juice = 1
lemonade = 2
filter_coffe = 3
tea = 4
hot_chocolate = 5

#snacks
cakes = 6
cookies = 7
sandwiches = 8
crisps = 9
###############################################################################


#price of every item in it's position in array    
CafePriceList = [2.50, 2.00, 1.50, 2.20, 1.75, 2.25, 2.50, 1.25, 3.00, 1.00]

# The name CafePriceList is also 'global' in scope. 

###############################################################################



###############################################################################
# The function items() is the main function that implements the 'glue' that
# holds the whole program together
# Its job is to repeatedly display a menu from which the user selects an option
# and to call the function that implements the option selected by the user.

def items () :

    # The name theOrder refers to a list containing information about how
    # many items of each kind the client has requested so far
    # So theOrder[Orange_juice] tells us how many Orange_juice items are in the order
    # An empty order list contains 0 items of each kind:

    # This name is local to the function items(), so to make the contents of
    # theOrder accessible to other functions we must pass it as a parameter
    
    theOrder = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    print("Welcome to the Cafe simulation")
    while True :  # Display the menu
        print ("\nPlease choose from the following menu:")
        print ("  Enter 1 to exit the system")
        print ("  Enter 2 to add items to your order")
        print ("  Enter 3 to remove items from your order")
        print ("  Enter 4 to checkout")
        print ("  Enter 5 to empty your order list")
        print ("  Enter 'i' to display your order list")
        print ("  Enter 'm' to show the menu card")

        choice = input("Enter your choice:")    # Collect what the user types in
        print ()
        # Carry out the user's wishes
        # (This part is incomplete)
        if choice == '1' :
            break
        elif choice == '2' :
            addItems (theOrder)
            showOrder (theOrder)
        elif choice == '3' :
            showOrder (theOrder)
            removeItems (theOrder)
            
        elif choice == '4' :
            showOrder (theOrder)
            totalOrder = priceOf (theOrder)
            discount = totalOrder * getDiscount ()
            totalOrder = totalOrder - discount
            sleep(1)#just for a thrill or to feel like actuall
            
            print ("Please proceed to payment: you owe £", totalOrder)
            
            
            #additional feature added payment methods
            print("""Select your payment type
              1.cash
              2.card""")
            payment = input(">")
            if payment == '1':
                #additional feature added tip adding
                print("Do you like to add a tip:")
                add_tip = input("Y or N:")
                if add_tip == "Y" or add_tip == "y":
                    tip = float(input("Add tip:£"))
                    totalOrder = totalOrder + tip
                    print("tip amount of £",tip,"added to your bill")
                    print ("Please proceed to payment: you owe £", totalOrder, "with tip")
                    pass
                if add_tip == "N" or add_tip == "n":
                    print("Please proceed to payment: you owe £", totalOrder, "without tip")
                    pass
                rcvd_cash = float(input("Amount received:£ "))
                if rcvd_cash > totalOrder:
                    balance = rcvd_cash - totalOrder
                    print("Change given £",balance)
                print ("\nSimulated payment")
                print ("Thank you")
                print ()
                removeAllItems (theOrder)
                showOrder (theOrder)
            if payment == '2':
                print("if your total bill is < £10, then there should be an extra charge of 60p...")
                if totalOrder < 10.00:
                    totalOrder += 0.60
                    print ("Please proceed to payment: you owe £", totalOrder)
                print("Adding your card...")
                #additional feature added tip adding
                print("Do you like to add a tip:")
                add_tip = input("Y or N:")
                if add_tip == "Y" or add_tip == "y":
                    tip = float(input("Add tip:£"))
                    totalOrder = totalOrder + tip
                    print("tip amount of £",tip,"added to your bill")
                    print ("Please proceed to payment: you owe £", totalOrder, "with tip")
                    pass
                if add_tip == "N" or add_tip == "n":
                    print("Please proceed to payment: you owe £", totalOrder, "without tip")
                    pass
                sleep(2)
                print("\nCard added...\nEnter your pin..")
                pin = input("pin:")
                if pin == 1234:
                    sleep(1)
                    print("Payment processing...please wait...")
                    sleep(3)
                    print ("\nSimulated payment")
                    print ("Thank you")
                    print ()
                    removeAllItems (theOrder)
                    showOrder (theOrder)
                else:
                    sleep(1)
                    print("Payment processing...please wait...")
                    sleep(3)
                    print ("\nSimulated payment")
                    print ("Thank you")
                    print ()
                    removeAllItems (theOrder)
                    showOrder (theOrder)


        elif choice == '5' :
            removeAllItems (theOrder)
            showOrder (theOrder)
        #for displaying our order list whenever we wanted
        elif choice == "I" or choice == "i":
            showOrder(theOrder)
        elif choice == "M" or choice == "m":
            menuCard()
        else:
            print("[!]Please enter a valid option\n")
    print ("\nThank you for using the simulation")

###############################################################################





def showOrder (order) :
    # Display the current contents of the client's shopping basket
    if sum(order) == 0 :
        print ("order list is empty")
    else :
        #drinks
        num_orange_juice = order[orange_juice]
        print (num_orange_juice, " Orange juice at £", CafePriceList[orange_juice], "each")
        num_apple_juice = order[apple_juice]
        print (num_apple_juice, " Apple Juice at £", CafePriceList[apple_juice], "each")
        num_lemonade = order[lemonade]
        print (num_lemonade, " Lemonade at £", CafePriceList[lemonade], "each")
        num_filter_coffe = order[filter_coffe]
        print (num_filter_coffe, " Filter coffee at £", CafePriceList[filter_coffe], "each")
        num_tea = order[tea]
        print (num_tea, " Tea at £", CafePriceList[tea], "each")
        num_hot_chocolate = order[hot_chocolate]
        print (num_hot_chocolate, " Hot chocolate at £", CafePriceList[hot_chocolate], "each")
        #snacks
        num_cakes = order[cakes]
        print(num_cakes," Cakes at £",CafePriceList[cakes], "each")
        num_cookies = order[cookies]
        print(num_cookies," Cookies at £",CafePriceList[cookies], "each")
        num_sandwiches = order[sandwiches]
        print(num_sandwiches," Sandwiches at £",CafePriceList[sandwiches], "each")
        num_crisps = order[crisps]
        print(num_crisps," Crisps at £",CafePriceList[crisps], "each")
        print ()
        price = priceOf(order)
        print ("Total price of your order is £", price)
    print ()




def addItems (order) :
    # Ask the user what kind of items (s)e wishes to add (orange juice, cakes, etc)
    
    print ("What would you like to eat/drink today :) ?")
    print ("You may add one item at a time")
    menuCard()
    menuChoice = input ("Enter the item number:")
    # Before we can proceed we must check that the user has entered a selection
    # that is on our menu. For this we need a list of valid menu choices
    validChoices = ["0","1","2","3","4","5","6","7","8","9"]
    # We can only use what the user has typed in if it is a valid menu option
    while menuChoice not in validChoices :
        menuChoice = input ("Item not available: please try again: ")
    # The loop will continue executing until the string entered by the user
    # matches one of the valid menu options
    # Since each of these is a string representation of an integer it is
    # safe to 'convert' the menu choice to an integer ticket type
    item_type = int(menuChoice)
            
    # Then ask how many
    item_qty = input ("How many would you like to add? ")
    # Only use the user's input if it's a non-negative whole number
    # This can be checked by testing to see whether the only characters
    # it contains are digits
    while not item_qty.isdigit() :
        item_qty = input ("Please enter available item number from menu card[!]: ")
    # The loop will continue executing until the string entered by the user
    # contains only digits, at which point it can be 'converted' to an int
    item_qty = int (item_qty)
    # Now we can add items to the order
    order [item_type] = order[item_type] + item_qty




def removeItems (order) :
    # Ask the user what kind of items (s)e wishes to remove (orange juice, cakes, etc)
    print ("What item would you like to remove?")
    print ("You may remove one item type at a time")
    menuCard()
    menuChoice = input ("Enter the item number to remove item:")
    # Before we can proceed we must check that the user has entered a selection
    # that is on our menu. For this we need a list of valid menu choices
    validChoices = ["0","1","2","3","4","5","6","7","8","9"]
    # We can only use what the user has typed in if it is a valid menu option
    while menuChoice not in validChoices :
        menuChoice = input ("That item is not available in your order list: please try again: ")
    # The loop will continue executing until the string entered by the user
    # matches one of the valid menu options
    # Since each of these is a string representation of an integer it is
    # safe to 'convert' the menu choice to an integer item type
    item_type = int(menuChoice)
            
    # Then ask how many
    item_qty = input ("How many would you like to remove? ")
    # Only use the user's input if it's a non-negative whole number
    # This can be checked by testing to see whether the only characters
    # it contains are digits
    while not item_qty.isdigit() :
        item_qty = input ("Please enter available item number from menu card[!]: ")
    # The loop will continue executing until the string entered by the user
    # contains only digits, at which point it can be 'converted' to an int
    item_qty = int (item_qty)
    # Now we must check that we can remove that many tickets from the basket
    if order [item_type] < item_qty :
        print ("Sorry: there are only", order [item_type], "items in your order")
    else:
        order [item_type] = order [item_type] - item_qty




def removeAllItems (order) :
    # Empties the order

    orderSize = len(order)
    for i in range (orderSize) :
        order[i] = 0



def priceOf (order) :
    # Calculate the total price of the itemss in the order in pounds
    # (This will be obtained by multiplying the number of each ticket type
    #  in the order by its price and adding together the results of all 
    #  these multiplications to get the total price for the order)
    totalPrice = 0.00
    length = len(order)
    for index in range (length) :
        price = order[index] * CafePriceList[index]
        totalPrice = totalPrice + price
    # Once the total is obtained it should be and returned to the
    # function that called priceOf
    return totalPrice


def getDiscount () :
    discountLevel = 0   # Start by assuming there's no discount
    print ("Are you elgible for a discount?")
    eligible = input ("Enter Y or N:")
    if eligible == "Y" or eligible == "y" :
        discType = input ("Enter 1 for staff discount, 2 for loyalty discount:")
        if discType == "1" :
            discountLevel = 0.10
            print("discount of £", discountLevel, "applied")
        elif discType == "2" :
            discountLevel = 0.05
            print("discount of £", discountLevel, "applied")
    if eligible == "N" or eligible == "n":
        discountLevel = 0.00
        print("discount not applied")
    return discountLevel

def menuCard():#menu card or items list== to make more code user friendly
    print("-------------Cafe Menu Card-------------")
    print("No__Items _________________________Price__")
    print("----------------DRINKS------------------")
    print("""0.Orange Juice                    £2.50   
1.Apple Juice                     £2.00 
2.Lemonade                        £1.50
3.Filter Coffee                   £2.20
4.Tea                             £1.75
5.Hot Chocolate                   £2.25""")
    print("----------------SNACKS------------------")
    print("""6.Cakes                           £2.50   
7.Cookies                         £2.50 
8.Sandwiches                      £1.25
9.Crisps                          £2.20""")

def bill(order):
    if sum(order) != 0:
        


items ()
