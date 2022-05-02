#another combine code
pizza = {
'crust': ['thick','thin'],
'toppings': ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese'],
}
pizza_crust = input("what kind of crust do you want to have ===> ")
requested_crusts = []
requested_crusts.append(pizza_crust)
#print(requested_crusts)
for requested_crust in requested_crusts:
    if requested_crust in pizza['crust']:
        toppings = input("what topping do you want to add ===> ")
        requested_toppings = []
        requested_toppings.append(toppings)
        for requested_topping in requested_toppings:
            if requested_topping in pizza['toppings']:
                print("We are adding",requested_topping + ".")
            else:
                print("Sorry,the topping you want to add is out of stock! Could you please choose another topping?")
        print("\nWe have finished making your pizza")
                           
    else:
        print("Sorry,the crust you want to add is out of stock! Could you please choose another crust?")
        
order_way = input("Do you want packaging or delivery? ===> ")
if order_way == "packaging" :
    print("We offer a two-dollar discount for packaging.")
    print(f"==== ${bill-2} " + "Thank you. You can pick it up later")
else:
    del_adr = input("okay, Please enter your address ===>")
    print("Yes, then I will deliver " + del_adr + " to this address.")
    print("Thank you so much, I'll deliver it to you soon")
