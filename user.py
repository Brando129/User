"""For this assignment you will create the user class and add a couple methods!
On instantiation of a user, the following attributes should be passed in as arguments:

first_name
last_name
email
age
Also include default attributes:

is_rewards_member - default value of False
gold_card_points = 0
"""

"""display_info(self) - Have this method print all of the users' details on separate lines.
enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
spend_points(self, amount) - have this method decrease the user's points by the amount specified."""

"""Add logic in the enroll method to check if they are a member already,
and if they are, print "User already a member." and return False, otherwise
return True. Add logic in the spend points method to be sure they have
enough points to spend that amount and handle appropriately."""

class User:
    def __init__(self, first_name, last_name, email, age):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self

    def enroll(self):

        if self.is_rewards_member == True:
            print(f"{self.first_name}, is already a member.")
            return self

        self.is_rewards_member = True
        self.gold_card_points = 200

        return self


    def spend_points(self, amount):

        if self.gold_card_points < amount:
            print("You don't have enough points")
            return  False

        self.gold_card_points -= amount



brandon = User("Brandon", "Colangelo", "brandoncancode@gmail.com", 30)
jane = User("Jane", "Doe", "janedoe@email.com", 29)
john = User("John", "Stylone", "js412@gmail.com", 44)

john.enroll().spend_points(80)
john.display_info()