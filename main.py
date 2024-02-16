
import random


# class to retain beverage information
class BevRecipe():
# default values for initialization
    def __init__(self,
                 size="NoSize",
                 temp="NoTemp",
                 type="Notype",
                 liquid="NoMilk",
                 flavoring="NoFlavor"):
        self.bev_size = size
        self.bev_temp = temp
        self.bev_type = type
        self.bev_liquid = liquid
        self.bev_flavoring = flavoring
        self.price = 0.00

# getters and setters for beverage recipe information

    def get_recipe(self):
        if self.bev_type == "Drip":
            return_str = (f"a {self.get_size()} {self.get_temp()} {self.get_type()} coffee "
                f"with {self.get_flavoring()} sweetener.")
            return return_str
        if self.bev_type == "Americano" or self.bev_type == "Espresso":
            return_str = (f"a {self.get_size()} {self.get_temp()} {self.get_type()} "
                f"with {self.get_flavoring()} sweetener.")
            return return_str
        else:
            return_str = (f"a {self.get_size()} {self.get_temp()} {self.get_type()} "
                f"with {self.get_liquid()} milk and {self.get_flavoring()} sweetener.")
            return return_str

    def get_price(self):
        return self.price
        
    def get_size(self):
        return self.bev_size

    def get_temp(self):
        return self.bev_temp

    def get_liquid(self):
        if self.bev_type == "Americano" or self.bev_type == "Espresso":
            self.set_liquid("No")
        return self.bev_liquid

    def get_type(self):
        return self.bev_type

    def get_flavoring(self):
        return self.bev_flavoring

    def set_size(self, str):
        if str[0].upper() == "S":
            self.bev_size = "Small"
           
        if str[0].upper() == "M":
            self.bev_size = "Medium"
            
        if str[0].upper() == "L":
            self.bev_size = "Large"
          

    def set_type(self, str):
        if str[0].upper() == "L":
            self.bev_type = "Latte"
        if str[0].upper() == "C":
            self.bev_type = "Cappucino"
        if str[0].upper() == "A":
            self.bev_type = "Americano"
        if str[0].upper() == "E":
            self.bev_type = "Espresso"
        if str[0].upper() == "D":
            self.bev_type = "Drip"
    
    def set_liquid(self, str):
        if str[0].upper() == "W":
            self.bev_liquid = "Whole"
        if str[0].upper() == "N" and len(str) > 2:
            self.bev_liquid = "Non-Fat"
        if str[0].upper() == "O":
            self.bev_liquid = "Oat"
        if str[0].upper() == "A":
            self.bev_liquid = "Almond"
        if str[0].upper() == "N":
            self.bev_liquid = "None"
        
    def set_temp(self, str):
        if str[0].upper() == "H":
            self.bev_temp = "Hot"
        if str[0].upper() == "I":
            self.bev_temp = "Iced"
        
    def set_price(self, sum):
        self.price = sum
    def set_flavoring(self, str):
        if str[0].upper() == "V":
            self.bev_flavoring = "Vanilla"
        if str[0].upper() == "C" and str[1].upper() == "H":
            self.bev_flavoring = "Chai"
        if str[0].upper() == "C" and str[1].upper() == "I":
            self.bev_flavoring = "Cinnamon"
        if str[0].upper() == "H":
            self.bev_flavoring = "Hazelnut"
        if str[0].upper() == "M":
            self.bev_flavoring = "Mocha"
        if str[0].upper() == "N" and str[1].upper() == "O":
            self.bev_flavoring = "None"
       

current_drinks = ["Latte", "Cappucino", "Americano", "Espresso", "Drip"]
current_sizes = {"Small": 3.00, "Medium": 4.00, "Large": 5.00}
current_liquids = {
    "Whole": 0.25,
    "Non-Fat": .25,
    "Oat": .50,
    "Almond": .50,
    "None": .00
}
current_flavors = {
    "Vanilla": .50,
    "Chai": .50,
    "Cinnamon": .50,
    "Hazelnut": .50,
    "Mocha": .50,
    "None": .00
}
current_temps = ["Hot", "Iced"]

total = 0.00

