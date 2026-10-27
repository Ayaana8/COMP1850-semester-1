# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    def __init__(self, name, birth):
        """
        Creates a person, given values for name and birthday
        """
        self.name = name
        self.birth = birth

        if not isinstance(name, str):
            raise TypeError
        if not isinstance(birth,date):
            raise TypeError
        if len(name) == 0:
            raise ValueError

    def initials(self):
        """
        Returns the person's initials
        """
        nameList = []
        nameList = self.name.split(" ")
        initials = ""
        for name in nameList:
            initials += name[0]
        return initials

    def is_birthday(self):
        """
        Returns true if it is the person's birthday today
        """
        if self.date == date.today():
            return True
        return False   
        
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
