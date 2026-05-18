import pytest
from weather import celsius_to_fahrenheit, average_temperature, detect_anomalies

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40  # Special case where both scales match

def test_average_temperature():
    assert average_temperature([10, 20, 30]) == 20
    assert average_temperature([-5, 5, 15]) == 5

def test_average_temperature_empty_list():
    with pytest.raises(ValueError, match="Temperature list cannot be empty"):
        average_temperature([])

@pytest.mark.parametrize("celsius, expected", [
    (0, 32),
    (100, 212),
    (-40, -40),
    (37, 98.6)
])
def test_celsius_to_fahrenheit_param(celsius, expected):
    assert celsius_to_fahrenheit(celsius) == expected


def test_detect_anomalies():
    temperatures = [10, -15, 35, -40, 5]
    assert detect_anomalies(temperatures, 20) == [35, -40]
    assert detect_anomalies(temperatures, 50) == []
    assert detect_anomalies(temperatures, 5) == [10, -15, 35, -40]

@pytest.mark.skip(reason="Function not implemented yet")
def test_future_feature():
    assert False  # Placeholder for future test

