## BMI-Programming

# Objectives
1. Develop a Python script that calculates k-mer frequency profiles from FASTA-format oral microbiome sequences
2. Build and populate a MySQL database with sample metadata and corresponding k-mer frequency results.
3. Create a Bash shell script to automate the full pipeline

# Deliverables
1. A Python script reads FASTA files, accepts user input for k-mer length, calculates frequencies. The script includes logging of sequence counts processed and coverage status.
2.  A sql file contains all DDL and DML statements to create and populate two tables for sample metadata and kmer frequencies
3. A Bash script asks for input FASTA file and k-mer size, runs the Python script, and then populates the SQL database using the generated CSV files.
