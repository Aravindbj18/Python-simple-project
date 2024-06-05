
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 100,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 150,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 200,
    }
}

#total resources ......
profit=0
resources ={
    "water":500,
    "milk":200,
    "coffee":100

}
# check the resources, ingredients ........
def check_resources(order_ingredients):
    for item in order_ingredients:#water #milk #coffee
        if order_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough{item}")
            return False
    return True

#collecting the coins and adding the total ........
def process_coins():
    print("please insert the coins.")
    total = 0
    coins_five=int(input("How many 5rs coin?: "))#1
    coins_ten=int(input("How many 10rs coin?: "))#1
    coins_twenty=int(input("How many 20rs coin?: "))#1
    total=coins_five*5 + coins_ten*10 + coins_twenty*20
    return total

#payment updation .......
def is_payment_successful(money_received,coffee_cost):
    if money_received>=coffee_cost:
        global profit
        profit +=coffee_cost
        change=money_received-coffee_cost
        print(f"Here is your RS{change} in change.")
        return True
    else: 
        print("Sorry that's not enough money.Money Refunded.")
        return False    

 # selected coffe making  ........
def make_coffee(coffe_name,coffee_ingredients):
    for item in coffee_ingredients:
        resources[item]-= coffee_ingredients[item]  
    print(f"Here is your(coffee_name)☕.. Enjoy !!!")      
    
#There is a while loop its print continues then press off the loop can stop .......
is_on=True
while is_on:
    choice=input("What would you llike to have? (latte/espresso/cappuccino):")
    if choice == "off":
        is_on=False
    elif choice=="report":
        print(f"Water={resources['water']}ml")
        print(f"Milk={resources['milk']}ml")
        print(f"Coffee={resources['coffee']}g")
        print(f"Money=RS{profit}")

    else:
       coffee_type = MENU[choice]
       print(coffee_type)
       if check_resources(coffee_type['ingredients']):
          payment=process_coins()
          if is_payment_successful(payment,coffee_type['cost']):
              make_coffee(choice,coffee_type['ingredients'])

           

      

