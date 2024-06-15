from datetime import datetime
from logger.logger.time_calculator.TimeCalculation import TimeCalculation
from collections import namedtuple


ModelObject = namedtuple('ModelObject', 'start_up take_off land shut_down')


class Calculator(TimeCalculation):
    """ This class overrides init method of inherited class in order to use simpler object containing
    datetime attributes """
    def __init__(self, myobject: ModelObject):
        self.object = myobject


class TestUtilsCalculation:

    def test_fulltime_below_1hour(self):
        model_object = Calculator(
            ModelObject(
                start_up=datetime(2023, 7, 25, 17, 10, 0),
                take_off=datetime(2023, 7, 25, 17, 20, 0),
                land=datetime(2023, 7, 25, 17, 50, 0),
                shut_down=datetime(2023, 7, 25, 17, 55, 0)
            )
        )
        air, ground, full = model_object.get_times()
        assert full == '00:45'
        assert ground == '00:15'
        assert air == '00:30'

    def test_fulltime_equal_1hour(self):
        model_object = Calculator(
            ModelObject(
                start_up=datetime(2023, 7, 25, 17, 10, 0),
                take_off=datetime(2023, 7, 25, 17, 20, 0),
                land=datetime(2023, 7, 25, 17, 50, 0),
                shut_down=datetime(2023, 7, 25, 18, 10, 0)
            )
        )
        air, ground, full = model_object.get_times()
        assert full == '01:00'
        assert ground == '00:30'
        assert air == '00:30'

    def test_fulltime_over_1hour(self):
        model_object = Calculator(
            ModelObject(
                start_up=datetime(2023, 7, 25, 17, 10, 0),
                take_off=datetime(2023, 7, 25, 17, 20, 0),
                land=datetime(2023, 7, 25, 18, 45, 0),
                shut_down=datetime(2023, 7, 25, 18, 55, 0)
            )
        )
        air, ground, full = model_object.get_times()
        assert full == '01:45'
        assert ground == '00:20'
        assert air == '01:25'

    def test_time_over_midnight(self):
        model_object = Calculator(
            ModelObject(
                start_up=datetime(2023, 7, 25, 23, 40, 0),
                take_off=datetime(2023, 7, 25, 23, 45, 0),
                land=datetime(2023, 7, 26, 00, 10, 0),
                shut_down=datetime(2023, 7, 26, 00, 15, 0)
            )
        )
        air, ground, full = model_object.get_times()
        assert full == '00:35'
        assert ground == '00:10'
        assert air == '00:25'


