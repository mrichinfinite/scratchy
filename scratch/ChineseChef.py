from Chef import Chef

class ChineseChef(Chef): # Here we are inheriting all the functionality from the Chef class and passing it into the ChineseChef class. 
    def make_fried_rice(self): # Here we are creating a new function just for the ChineseChef class.
        print("The chef makes fried rice")

    def make_special_dish(self): # Here we are changing the old make_special_dish function from the Chef class and redefining it for the ChineseChef class.
        print("The chef makes orange chicken")