import datetime

def chop_microseconds(delta):
    return delta - datetime.timedelta(microseconds=delta.microseconds)
