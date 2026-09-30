class Menu:
    def __init__(self, meals, drinks, desserts):
        self.meals = meals
        self.drinks = drinks
        self.desserts = desserts
    
    
    def get_all_items(self):
        """Returns all menu items organized by category"""
        return {
            'meals': self.meals,
            'drinks': self.drinks,
            'desserts': self.desserts
        }
    def add_item(self,category, name, price):
        ls= vars(self)
        if category in ls.keys():
            ls[category][name]=price
            return f"<<{name}>> add in menu"
    def remove_item(self,category, name):  
        ls= vars(self) 
        if  category in ls.keys():
            del ls[category][name]   
            return f"<<{name}>> is deleted from menu"
    def get_item_price(self,category, name):
        ls=vars(self) 
        if  category in ls.keys():
            return f"{ls[category][name]}$"
            


    def __str__(self):
        return f"1)Meals: {len(self.meals)} \n2)Drinks: {len(self.drinks)} \n3)Desserts: {len(self.desserts)}"

meals = {"Burger": 10, "Pizza": 12, "Pasta": 8}
drinks = {"Cola": 2, "Juice": 3, "Water": 1}
desserts = {"Cake": 5, "Ice Cream": 4}
paymentList = ["Cart", "PayPal", "Cash", "Idram"]
x=Menu(meals,drinks,desserts) 
print(x.add_item("drinks","vodka",10)) 
print(x.add_item("desserts","dranken cherry",15))  
print(x.add_item("meals","salad",5)) 
print(x.get_all_items()) 
print("\n") 
print(x.remove_item("desserts","dranken cherry"))
print(x.get_all_items())  
print(x.get_item_price("drinks","vodka"))
      

