import time

"""
Calculate user priority
"""
def calc_priority(timelastreq, timeactualreq):
    return timeactualreq - timelastreq

"""
Calculate user priority now
"""
def calc_priority_now(timelastreq):
    millis = int(round(time.time() * 1000))
    return calc_priority(timelastreq, millis)