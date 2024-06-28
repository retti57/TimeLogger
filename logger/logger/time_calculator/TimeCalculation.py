from collections import namedtuple
from datetime import datetime
from django.db import models


class TimeCalculation:
    def __init__(self, model_object: [models.Model, models.Field]):
        self.object = model_object

    def _time_calculation(self, time1: datetime, time2: datetime) -> float():
        """ Time calculation of given values of type 'datetime'.
        First value should be earlier value in time concept
        :return: time value in format  HH:MM """
        _FORMAT = '%H:%M:%S'

        if time1 > time2:
            duration = time1 - time2
        else:
            duration = time2 - time1

        return duration.total_seconds()

    def _conv_sec_to_H_M(self, totalseconds: float):
        from math import floor
        h = floor(totalseconds / 3600)
        m = floor((totalseconds % 3600) / 60)
        if len(str(h)) == 1:
            h = f'0{h}'
        if len(str(m)) == 1:
            m = f'0{m}'

        return f'{h}:{m}'

    def get_times_in_seconds(self) -> tuple:
        air = self._time_calculation(self.object.take_off, self.object.land)
        gnd1 = self._time_calculation(self.object.start_up, self.object.take_off)
        gnd2 = self._time_calculation(self.object.land, self.object.shut_down)
        gnd = gnd2 + gnd1
        full = self._time_calculation(self.object.start_up, self.object.shut_down)

        return air, gnd, full

    def get_times(self) -> namedtuple:
        """ Returns namedtuple with fields 'air','gnd', 'full'.
        Times in specific fields are converted in format HH:MM"""
        air_s, gnd_s, full_s = self.get_times_in_seconds()
        air = self._conv_sec_to_H_M(air_s)
        gnd_total = self._conv_sec_to_H_M(gnd_s)
        full = self._conv_sec_to_H_M(full_s)

        FlightTimes = namedtuple("FlightTimes", "air gnd full")

        return FlightTimes(air, gnd_total, full)
