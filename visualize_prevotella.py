import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# connect to database
engine = create_engine("mysql+mysqlconnector://root:NewPassword123!@localhost/bmi_project")
conn = engine.connect()

# Query Prevotella abundance and depression status
query = "SELECT s.depression_status, g.abundance FROM genus_abundance g JOIN subject_metadata s ON g.subject_id = s.subject_id WHERE g.genus_name = 'g__Prevotella'"
df = pd.read_sql(query, conn) 

# Done with the database
conn.close()

# Create a boxplot showing Prevotella abundance by depression status
df.boxplot(by="depression_status", column="abundance", grid=False)
plt.title("Prevotella Abundance by Depression Status")
plt.suptitle("")  # Removes automatic subtitle
plt.xlabel("Depression Status")
plt.ylabel("Abundance")
plt.tight_layout()
plt.savefig("prevotella_abundance_boxplot.png")
plt.show()
