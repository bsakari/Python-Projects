import datetime


class User:  # The class is defined
    pass


user1 = User()  # An instance of a class or an object
user1.fname = "King"
user1.sname = "Kingde"  # (These are field data attached to an object)
print(user1.fname, user1.sname)
user2 = User()
user2.fname = "Wanyama"
user2.sname = "Senior"
print(user2.fname, user2.sname)


# Why use Classes instead of simple dictionaries
# because can have Methods,Initialization and help text
# A function within a class is called a method
class User:
    # This is a docstring
    """You can see this when you type the help(User)"""

    def __init__(self, full_name, birthday):
        self.name = full_name  # name is a field while full_name is the value
        self.birthday = birthday
        # Extract first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """Return the age of the user in Years"""
        today = datetime.date(2001, 12, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)  # date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)


user = User("King Wanyama", "10101998")
print(user.age())

user = User("King Wanyama", "10101998")
print(user.name, user.birthday)
print(user.first_name, user.last_name)
# help(User)
