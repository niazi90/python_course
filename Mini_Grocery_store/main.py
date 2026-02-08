''' Mini Grocery store program 
 write a menu based python program for a small grocery store
 Menu
 1 Add item
 2 view items
 3 buy items
 4 Exit
 Requirenment 
 Take item name ,price,and quantity from the user
 store item in a dictionary 
 show all items using a loop
 when buying an item :
 check if the item exist
check if quantity is avaiable
calculate total price 
 use the while loop to keep the program runing '''


print(".........Wellcome to Small Grocery Store..............")
item_store=[{"name":"Apple","price":100,"quantity":12},
            {"name":"Banana","price":50,"quantity":20},
            {"name":"Orange","price":80,"quantity":15}]


while True:
    print("---------This is the menu of our Store:------")
    print("__________1 Add item_______________")
    print("__________2 View items_____________")
    print("__________3 Buy items_____________")
    print("__________4 Exit_______________")
    choice=int(input("Enter your choice: "))
    if choice == 1:
        print("========Add Item to the store==========")
        name=input("Enter item name: ")
        price=int(input("Enter item price:"))
        quantity=int(input("Enter item Quantity:"))
        item_store.append({"name":name,"price":price,"quantity":quantity})
        print("==========Item added successfully!==========")
    elif choice == 2:
        print("========Items in the store:===========")
        for item in item_store:
            print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
    elif choice == 3:
        selection=input("=======Which item do you want to buy?========= ")
        found=False
        for item in item_store:
            if selection == item["name"]:
                found=True
                qty=int(input("Enter quantity to buy: "))
                if qty <= item["quantity"]:
                    total_price = qty * item["price"]
                    item["quantity"] -= qty
                    print(f"You bought {qty} {item['name']}(s) for a total of {total_price}.")
                else:
                    print("__Sorry, not enough quantity available.____")
                break
        if not found:
            print("========Item not available.=========")
    elif choice == 4:
        print("*************Exiting the program. Thank you for visiting!***********")
        break
    else:
        print("__Invalid choice. Please try again._______")


