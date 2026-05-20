import csv

with open("movies.csv", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if int(row[1]) > 2000 and row[3].lower() == "sci-fi":
            print(row)

with open("movies.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        if int(row.get("Year", 0)) > 2000 and row.get("Genre", "").lower() == "sci-fi":
            print(row)

# with open("movies.csv", newline="", mode="a") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Interstellar", 2014, "Christopher Nolan", "Sci-Fi"])
#
with open("movies.csv", newline="", mode="a") as file:
    writer = csv.DictWriter(file, fieldnames=("Title", "Year", "Director", "Genre"))
    writer.writerow({
        "Title": "Finding Nemo",
        "Year": 2003,
        "Director": "Pixar",
        "Genre": "Animation"
    })