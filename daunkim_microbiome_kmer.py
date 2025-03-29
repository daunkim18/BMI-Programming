#!/usr/bin/env python3

import sys

# Error handling for command-line arguments
if len(sys.argv) == 1:
    print("Error: No options given. The program takes a filename and an integer as input.")
    sys.exit(1)
elif len(sys.argv) == 2:
    print("Error: Not enough options given. The program takes a filename and an integer as input.")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Error: Too many options given. The program takes a filename and an integer as input.")
    sys.exit(1)

filename = sys.argv[1]
try:
    k = int(sys.argv[2])
except ValueError:
    print("Error: Second argument must be an integer.")
    sys.exit(1)

# Read sequence from FASTA file
sequence = ""
try:
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith(">"):
                continue
            sequence += line.strip().upper()
except FileNotFoundError:
    print("Error: File not found.")
    sys.exit(1)

# Generate k-mer frequency dictionary
kmer_dict = {}
for i in range(len(sequence) - k + 1):
    kmer = sequence[i:i+k]
    if len(kmer) == k:
        if kmer in kmer_dict:
            kmer_dict[kmer] += 1
        else:
            kmer_dict[kmer] = 1

# Output to CSV
output_file = "kmer_output.csv"
with open(output_file, 'w') as out:
    out.write("kmer,frequency\n")
    for kmer in sorted(kmer_dict.keys()):
        out.write(kmer + "," + str(kmer_dict[kmer]) + "\n")

print("k-mer frequency analysis complete. Output saved to:", output_file)

