class User:
    pass  # A way to not declare anything


user_1 = User()  # empty constructor
user_1.id = "001"  # creating attributes
user_1.username = "maithreyi"


# class with a parameterized contructor
class CarUser:
    # a parameterised  constructor which requires the user to pass 2 paramenters while initializing the object
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.seats = 5

    # a new func defenition for the car to enter race mode. Happens by reducing the seats to 2
    def enter_race_mode(self):
        self.seats = 2

    def print_user(self):
        print(f"id: {self.id}\nname: {self.username}\nfollowers: {self.followers}\nseats: {self.seats}\n")


car_user = CarUser("001", "Advik")
car_user.print_user()

car_user.enter_race_mode()
car_user.print_user()
