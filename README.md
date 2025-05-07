## A Reproducible Pipeline for Identifying Fusobacterium nucleatum in Oral Microbiome Sequences Using k-mer Profiling and SQL Integration

# Objectives
1. Develop a Python script that calculates k-mer frequency profiles from FASTA-format oral microbiome sequences
2. Build and populate a MySQL database with sample metadata and corresponding k-mer frequency results.
3. Create a Bash shell script to automate the full pipeline

# Deliverables
1. **Python Script**
   - Reads FASTA files.
   - Accepts user input for k-mer length.
   - Calculates k-mer frequencies.
   - Logs:
     - Number of sequences processed.
     - Coverage status.

2. **SQL File**
   - Contains all necessary DDL (Data Definition Language) statements to:
     - Create two tables: one for sample metadata and one for k-mer frequencies.
   - Contains DML (Data Manipulation Language) statements to:
     - Populate the tables using data generated from the Python script.

3. **Bash Script**
   - Prompts the user to:
     - Enter the input FASTA file path.
     - Specify the desired k-mer size.
   - Executes the Python script.
   - Populates the SQL database using the generated CSV files.
