#!/bin/bash

# -------------------------------------------
# This script automates the process of importing oral microbiome data
# into a MySQL database and generating a visualization using Python.
# -------------------------------------------

echo "Starting microbiome data pipeline"

# Step 1: Import CSV into MySQL database
# runs the Python script that loads the first 10 subjects from oral_microbiome.csv
echo "Step 1: Importing CSV data into MySQL"
python import_microbiome_csv.py oral_microbiome.csv

# Step 2: Generate a plot of Prevotella abundance
# runs the Python script that connects to MySQL and creates a boxplot
echo "Step 2: Generating visualization from MySQL data"
python visualize_prevotella.py

# Final message when everything completes
echo "Pipeline finished."
