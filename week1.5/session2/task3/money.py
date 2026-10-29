# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        # Add validation code here, to check that
        # - the pounds parameter is an integer
        # - pounds is not negative
        # - the pence parameter is an integer
        # - pence is not negative and not greater than 99
        # Raise appropriate exceptions if any of these are violated

        if not isinstance(pounds, int):
            raise TypeError("Pounds must be an integer")
        if pounds < 0:
            raise ValueError("Pounds must not be negative")
        if not isinstance(pence, int):
            raise TypeError("Pence must be an integer")
        if pence < 0 or pence > 99:
            raise ValueError("Pence must not be negative, and pence must be less than 99")


        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        # Add code here to return an appropriate string representation
        # Use the currency symbol for British Pounds Sterling
        # Represent pence with a leading zero if needed (e.g. '05')

        
        return f"£{self.pounds}.{self.pence:02d}"

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """
        # Add code here to check that parameter 'other' is a Money object,
        # add self to other, then return the sum as a new Money object
        # (see README for hints and tips)
        if not isinstance(other,Money):
            raise TypeError("Must add two money objects")

        poundSum = self.pounds + other.pounds
        penceSum = self.pence + other.pence

        if penceSum // 100 > 0:
            poundSum += 1
            penceSum = 100-(penceSum % 100)
        
        return Money(poundSum,penceSum)

        
