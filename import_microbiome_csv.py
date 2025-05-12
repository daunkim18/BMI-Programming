import csv
import mysql.connector
import sys

# make sure user passed a CSV file
if len(sys.argv) < 2:
    print("usage: python import_microbiome_csv.py <csv_file>")
    sys.exit(1)

csv_file = sys.argv[1]
imported = 0

# connect to MySQL 
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NewPassword123!",  # replace with user's actual password
    database="bmi_project"
)
cursor = conn.cursor()

# Open the CSV file 
with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)  # Read rows as dictionaries using header names

    for row in reader:
        # Get the subject ID and depression status
        subject_id = int(row["SEQN"])
        label = row["Group"]

        # Add subject info to the metadata table 
        cursor.execute(
            "INSERT IGNORE INTO subject_metadata (subject_id, depression_status) VALUES (%s, %s)",
            (subject_id, label)
        )

        # Insert abundance values
        for genus_name, value in row.items():
            if genus_name in ["SEQN", "Group"]:
                continue  # Skip ID and label columns

            value = value.strip()  # Remove any spaces

            if value:
                # Convert the abundance to a float and insert it
                abundance = float(value)
                cursor.execute(
                    "INSERT INTO genus_abundance (subject_id, genus_name, abundance) VALUES (%s, %s, %s)",
                    (subject_id, genus_name, abundance)
                )

        # Keep track of how many subjects are imported
        imported += 1
        if imported >= 10:
            break  # Stop after 10 subjects 
