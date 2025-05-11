import csv  # read the CSV file
import sys  # get command line arguments
import mysql.connector  # connect to the MySQL database

# If the user forgets to give a CSV file when running the script, show how to use it and exit
if len(sys.argv) < 2:
    print("How to use: python import_microbiome_csv.py <csv_file>")
    sys.exit(1)

csv_file = sys.argv[1]  # stores the file name given by the user

# --- Connect to MySQL database ---
# connect to the local MySQL server using the 'bmi_project' database
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="NewPassword123!",  # Replace with your actual password
        database="bmi_project"  # Replace with your actual dababase name
    )
    cursor = conn.cursor()
except Exception as e:
    print("Database connection failed:", e)
    sys.exit(1)

print("Step 1: Importing microbiome data")

imported = 0  # keep count of how many were successfully imported

# --- Open and read the CSV file ---
try:
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # Read the CSV with column headers as keys

        # Loop through each row 
        for row in reader:
            try:
                # Get subject ID and depression group label
                subject_id = int(row["SEQN"])  # Convert ID to an integer
                label = row["Group"]  # 'Depression' or 'No Depression'

                # Insert basic subject info into 'subject_metadata' table
                cursor.execute(
                    "INSERT IGNORE INTO subject_metadata (subject_id, depression_status) VALUES (%s, %s)",
                    (subject_id, label)
                )

                # Go through each genus column and insert its abundance value
                for genus_name, value in row.items():
                    if genus_name not in ["SEQN", "Group"]:  # Skip ID and label columns
                        value = value.strip()  # Clean up whitespace
                        if value:  # Only proceed if there's a number
                            try:
                                abundance = float(value)  # Convert string to float
                                cursor.execute(
                                    "INSERT INTO genus_abundance (subject_id, genus_name, abundance) VALUES (%s, %s, %s)",
                                    (subject_id, genus_name, abundance)
                                )
                            except:
                                continue  # Skip if the value can't be converted to a number

                imported += 1  # Count how many rows are imported
                if imported >= 10:  # For demo purposes, stop after 10 subjects
                    break

            except Exception as error:
                print("Error with subject ID", row.get("SEQN", "Unknown"), ":", error)

except Exception as err:
    print("Error reading file:", err)

# --- Save all the inserted data and clean up ---
conn.commit()  # Save changes to the database
cursor.close()  # Close the cursor object
conn.close()  # Close the database connection

print("Imported %d rows successfully." % imported)
