## Title: A Reproducible Pipeline for Identifying Fusobacterium nucleatum in Oral Microbiome Sequences Using k-mer Profiling and SQL Integration

# Abstract / Purpose
Our project features a reproducible bioinformatics pipeline that investigates the oral microbiome for cancer biomarkers by specifically targeting Fusobacterium nucleatum (FN) which shows strong associations with oral carcinoma. The central research question is: K-mer frequency profiles from oral microbiome sequences could enable researchers to detect Fusobacterium nucleatum and determine its abundance as it relates to oral cancer.

The solution comprises three fundamental components which work together in the pipeline.

This Python script analyzes microbiome sequences from FASTA format to produce k-mer frequency profiles.

The MySQL database contains both sample metadata and k-mer results to support structured queries and analytical tasks.

This Bash shell script manages the entire process from initial input through to database storage.

The project delivers a proof-of-concept tool for detecting oral carcinoma biomarkers through streamlined oral microbiome analysis using a modular and reproducible method.

The early data demonstrates that samples identified as oral carcinoma exhibit increased relative frequencies of k-mer patterns connected to Fusobacterium nucleatum which suggests its usefulness as a diagnostic microbial marker.

# Objectives / Goals
1. Write a Python tool that analyzes k-mer frequencies within FASTA oral microbiome sequences to identify Fusobacterium nucleatum patterns.
2. Create a MySQL database to store sample metadata together with k-mer frequencies that supports structured data queries and comparative analysis between cancer and control groups.
3. By automating the entire pipeline through a Bash shell script you can process data inputs and populate databases while maintaining reproducibility and simplicity of use.

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
