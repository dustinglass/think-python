class Time(object):
    """represents the time of day"""
    
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other): #operator overloading for "+"
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

def print_attributes(obj):
    for attr in obj.__dict__:
        print attr, getattr(obj, attr)

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

start = Time()
start.hour = 9
start.minute = 45
start.second = 00

print start

print start.time_to_int()

end = start.increment(1337)

print end

print end.time_to_int()

print end.is_after(start)

print start + end

print start.__dict__

print_attributes(start)