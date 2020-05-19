import datetime

def time_diff(start, end):
    if isinstance(start, datetime.time):
        assert isinstance(end, datetime.time)
        start, end = [datetime.datetime.combine(datetime.datetime.min, t) for t in [start, end]]
    if start <= end:
        return end - start
    else:
        end += datetime.timedelta(1)
        assert end > start
        return end - start

def days_between(d1, d2):
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)