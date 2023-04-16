MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_report():
    print(resources)
    coffee()
def check_resources(user_input):

    if user_input == 'espresso':
        MENU[user_input]["ingredients"]["milk"] = 0

    for resource in resources:
        if resources[resource] < MENU[user_input]["ingredients"][resource]:
            print(f"Sorry there is not enough {resource}")
            coffee()

def calculate_bill(user_input):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    inserted_amount = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)
    item_cost = MENU[user_input]["cost"]
    if inserted_amount < item_cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is ${round(inserted_amount - item_cost, 2)} in change")
        print(f"Here is your ${user_input} ☕ Enjoy!")

def update_resources(user_input):
    for resource in resources:
        if MENU[user_input]["ingredients"][resource]:
            resources[resource] -= MENU[user_input]["ingredients"][resource]
        else:
            resources[resource] -= 0

machine_off = False

while not machine_off:
    def coffee():
        user_input = input("What would you like? (espresso/latte/cappuccino): ")
        if user_input == "off":
            global machine_off
            machine_off = True
            return
        elif user_input == "report":
            check_report()
        else:
            check_resources(user_input)
            calculate_bill(user_input)
            update_resources(user_input)
    coffee()
