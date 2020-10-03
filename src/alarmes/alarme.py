""" Class de alarme """
from .sensor import Sensor


class Alarme:

    def __init__(self, sensor=None):
        self._low_pressure_threshold = 15
        self._high_pressure_threshold = 31
        self._sensor = sensor or Sensor()  # aqui onde vai o stub
        self._is_alarm_on = False

    def check(self):
        pressure = self._sensor.exemplo_pressao()
        if pressure < self._low_pressure_threshold \
                or self._high_pressure_threshold < pressure:
            self._is_alarm_on = True

    @property
    def is_alarm_on(self):
        return self._is_alarm_on
