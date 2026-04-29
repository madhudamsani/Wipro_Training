import csv
import os


def write_csv(filename):
    # Data should be a list of dictionaries, not a single dictionary
    data = [
        {"Name": "Madhu", "Age": 23},
        {"Name": "Sri", "Age": 22}
    ]

    # Correct column names to match the dictionary keys
    columns = ["Name", "Age"]

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(data)


def read_csv(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


def delete_csv(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully")
    else:
        print(f"{filename} does not exist")


# Main execution
filename = "myfile.csv"
write_csv(filename)
print("Data read from csv file:")
read_csv(filename)
delete_csv(filename)
