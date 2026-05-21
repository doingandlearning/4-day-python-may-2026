import pandas as pd

df = pd.read_csv("weather.csv")
del df["temp_c_roll3"]
print(df.head())
print(df.tail())
print(df.sample(5))

print(df.describe())
df["temp_c_roll5"] = df["temp_c"].rolling(window=5, min_periods=5).mean()
print(df.info())
df.to_csv("new_weather.csv", index=False)

print(df.sort_values(by="temp_c", ascending=False))