def welcome_splash():
    print("\n\n\t\t\t$$$$$$$$$$$ Welcome to Coffee Roulette $$$$$$$$$$$\n\n")
    print()
    print("\n\t\tDrink Options: \n")
    print(f"\t\t\t\t\t{'Small':5}\t\t{'Medium':5}\t\t{'Large':5}\n")
    for drink in current_drinks:
        # modification of price for straight espresso
        if drink == "Espresso":
            print(f"\t{drink:10}\t\t${current_sizes['Small']/2:5.2f}\t\t"
                  f"${current_sizes['Small']/2:5.2f}\t\t"
                  f"${current_sizes['Small']/2:5.2f}\t\t")
            continue
        # modification of price for drip coffee sizing
        if drink == "Drip":
            print(
                f"\t{drink:10}\t\t${current_sizes['Small']*.5:5.2f}\t\t"
                f"${current_sizes['Medium']*.5:5.2f}\t\t${current_sizes['Large']*.5:5.2f}"
            )
            continue
        # modification of price for americano sizing
        if drink == "Americano":
            print(
                f"\t{drink:10}\t\t${current_sizes['Small']*.75:5.2f}\t\t"
                f"${current_sizes['Medium']*.75:5.2f}\t\t${current_sizes['Large']*.75:5.2f}"
            )
            continue
        print(
            f"\t{drink:10}\t\t${current_sizes['Small']:5.2f}\t\t"
            f"${current_sizes['Medium']:5.2f}\t\t${current_sizes['Large']:5.2f}"
        )

    print("\n\t\tMilk Options: \n")
    for milk in current_liquids:
        print(f"\t{milk:10}\t\t${current_liquids[milk]:5.2f}\t\t"
              f"${(current_liquids[milk]*1.5):5.2f}\t\t"
              f"${(current_liquids[milk]*2):5.2f}")
    print("\n\t\tFlavor Options: \n")
    for flavor in current_flavors:
        print(f"\t{flavor:10}\t\t${current_flavors[flavor]:5.2f}\t\t"
              f"${current_flavors[flavor]*1.5:5.2f}\t\t"
              f"${current_flavors[flavor]*2:5.2f}")
    print()


employee_roster = {
    "Bob": 0,
    "Jeremy": 0,
    "Alice": 0,
    "Kelly": 0,
    "Preston": 0,
    "Cody": 0,
    "Kara": 0
}
employees_present = []
employee_drinks = {
    "Bob": BevRecipe(),
    "Jeremy": BevRecipe(),
    "Alice": BevRecipe(),
    "Kelly": BevRecipe(),
    "Preston": BevRecipe(),
    "Cody": BevRecipe(),
    "Kara": BevRecipe()
}


def attendance_check():
    
    # check who is here!
    for employee in employee_roster:
        user_input = input(f"Is {employee} here? (Y/N): ")
        
        # if they are here and they have a usual, offer for use
        if user_input.upper() == "Y" and employee_drinks[employee].get_size() != "NoSize":
            employees_present.append(employee)
            user_choice = input(f"Does {employee} want their usual? (Y/N): ")
            if user_choice.upper() == "Y":
                print(str(employee) + " gets ", end = '')
                print(f"{employee_drinks[employee].get_recipe()}")
                price_calc(employee)
                
            # user can choose to modify their usual temporarily
            if user_choice.upper() == "N":
                recipe_finder(str(employee))
                print(str(employee) + " is getting ", end = '')
                print(f"{employee_drinks[employee].get_recipe()}")
                price_calc(employee)
                
        # if they are here and dont have a usual, get their order
        if user_input.upper() == "Y" and employee_drinks[employee].get_size() == "NoSize":
            employees_present.append(employee)
            recipe_finder(str(employee))
            print(str(employee) + " is getting ", end = '')
            print(f"{employee_drinks[employee].get_recipe()}")
            price_calc(employee)

