"""
1. Use the datetime module to write a program that gets the current date and prints the day of the week.

2. Write a program that takes a birthday as input and prints the user's age and the number of days, hours, minutes and seconds until their next birthday.

3. For two people born on different days, there is a day when one is twice as old as the other. That's their Double Day. Write a program that takes two birthdays and computes their Double Day.

4. For a little more challenge, write the more general version that computes the day when one person is n times older than the other.
"""

import datetime

class Today(object):
    """Today's date.

    attributes: day, month, year, day_of_week
    """

def print_day_of_week(date):
    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print day_names[date.day_of_week]

