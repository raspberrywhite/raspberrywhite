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
    millis = int(round(time.time()))
    return calc_priority(timelastreq, millis)

"""
Calculate last request
"""
def calc_last_request():
    millis = int(round(time.time()))
    return millis