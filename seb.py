
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} and its name is {pet_name}.")


describe_pet("horse", "kabayots")
describe_pet("bird", "wiwit")
describe_pet("turtle", "gongpa")



describe_pet("dog", "blackie")


describe_pet(pet_name="bens", animal_type="duck")


def describe_pet(pet_name, animal_type="lion"):
    print(f"I have a {animal_type} and its name is {pet_name}.")

describe_pet("dada")
describe_pet("berto", "fish")



def order_drink(drink, size="medium", iced=False):
    if iced:
        ice_text = "iced"
    else:
        ice_text = "hot"

    return f"Your order: {size} {ice_text} {drink}"


print(order_drink("milk"))
print(order_drink("white chocolate", size="large", iced=False))
print(order_drink("latte", size="small", iced=True))


def compute(operation, num1, num2=1):
    if operation == "add":
        return num1 + num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "subtract":
        return num1 - num2
    else:
        return "Invalid operation"


print(compute("add", 6, 9))
print(compute("multiply", num1=6, num2=9))
print(compute("subtract", 69))  
print(compute("divide", 6, 9)) 