def recipe_finder(employee):
    user_size = input("What size drink? (S/M/L): ")
    acceptable_sizes = ['S','M','L']
    # catch invalid values for sizing
    while user_size[0].upper() not in acceptable_sizes:
            print("Please enter a valid size!")
            user_size = input("What size drink? (S/M/L): ")
    user_temp = input("What temperature? (Hot/Iced): ")
    acceptable_temp = ['H','I']
    # catch invalid values for temp
    while user_temp[0].upper() not in acceptable_temp:
        print("Please enter a valid temp!")
        user_temp = input("What temperature? (Hot/Iced): ")
    user_type = input("What type? (Select from drink options): ")
    acceptable_type = ['L','C','A','E','D']
    # catch invalid values for type
    while user_type[0].upper() not in acceptable_type:
        print("Please enter a valid temp!")
        user_type = input("What type? (Select from drink options): ")
    employee_drinks[employee].set_size(user_size)
    employee_drinks[employee].set_temp(user_temp)
    employee_drinks[employee].set_type(user_type)
    acceptable_flavor = ['V','C','H','M','N']
    acceptable_milk = ['W','N','O','A','N']
    
    if employee_drinks[employee].get_type() == "Americano" or employee_drinks[employee].get_type() == "Espresso":
        user_flavor = input(
            "What kind of flavoring? (Select from flavor options): ")
        
        # catch invalid values for flavor
        while user_flavor[0].upper() not in acceptable_flavor:
            print("Please enter a valid flavor!")
            user_flavor = input("What kind of flavoring? (Select from flavor options): ")
        employee_drinks[employee].set_flavoring(user_flavor)
        return employee_drinks[employee]
    else:
        user_milk = input(
            "What kind of milk? (Select from milk options): ")
        
        # catch invalid values for milk
        while user_milk[0].upper() not in acceptable_milk:
            print("Please enter a valid milk choice!")
            user_milk = input(
                "What kind of milk? (Select from milk options): ")
        user_flavor = input(
            "What kind of flavoring? (Select from flavor options): ")
        
        # catch invalid values for flavor
        while user_flavor[0].upper() not in acceptable_flavor:
            print("Please enter a valid flavor!")
            user_flavor = input("What kind of flavoring? (Select from flavor options): ")
        employee_drinks[employee].set_liquid(user_milk)
        employee_drinks[employee].set_flavoring(user_flavor)
        return employee_drinks[employee]

def price_calc(employee):
    global total
    sum = 0.00
    type = employee_drinks[employee].get_type()
    size = employee_drinks[employee].get_size()
    milk = employee_drinks[employee].get_liquid()
    flavor = employee_drinks[employee].get_flavoring()
    
    # handling americano discounts
    if type == "Americano" and size == "Small":
        sum += current_sizes[size]*.75 + current_liquids[milk] + current_flavors[flavor]
    if type == "Americano" and size == "Medium":
        sum += current_sizes[size]*.75 + current_liquids[milk] + current_flavors[flavor]*1.5
    if type == "Americano" and size == "Large":
        sum += current_sizes[size]*.75 + current_liquids[milk] + current_flavors[flavor]*2
        
    # handling drip coffee discount
    if type == "Drip":
        sum += current_sizes[size]*.5 + current_liquids[milk] + current_flavors[flavor]
        
    # handle espresso discount
    if type == "Espresso":
        sum += current_sizes[size]/2 + current_liquids[milk] + current_flavors[flavor]
        
    else:   
    # handling normal pricing
        if size == "Small":
            sum += current_sizes[size] + current_liquids[milk] + current_flavors[flavor]
        if size == "Medium":
            sum += current_sizes[size] + current_liquids[milk] + current_flavors[flavor]*1.5
        if size == "Large":
            sum += current_sizes[size] + current_liquids[milk] + current_flavors[flavor]*2
    
    total += sum
    print(f"Cost is ${sum:.2f}")
    employee_drinks[employee].set_price(sum)
    
    
    
