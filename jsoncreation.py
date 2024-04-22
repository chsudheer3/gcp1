import csv
import json
import pandas as pd
def make_json(csvFilePath, jsonFilePath):
    data = []
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            data.append(dict(rows))

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Typecast specific columns to integers
    columns_to_typecast = ['age', 'marks']
    df[columns_to_typecast] = df[columns_to_typecast].astype(int)

    # Write the modified DataFrame to a JSON file
    df.to_json(jsonFilePath, orient='records', indent=4)
csvFilePath = r'/content/StudentData.csv'  # Replace with your CSV file path
jsonFilePath = r'student3.json'  # Specify the desired JSON file path
make_json(csvFilePath, jsonFilePath)
