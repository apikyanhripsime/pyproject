from Restaurants import Restaurant
from user import User
class Glovo:
    def __init__(self, zone, restaurants, delivers):
        self.zone = zone
        self.restaurants = restaurants
        self.delivers = delivers
        self.orders=[]
    def create_order(self, zone, user):
        while True:
            print("\nAvailable Restaurants:")
            for i in range(len(self.restaurants)):
                print(f"{i}: {self.restaurants[i]}")
            try:
                restaurant_index = int(input("Enter the number of restaurant: "))
                if restaurant_index < 0 or restaurant_index >= len(self.restaurants):
                    print("Invalid restaurant number.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue
            
            selected_restaurant = self.restaurants[restaurant_index]
            print(f"\nOrdering from {selected_restaurant.name}")
            price = selected_restaurant.order(zone)
            
            if price > 0:
                selected_restaurant.payment(user.paymentMethod, price)
            
            ex = input("\nFinish ordering? (Yes/No): ")
            if ex.lower() == "yes":
                break
    