def main():
    global total
    welcome_splash()
    # set Bobs usual
    employee_drinks["Bob"].set_size("Medium")
    employee_drinks["Bob"].set_temp("Hot")
    employee_drinks["Bob"].set_type("Cappucino")
    employee_drinks["Bob"].set_liquid("Whole")
    employee_drinks["Bob"].set_flavoring("no")

    # set Jeremys usual
    employee_drinks["Jeremy"].set_size("Medium")
    employee_drinks["Jeremy"].set_temp("Hot")
    employee_drinks["Jeremy"].set_type("Drip")
    employee_drinks["Jeremy"].set_liquid("No")
    employee_drinks["Jeremy"].set_flavoring("no")
    

    # set Alices usual
    employee_drinks["Alice"].set_size("Large")
    employee_drinks["Alice"].set_temp("Hot")
    employee_drinks["Alice"].set_type("Latte")
    employee_drinks["Alice"].set_liquid("Whole")
    employee_drinks["Alice"].set_flavoring("Chai")

    # set Kellys usual
    employee_drinks["Kelly"].set_size("Small")
    employee_drinks["Kelly"].set_temp("Hot")
    employee_drinks["Kelly"].set_type("Latte")
    employee_drinks["Kelly"].set_liquid("Oat")
    employee_drinks["Kelly"].set_flavoring("Vanilla")

    # set Prestons usual
    employee_drinks["Preston"].set_size("Medium")
    employee_drinks["Preston"].set_temp("Hot")
    employee_drinks["Preston"].set_type("Americano")
    employee_drinks["Preston"].set_liquid("No")
    employee_drinks["Preston"].set_flavoring("Vanilla")

    # set Codys usual
    employee_drinks["Cody"].set_size("Medium")
    employee_drinks["Cody"].set_temp("Iced")
    employee_drinks["Cody"].set_type("Latte")
    employee_drinks["Cody"].set_liquid("Oat")
    employee_drinks["Cody"].set_flavoring("No")

    # set Karas usual
    employee_drinks["Kara"].set_size("Small")
    employee_drinks["Kara"].set_temp("Hot")
    employee_drinks["Kara"].set_type("Latte")
    employee_drinks["Kara"].set_liquid("Oat")
    employee_drinks["Kara"].set_flavoring("Mocha")

    attendance_check()
    price_list = {}
    shuffle_list = []
    for employee in employee_drinks:
        price_list[employee] = employee_drinks[employee].price
    sorted_list = dict(sorted(price_list.items(), key=lambda item:item[1], reverse=True))
    top_spender = next(iter(sorted_list.keys()))
    print(f"Most expensive coffee is: {top_spender}")
    print(f"Total is: ${total:.2f}")
    for i in enumerate(employees_present):
        shuffle_list.append(i)
    print("\nList of employees and numbers assigned to them:\n")
    print(shuffle_list)
    print()
    # i present.....Triple Shuffle! (in the spirit of triple DES)
    print("\nShuffling once...\n")
    random.shuffle(shuffle_list)
    print(shuffle_list[0],shuffle_list[1], shuffle_list[2])
    print("\nShuffling twice...\n")
    random.shuffle(shuffle_list)
    print(shuffle_list[0],shuffle_list[1], shuffle_list[2])
    print("\nShuffling thrice...\n")
    random.shuffle(shuffle_list)
    print(shuffle_list[0],shuffle_list[1], shuffle_list[2])
    chosen_one = shuffle_list[0]
    # uncomment next 4 lines to set almost all employees to having already paid once to see the avoidance of paying twice in one week
    #employee_roster["Preston"] = 1
    #employee_roster["Kelly"] = 1
    #employee_roster["Bob"] = 1
    #employee_roster["Jeremy"] = 1

    # if the employee exists
    if chosen_one[1] in employee_roster:
        # while there is a collision, shuffle again
        while employee_roster[chosen_one[1]] == 1:
            print(f"Collision! {chosen_one[1]} has already paid once this week. Reshuffling...\n")
            random.shuffle(shuffle_list)
            print(shuffle_list[0],shuffle_list[1], shuffle_list[2])
            chosen_one = shuffle_list[0]
        # if there is no collision, check the employee off as having paid once, print their name
        employee_roster[chosen_one[1]] = 1
        print(f"Chosen payee is: {chosen_one[1]}")
    
    
    
        
    
    


main()

# the usuals!
# Bob - Med Hot Cappucino
# Jeremy - Med black coffee 
# Alice - Large hot chai latte
# Kelly - small hot vanilla oat milk latte
# Preston - Medium hot vanilla Americano
# Cody -  medium iced oat milk latte
# Kara - small hot mocha oat milk latte
