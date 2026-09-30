from user import User
from Menu import Menu

class order: 
    def __init__(self,items, total, date, restaurant, user):
        self.item=items
        self.total=total 
        self.date=date 
        self.restaurant=restaurant
        self.user=user 
    