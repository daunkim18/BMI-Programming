# This script connects to the MySQL database
# grabs data about the genus Prevotella
# and shows a boxplot comparing its abundance in people with and without depression.

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Set up database connection
try:
    engine = create_engine("mysql+mysqlconnector://root:NewPassword123!@localhost/bmi_project")
    conn = engine.connect()
except Exception as e:
    print("Failed to connect to database:", e)
    exit()

# Load Prevotella data from database
query = "SELECT s.depression_status, g.abundance FROM genus_abundance g JOIN subject_metadata s ON g.subject_id = s.subject_id WHERE g.genus_name = 'g__Prevotella'"
try:
    # Read the SQL result into Pandas DataFrame
    df = pd.read_sql(query, conn)
except Exception as e:
    print("Failed to load data:", e)
    conn.close()
    exit()

conn.close()

# Plot boxplot to visualize the data
try:
      # shows the spread of Prevotella abundance
    df.boxplot(by="depression_status", column="abundance", grid=False)
    plt.title("Prevotella Abundance by Depression Status")
    plt.suptitle("") # Removes the automatic title from panda
    plt.xlabel("Depression Status")
    plt.ylabel("Abundance")
    plt.tight_layout() # Save the plot as a PNG file
    plt.savefig("prevotella_abundance_boxplot.png")
    plt.show()
except Exception as e:
    print("Failed to generate plot:", e)
