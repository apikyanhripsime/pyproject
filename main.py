from Restaurants import Restaurant
from Menu import Menu
from Order import Glovo
from user import User


def main():
    #=========0.Kovkas=======
    meals = {"Burger": 10, "Pizza": 12, "Pasta": 8}
    drinks = {"Cola": 2, "Juice": 3, "Water": 1}
    desserts = {"Cake": 5, "Ice Cream": 4}
    paymentList = ["Cart", "PayPal", "Cash", "Idram"]
    menu_of_kovkas = Menu(meals, drinks, desserts)
    Kovkas = Restaurant("Kovkas", 4, "Yerevan", menu_of_kovkas, paymentList)
    # ========== 1. La Piazza Italian Grill ==========
    meals1= {"Margherita Pizza": 12,"Alfredo Pasta": 14,"Lasagna": 15}
    drinks2= {"Italian Soda": 4,"Sparkling Water": 3}
    desserts3= {"Tiramisu": 7,"Cannoli": 6}
    paymentList1=['Credit Card', 'PayPal', 'Cash', 'Apple Pay']
    menu_of_LaPiazzaItalianGrill=Menu(meals1,drinks2,desserts3)
    LaPiazzaItalianGrill=Restaurant("LaPiazzaItalianGrill",4.6,['Downtown', 'Riverside', 'East Market'],menu_of_LaPiazzaItalianGrill,paymentList1)
   # ========== 2. Sakura Sushi House ==========
    meals5 = {"Salmon Nigiri": 5, "California Roll": 8, "Ramen Bowl": 11}
    drinks6 = {"Green Tea": 2, "Soft Drink": 2}
    desserts7 = {"Mochi Ice Cream": 4, "Matcha Cake": 5}
    paymentList8 = ['Credit Card', 'Cash', 'Google Pay']
    menu_of_SakuraSushiHouse = Menu(meals5, drinks6, desserts7)
    SakuraSushiHouse = Restaurant("SakuraSushiHouse",4.8,['Midtown', 'University District'],menu_of_SakuraSushiHouse,paymentList8)
    # ========== 3. Burger Station ==========
    meals9 = {"Classic Burger": 10, "Chicken Wrap": 8, "Veggie Burger": 9}
    drinks10 = {"Cola": 2, "Milkshake": 4}
    desserts11 = {"Chocolate Pie": 5, "Ice Cream Cup": 3}
    paymentList12 = ['Credit Card', 'Cash', 'Apple Pay', 'Food Vouchers']
    menu_of_BurgerStation = Menu(meals9, drinks10, desserts11)
    BurgerStation = Restaurant("BurgerStation",4.3,['Downtown', 'West Side', 'Industrial Park'],menu_of_BurgerStation,paymentList12)
    # ========== 4. Green Leaf Vegan ==========
    meals13 = {"Vegan Burrito": 9, "Tofu Salad": 8, "Veggie Burger": 11}
    drinks14 = {"Fresh Green Juice": 5, "Herbal Tea": 3}
    desserts15 = {"Vegan Chocolate Cake": 6, "Fruit Bowl": 4}
    paymentList16 = ['Credit Card', 'PayPal', 'Cash']
    menu_of_GreenLeafVegan = Menu(meals13, drinks14, desserts15)
    GreenLeafVegan = Restaurant("GreenLeafVegan",4.7,['Uptown', 'Central Park Area'],menu_of_GreenLeafVegan,paymentList16)
    # ========== 5. Bombay Spice Curry House ==========
    meals17 = {"Chicken Tikka Masala": 13,"Vegetable Biryani": 11,"Butter Chicken": 14}
    drinks18 = {"Mango Lassi": 5, "Chai Tea": 3}
    desserts19 = {"Gulab Jamun": 4, "Kheer": 5}
    paymentList20 = ['Credit Card', 'Cash', 'Google Pay', 'Apple Pay']
    menu_of_BombaySpiceCurryHouse = Menu(meals17, drinks18, desserts19)
    BombaySpiceCurryHouse = Restaurant("BombaySpiceCurryHouse",4.5,['East Market', 'Lakeside'],menu_of_BombaySpiceCurryHouse,paymentList20)
    user = User("John Doe", 25, "+1234567890", "PayPal", email="example.@emil")
    # Create Glovo delivery service with restaurants
    restaurants_list = [Kovkas,LaPiazzaItalianGrill,SakuraSushiHouse,BurgerStation,GreenLeafVegan,BombaySpiceCurryHouse]
    glovo = Glovo("Yerevan", restaurants_list, [])

    # Display initial menu
    print("Welcome to Glovo!")
    print("""1. View all restaurants
                2. Place an order
                3. View user profile
                4. Exit""")
    
    try:
        p = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Please enter a number.")
        

    match p:
        case 1:
            for i, restaurant in enumerate(restaurants_list, 1):
                print(f"{i}. {restaurant}")

        case 2:
            glovo.create_order("Yerevan", user)

        case 3:
            print(user)

        case 4:
            print("Thank you for using Glovo!")
            

        case _:
            print("Invalid choice!")
    
    
    # Create an order
    glovo.create_order("Yerevan", user)
    
    print("\nThank you for using Glovo!")


if __name__ == "__main__":
    main()