result_1 = {
    "detector": "ATLAS",
    "date": "2026-01-01",
    "energy": 120,
    "time": "15:01:12"
}

result_2 = {
    "decorator": "LMS",
    "date_of_experiment": True
}

results = [result_1, result_2]

# print([r for r in results if r["date"] == "2026-01-01"])

class Result:
    def __init__(self, date, detector, temperature, time=None):
        self.date = date
        if detector in ["ATLAS", "LMS", "LHC"]:
            self.detector = detector
        else:
            self.detector = "Invalid detector set"
        self.temperature = temperature
        self.time = time if time is not None else "15:01:12"

    def __str__(self):
        return f"Result from {self.detector}, {self.temperature}K, {self.time} on {self.date}"

    def __repr__(self):
        return f"Result({self.detector}, {self.temperature}K, {self.time} on {self.date})"

    def is_anomaly(self):
        if self.temperature > 30 or self.temperature < 0:
            return True
        else:
            return False

    def to_celsius(self):
        return (self.temperature - 270)

    def to_fahrenheit(self):
        return ((self.temperature - 270) * 1.8) + 32



result_3 = Result(date="2026-02-01", detector="ATLAS", temperature=3, time="15:01:12")
result_4 = Result("2026-03-01", "LMS", 40, "10:01:12")
results = [result_3, result_4]

anomalies = [result for result in results if result.is_anomaly()]
print(anomalies)

temp_in_cel = [result.to_celsius() for result in results]
print(temp_in_cel)


