from Menu import Menu

class Restaurant:
    def __init__(self, name, rating, delivery_zone, menu, paymentList):
        self.name = name
        self.rating = rating
        self.delivery_zone = delivery_zone
        self.menu = menu
        self.paymentList = paymentList

    def __str__(self):
        return f"Name: {self.name} \nRating: {self.rating}"
    def order(self,zone):
        card = {}
        total_price = 0
        
        while True:
            print(self.menu)
            print("0) Finish order")
            try:
                n = int(input("Enter The number of menu category (1-Meals, 2-Drinks, 3-Desserts, 0-Finish): ").strip())
                
                if n == 0:
                    break
                elif n == 1:
                    while True:   
                        print(f"Meals: {self.menu.meals}")
                        dish = input("Enter the dish name (or 'back' to go back): ").strip()
                        if dish.lower() == 'back':
                            break
                        if dish in self.menu.meals.keys():
                            if dish in card.keys():
                                card[dish] += 1
                            else:
                                card[dish] = 1
                            print(f"Added {dish} to cart. Quantity: {card[dish]}")
                        else:
                            print("Dish not found in menu.")
                elif n == 2:
                    while True:
                        print(f"Drinks: {self.menu.drinks}")
                        drink = input("Enter the drink name (or 'back' to go back): ").strip()
                        if drink.lower() == 'back':
                            break
                        if drink in self.menu.drinks.keys():
                            if drink in card.keys():
                                card[drink] += 1
                            else:
                                card[drink] = 1
                            print(f"Added {drink} to cart. Quantity: {card[drink]}")
                        else:
                            print("Drink not found in menu.")
                elif n == 3:
                    while True:
                        print(f"Desserts: {self.menu.desserts}")
                        dessert = input("Enter the dessert name (or 'back' to go back): ").strip()
                        if dessert.lower() == 'back':
                            break
                        if dessert in self.menu.desserts.keys():
                            if dessert in card.keys():
                                card[dessert] += 1
                            else:
                                card[dessert] = 1
                            print(f"Added {dessert} to cart. Quantity: {card[dessert]}")
                        else:
                            print("Dessert not found in menu.")
                else:
                    print("Invalid menu number.")
            except ValueError:
                print("Please enter a valid number.")
            
        # Calculate total price
        all_items = self.menu.get_all_items()
        for item, quantity in card.items():
            if item in all_items['meals']:
                total_price += all_items['meals'][item] * quantity
            elif item in all_items['drinks']:
                total_price += all_items['drinks'][item] * quantity
            elif item in all_items['desserts']:
                total_price += all_items['desserts'][item] * quantity
        
        print(f"\nOrder Summary:")
        for item, quantity in card.items():
            if item in all_items['meals']:
                price = all_items['meals'][item]
            elif item in all_items['drinks']:
                price = all_items['drinks'][item]
            elif item in all_items['desserts']:
                price = all_items['desserts'][item]
            print(f"  {item} x{quantity} = ${price * quantity}")
        print(f"Total: ${total_price}")
        
        return total_price


    def payment(self, method, price):
        if not (method in self.paymentList):
            print(f"Payment method not available. Available methods: {self.paymentList}")
            return False
        print(f"Payment successful via {method}: -${price}")
        return True
    