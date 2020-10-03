from unittest.mock import Mock

from src.alarmes.alarme import Alarme
from src.alarmes.sensor import Sensor


def test_alarm_is_off_by_default():
    alarm = Alarme()
    assert not alarm.is_alarm_on


class StubSensor:
    def exemplo_pressao(self):
        return 13


def test_baixa_pressao_ativa_alarme():
    alarm = Alarme(sensor=StubSensor())
    alarm.check()
    assert alarm.is_alarm_on


def test_pressa_normal_alarme_fica_desligado():
    stub_sensor = Mock(Sensor)
    stub_sensor.exemplo_pressao.return_value = 16
    alarm = Alarme(stub_sensor)
    alarm.check()
    assert not alarm.is_alarm_on


def test_pressao_alta_ativa_alarme():
    stub_sensor = Mock(Sensor)
    stub_sensor.exemplo_pressao.return_value = 34
    alarm = Alarme(stub_sensor)
    alarm.check()
    assert alarm.is_alarm_on
