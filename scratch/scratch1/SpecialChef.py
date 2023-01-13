from Chef import Chef
# Here we are inheriting all the functionality from the Chef class and passing it into the SpecialChef class. 
class SpecialChef(Chef): 
    # Here we are creating a new function just for the SpecialChef class:
    def make_special_rice(self): 
        print("The chef makes special rice!")
    # Here we are changing the old make_special_dish function from the Chef class and redefining it for the SpecialChef class:
    def make_special_dish(self): 
        print("The chef makes a very special dish!")