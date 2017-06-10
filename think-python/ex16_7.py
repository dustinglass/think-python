"""
1. Use the datetime module to write a program that gets the current date and prints the day of the week.

2. Write a program that takes a birthday as input and prints the user's age and the number of days, hours, minutes and seconds until their next birthday.

3. For two people born on different days, there is a day when one is twice as old as the other. That's their Double Day. Write a program that takes two birthdays and computes their Double Day.

4. For a little more challenge, write the more general version that computes the day when one person is n times older than the other.
"""

from datetime import datetime
import copy


class Date(object):
    """A specific datetime.

    attributes: date, day, month, year, day_of_week
    """

def print_date(date):
    print "%.4d-%.2d-%.2d" % (date.year, date.month, date.day)

def print_day_of_week(d):
    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print day_names[d.day_of_week]


def instantiate_date(today=datetime.today()):
    result = Date()
    result.datetime = today
    result.day = result.datetime.day
    result.month = result.datetime.month
    result.year = result.datetime.year
    result.hour = result.datetime.hour
    result.minute = result.datetime.minute
    result.second = result.datetime.second
    result.day_of_week = result.datetime.weekday()
    return result


def custom_date(yyyy, mm, dd, h=0, m=0, s=0):
    result = Date()
    result.datetime = datetime(yyyy, mm, dd, h, m, s)
    result.day = dd
    result.month = mm
    result.year = yyyy
    result.hour = h
    result.minute = m
    result.second = s
    result.day_of_week = result.datetime.weekday()
    return result


def flat_time(date):
    seconds = 0
    seconds += date.second
    seconds += date.minute * 60
    seconds += date.hour * 60 * 60
    return seconds


def get_age(d1, d2=instantiate_date()):
    """
    Return the datetime between d1 and the d2 (current date by default).
    """
    age_delta = d2.datetime - d1.datetime
    if d2.month < d1.month: #compared month comes before anniversary month
        next_anniversary = custom_date(d2.year, d1.month, d1.day, d1.hour, d1.minute, d1.second)
    elif d2.month > d1.month: #compared month comes after anniversary month
        next_anniversary = custom_date(d2.year + 1, d1.month, d1.day, d1.hour, d1.minute, d1.second)
    elif d2.day < d1.day: #compared month = anniversary month but compared day comes before anniversary day
        next_anniversary = custom_date(d2.year, d1.month, d1.day, d1.hour, d1.minute, d1.second)
    elif d2.day > d1.day: #compared month = anniversary month but compared day comes after anniversary day
        next_anniversary = custom_date(d2.year + 1, d1.month, d1.day, d1.hour, d1.minute, d1.second)
    next_anniversary_delta = next_anniversary.datetime - d2.datetime
    return age_delta, next_anniversary_delta

def get_double_day(d1, d2):
    """
    Return the datetime at which d1 is twice as old as d2.
    """
    start_delta = d2.datetime - d1.datetime
    return d2.datetime + start_delta

def get_n_day(d1, d2, n):
    """
    Return the datetime at which d1 is n times as old as d2.
    """
    if n < 2:
        print Exception, 'The "n" in get_n_day() must be greater than 1.'
        return
    start_delta = d2.datetime - d1.datetime
    result = d2.datetime
    for i in range(n - 1):
        result += start_delta
    return result


if __name__ == '__main__':
    
    t_day = instantiate_date()

    b_day = custom_date(1992, 2, 26)
    
    age, next_bday = get_age(b_day, t_day)
    print "You are %s years old." % str(int(age.days / 365.25))
    print next_bday

    print get_double_day(b_day, t_day)

    print get_n_day(b_day, t_day, 3)






















