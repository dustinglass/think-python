"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""

import copy

class Time(object):
    """Represents the time of day.
       
    attributes: hour, minute, second
    """

def print_time(t):
    print '%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second)


def is_after(t1, t2):
    """Return True if Time t1 is after Time t2.

    (Don't use an if statement.)"""
    return t1.hour - t2.hour >= 0 and t1.minute - t2.minute >= 0 and t1.second >= t2.second


def increment(time, seconds):
    """Modifies Time object by adding seconds and carrying/rolling over attributes."""
    time.second += seconds
    carry_minutes = time.second / 60
    seconds = time.second % 60

    if carry_minutes > 0:
        time.minute += carry_minutes
        time.second = seconds

    carry_hours = time.minute / 60
    minutes = time.minute % 60

    if carry_hours > 0:
        time.hour += carry_hours
        time.minute = minutes

    rollover_hours = time.hour / 24
    hours = time.hour % 24

    if rollover_hours > 0:
        time.hour = hours


def pure_increment(time, seconds):
    """Returns a modified copy of a Time object according to increment."""
    time_copy = copy.deepcopy(time)
    return increment(time_copy, seconds)


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def time_to_int(time):
    """Computes the number of seconds since midnight.

    time: Time object.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def add_times(t1, t2):
    """Adds two time objects."""
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def valid_time(time):
    """Checks whether a Time object satisfies the invariants."""
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def main():
    # if a movie starts at noon...
    noon_time = Time()
    noon_time.hour = 12
    noon_time.minute = 0
    noon_time.second = 0

    print 'Starts at',
    print_time(noon_time)

    # and the run time of the movie is 109 minutes...
    movie_minutes = 109
    run_time = int_to_time(movie_minutes * 60)
    print 'Run time',
    print_time(run_time)

    # what time does the movie end?
    end_time = add_times(noon_time, run_time)
    print 'Ends at',
    print_time(end_time)

if __name__ == '__main__':
    main()