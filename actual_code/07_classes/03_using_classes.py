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

results = [
    ("2026-01-01", "ATLAS", 25, "15:01:12"),
    ("2026-01-01", "LMS", 25, "15:01:12"),
    ("2026-01-01", "LHC", 25, "15:01:12"),
    ("2026-01-01", "ATLAS", 31, "15:01:12"),
    ("2026-01-01", "LMS", 31, "15:01:12"),
    ("2026-01-01", "LHC", 31, "15:01:12"),
]

results_list = []

for date, detector, temperature, time in results:
    result = Result(date, detector, temperature, time)
    results_list.append(result)

print(results_list)