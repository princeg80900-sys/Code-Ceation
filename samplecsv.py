import csv
# Open the CSV file for reading
# count no of line in it+
try:
    with open('excel.csv', mode ='r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)
        count = 0
        for row in reader:
            count += 1

    print(f"The number of lines in the CSV file is: {count}")
        
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)