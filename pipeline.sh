#!/bin/bash

# Prompt user for input FASTA file and k-mer length
read -p "Enter FASTA filename: " fasta_file
read -p "Enter k-mer length (integer): " k

# Run Python script
echo "Running k-mer analysis..."
python3 daunkim_microbiome_kmer.py "$fasta_file" "$k"

# Confirm Python ran successfully
if [ $? -ne 0 ]; then
    echo "Python script failed. Exiting."
    exit 1
fi

# Ask for MySQL login
read -p "Enter your MySQL username: " mysql_user
read -s -p "Enter your MySQL password: " mysql_pass
echo ""

# Import CSV results into MySQL (requires table to already exist)
echo "Loading k-mer data into MySQL..."
mysql -u "$mysql_user" -p"$mysql_pass" -e "
USE microbiome_project;
LOAD DATA LOCAL INFILE 'kmer_output.csv'
INTO TABLE kmer_frequencies
FIELDS TERMINATED BY ',' 
IGNORE 1 ROWS
(kmer, frequency);
"

echo "Pipeline complete."
