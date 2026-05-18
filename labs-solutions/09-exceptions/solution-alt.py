class InvalidMeasurementError(Exception):
    """Custom exception for invalid scientific measurements."""
    def __init__(self, experiment_id, value):
        super().__init__(f"Invalid measurement in {experiment_id}: {value}")
        self.experiment_id = experiment_id
        self.value = value


def process_measurements(measurements):
    """
    Processes a list of scientific measurements with error handling.

    :param measurements: List of (experiment_id, value) tuples.
    :return: Processed data summary or an error message.
    """
    total = 0
    count = 0
    valid_measurements = []  # To store valid values

    for experiment_id, value in measurements:
        try:
            if not isinstance(value, (int, float)):
                raise TypeError(f"Invalid value '{value}' in experiment {experiment_id}. Must be a number.")
            
            if value < 0:
                raise InvalidMeasurementError(experiment_id, value)

            total += value
            count += 1
            valid_measurements.append(value)

        except TypeError as e:
            print(f"Error: {e}")  # Handle non-numeric values
        except InvalidMeasurementError as e:
            print(f"Error: {e}")  # Handle negative values

    try:
        average = total / count  # Might raise ZeroDivisionError if no valid measurements
    except ZeroDivisionError:
        print("Error: No valid measurements to process.")
        return None
    else:
        return f"Processed {count} valid measurements. Average value: {average:.2f}"
    finally:
        print("Processing complete.")  # Always runs, even if an error occurs


# --- 🔬 Example Usage & Testing ---
data_samples = [
    ("EXP001", 23.4),  
    ("EXP002", "invalid"),  # ❌ Should trigger TypeError
    ("EXP003", -5.0),       # ❌ Should trigger InvalidMeasurementError
    ("EXP004", 18.7),  
    ("EXP005", 30.2)
]

print(process_measurements(data_samples))  # Run the function

