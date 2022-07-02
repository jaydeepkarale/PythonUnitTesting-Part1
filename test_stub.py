import unittest
from unittest import mock

class Sensor:

    def read_current_temprature(self):
        pass


class WareHouseAlarm:
    def __init__(self, sensor=None):
        self.__low_temperature = 10
        self.__high_temperature = 18
        self.__sensor = sensor or Sensor()
        self.__is_alarm_on = False

    def check_current_temperature(self):
        temperature = self.__sensor.read_current_temprature()
        if self.__low_temperature > temperature or self.__high_temperature < temperature:
            self.__is_alarm_on = True

    @property
    def is_alarm_on(self):
        return self.__is_alarm_on


class MockSensorHighTemp:
    def read_current_temprature(self):
        return 20

class MockSensorLowTemp:
    def read_current_temprature(self):
        return 9

class TestWareHouseAlarm(unittest.TestCase):

    def test_is_alarm_off_by_default(self):
        alarm = WareHouseAlarm()
        self.assertFalse(alarm.is_alarm_on)

    def test_is_alarm_activated_for_high_temprature(self):
        sensor = MockSensorHighTemp()
        alarm = WareHouseAlarm(sensor)
        alarm.check_current_temperature()
        self.assertTrue(alarm.is_alarm_on)

    def test_is_alarm_activated_for_low_temperatrure(self):
        pass


if __name__ == "__main__":
    unittest.main()

