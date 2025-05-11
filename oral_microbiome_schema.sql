
DROP DATABASE IF EXISTS bmi_project;
CREATE DATABASE bmi_project;
USE bmi_project;

-- links subjects to their depression status
CREATE TABLE subject_metadata (
    subject_id INT PRIMARY KEY,
    depression_status VARCHAR(20)
);

-- Genus-level abundance table
CREATE TABLE genus_abundance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subject_id INT,
    genus_name VARCHAR(255),
    abundance FLOAT,
    FOREIGN KEY (subject_id) REFERENCES subject_metadata(subject_id)
);
