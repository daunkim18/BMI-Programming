#!/bin/bash

# pipeline to load oral microbiome data into MySQL and generate a plot

echo "Running microbiome data pipeline"

# Load first 10 subjects from the CSV into MySQL
echo "Importing data from CSV."
python import_microbiome_csv.py oral_microbiome.csv

# Create a boxplot of Prevotella abundance from the DB
echo "Generating Prevotella plot"
python visualize_prevotella.py

echo "Done."
