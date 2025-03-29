

-- Create table to store sample info
CREATE TABLE sample_metadata (
    sample_id INT AUTO_INCREMENT PRIMARY KEY,
    sample_name VARCHAR(255),
    health_status VARCHAR(50),  -- e.g., "Healthy", "Periodontal"
    source_file VARCHAR(255),
    date_processed DATE
);

-- Create table to store k-mer frequencies
CREATE TABLE kmer_frequencies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sample_id INT,
    kmer VARCHAR(50),
    frequency INT,
    FOREIGN KEY (sample_id) REFERENCES sample_metadata(sample_id)
);

-- Example inserts (you can generate more with Python/Bash)
INSERT INTO sample_metadata (sample_name, health_status, source_file, date_processed)
VALUES ('H001', 'Healthy', 'healthy_sample1.fasta', '2025-04-01');

INSERT INTO kmer_frequencies (sample_id, kmer, frequency)
VALUES (1, 'ACGT', 15),
       (1, 'CGTA', 10),
       (1, 'GTAC', 5);
