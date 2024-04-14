from datetime import datetime


def time_calculation(time1: datetime, time2: datetime) -> float():
    """ Time calculation of given values of type 'datetime'.
    First value should be earlier value in time concept
    :return: time value in format  HH:MM """
    _FORMAT = '%H:%M:%S'

    if time1 > time2:
        duration = time1 - time2
    else:
        duration = time2 - time1

    return duration.total_seconds()


def conv_sec_to_H_M(totalseconds: float):
    from math import floor
    h = floor(totalseconds / 3600)
    m = floor((totalseconds % 3600) / 60)
    if len(str(h)) == 1:
        h = f'0{h}'
    if len(str(m)) == 1:
        m = f'0{m}'

    return f'{h}:{m}'
