import unittest
from unittest import mock
from unittest.mock import Mock, patch

class Sensor:

    def read_current_temprature(self):
        pass


class WareHouseAlarm:
    def __init__(self):
        self.__low_temperature = 10
        self.__high_temperature = 18
        self.__sensor = Sensor()
        self.__is_alarm_on = False

    def check_current_temperature(self):
        temperature = self.__sensor.read_current_temprature()
        if self.__low_temperature > temperature or self.__high_temperature < temperature:
            self.__is_alarm_on = True

    @property
    def is_alarm_on(self):
        return self.__is_alarm_on


class TestWareHouseAlarm(unittest.TestCase):

    def test_is_alarm_off_by_default(self):
        alarm = WareHouseAlarm()
        self.assertFalse(alarm.is_alarm_on)

    def test_is_alarm_activated_for_high_temprature(self):
        with patch('test_monkey_patching.Sensor') as test_class:
            test_class_instance = Mock()
            test_class_instance.read_current_temprature.return_value = 20
            test_class.return_value = test_class_instance

            alarm = WareHouseAlarm()
            alarm.check_current_temperature()
            self.assertTrue(alarm.is_alarm_on)

    @patch('test_monkey_patching.Sensor')
    def test_is_alarm_activated_for_low_temperatrure(self, test_class):
        test_class_instance = Mock()
        test_class_instance.read_current_temprature.return_value = 9
        test_class.return_value = test_class_instance
        alarm = WareHouseAlarm()
        alarm.check_current_temperature()
        self.assertTrue(alarm.is_alarm_on)


if __name__ == "__main__":
    unittest.main()

