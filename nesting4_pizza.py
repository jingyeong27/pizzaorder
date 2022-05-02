# another combine code
pizza = {
    'crust': ['thick', 'thin'],
    'toppings': ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese'],
    'size' : ['S', 'M', 'L']
}
print("==== Welcome to Python Pizza shop! ====")

pizza_size = input("What size pizza do you want? [S, M, L]  ===> ")
requested_size= []
requested_size.append(pizza_size)
# print(requested_crusts)
bill = 0
for requested_size in requested_size:
    if pizza_size == "S":
        bill += 15
    elif pizza_size == "M":
        bill += 20
    elif pizza_size == "L":
        bill += 25
    else:
        pizza_size = input("You can choose the size from S, M, and L. Please enter it again !! ===> " )
        requested_size = []
        requested_size.append(pizza_size)
        if pizza_size == "S":
            bill += 15
        elif pizza_size == "M":
            bill += 20
        elif pizza_size == "L":
            bill += 25

for requested_size in requested_size:
    if requested_size in pizza['size']:
        pizza_crust = input("what kind of crust do you want to have [thick, thin]  ===> ")
        requested_crusts = []
        requested_crusts.append(pizza_crust)
        
for requested_crust in requested_crusts:
    if requested_crust in pizza['crust']:
        toppings = input("what topping do you want to add [mushrooms/olives/green peppers/pepperoni/pineapple/extra cheese]===> ")
        requested_toppings = []
        requested_toppings.append(toppings)
        for requested_topping in requested_toppings:
            if requested_topping in pizza['toppings']:
                print("The composition of the pizza is",requested_size,"size /", requested_crust,"crust /", requested_topping + " pizza!" )
                print(f"===== Your total pizza price is ${bill}")
            else:
                print("Sorry,the topping you want to add is out of stock! Could you please choose another topping?")
                toppings = input("what topping do you want to add [mushrooms/olives/green peppers/pepperoni/pineapple/extra cheese]===> ")
    else :
        print("Sorry,the crust you want to add is out of stock! Could you please choose another crust?")
        requested_crusts = []
        pizza_crust = input("what kind of crust do you want to have [thick, thin]  ===> ")
        requested_toppings = []
        toppings = input("what topping do you want to add [mushrooms/olives/green peppers/pepperoni/pineapple/extra cheese]===> ")
        print("The composition of the pizza is " + pizza_crust,toppings + " pizza ")
        
order_way = input("Do you want packaging or delivery? ===> ")
if order_way == "packaging" :
    print("We offer a two-dollar discount for packaging.")
    print(f"==== ${bill-2} " + "Thank you. You can pick it up later")
else:
    del_adr = input("okay, Please enter your address ===>")
    print("Yes, then I will deliver " + del_adr + " to this address.")
    print("Thank you so much, I'll deliver it to you soon")
