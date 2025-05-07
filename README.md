# BMI8540 Project Title
# A Reproducible Pipeline for Identifying Fusobacterium nucleatum in Oral Microbiome Sequences Using k-mer Profiling and SQL Integration

---

## Abstract & Purpose
Our project features a reproducible bioinformatics pipeline that investigates the oral microbiome for cancer biomarkers by specifically targeting Fusobacterium nucleatum (FN) which shows strong associations with oral carcinoma. The central research question is: K-mer frequency profiles from oral microbiome sequences could enable researchers to detect Fusobacterium nucleatum and determine its abundance as it relates to oral cancer.

The solution comprises three fundamental components which work together in the pipeline.

1. Python script analyzes microbiome sequences from FASTA format to produce k-mer frequency profiles.

2. MySQL database contains both sample metadata and k-mer results to support structured queries and analytical tasks.

3. Bash shell script manages the entire process from initial input through to database storage.

The project delivers a proof-of-concept tool for detecting oral carcinoma biomarkers through streamlined oral microbiome analysis using a modular and reproducible method.

The early data demonstrates that samples identified as oral carcinoma exhibit increased relative frequencies of k-mer patterns connected to Fusobacterium nucleatum which suggests its usefulness as a diagnostic microbial marker.

---

## Objectives & Goals
1. Write a Python tool that analyzes k-mer frequencies within FASTA oral microbiome sequences to identify Fusobacterium nucleatum patterns.
2. Create a MySQL database to store sample metadata together with k-mer frequencies that supports structured data queries and comparative analysis between cancer and control groups.
3. By automating the entire pipeline through a Bash shell script you can process data inputs and populate databases while maintaining reproducibility and simplicity of use.

---

## Background
Oral carcinoma is the most common head and neck cancer, but it remains a huge health concern because of its high incidence and high morbidity. New studies have pointed to the oral microbiome in oral cancer development and propose that microbiota can support tumorigenesis through a host of inflammatory and immune-modulatory mechanisms (Gopinath et al., 2020; Xiao et al., 2023). One of the taxa of microbes that are involved in this condition, Fusobacterium nucleatum, is most common in the oral biofilms of patients with cancer and has been found to cause inflammation and modulate immunity. It’s been shown that this bacterium makes a cancer-friendly microenvironment, via the activation of certain host immune systems, promoting inflammation and permitting tumorigenic states (Kostic et al., 2013; Rubinstein et al., 2019). There is evidence that Fusobacterium nucleatum might accelerate not just the cancer process but also other microbes to change host behavior, signaling and immunity (Kostic et al., 2013; Chandrababu & Bastola, 2022).

It would be beneficial to have knowledge of these microbial changes, which could yield invaluable information about early detection signals or targets. Identifying certain bacterial signatures associated with oral carcinoma helps scientists map microbial biology to disease (Chattopadhyay, Verma, & Panda, 2019). These microbial differences may also be early detected to identify oral carcinoma in more curable stages, where bacterial biomarkers are non-invasive markers of disease activity. Furthermore, determining which bacteria best match cancer states may guide microbiome-based therapeutic treatments like probiotics or specific antimicrobial treatments that modify or even normalize the oral microbiome to mitigate the risk of cancer.

The prevalence and deadly nature of oral carcinoma makes it one of the most widespread head and neck cancers worldwide. New research indicates that Fusobacterium nucleatum's dominance within the oral microbiome contributes to cancer development by affecting immune response and promoting inflammation. Analysis of microbial patterns creates a hopeful path for developing non-invasive diagnostic tools.

This database project aims to develop a structured search environment that connects sample metadata information like health status to microbial signatures including k-mer frequency profiles obtained from oral microbiome DNA sequences. The system enables computational analysis to identify possible microbial biomarkers specific to oral cancer.

This project holds importance because detecting oral carcinoma early stages improves treatment success rates. Traditional diagnostic procedures typically require invasive methods or incur high costs and remain inaccessible to many patients. Microbiome sequencing through computational data-driven methods creates scalable low-cost screening tools based on public 16S rRNA sequencing data which proves valuable for clinical research applications.

This research project introduces a new methodology that analyzes Fusobacterium nucleatum in cancers through k-mer based profiling while storing results in a MySQL database and automating the analysis process with Bash scripting. The pipeline combines microbial bioinformatics principles with practical data engineering solutions in a modular open-source framework—an approach rarely discussed in the existing literature.

## Research Question
What are the differences in the k-mer frequency profiles associated with *Fusobacterium nucleatum* between individuals with oral carcinoma and healthy controls, and can these differences be used to support its role as a non-invasive microbial biomarker for early cancer detection?

---

## Installation & Usage

### Prerequisites

- Python 3.x
- MySQL server
- Bash shell
- Required Python packages: `pandas`, `argparse`

### Step-by-Step

1. **Create MySQL database**
   ```bash
   mysql -u root -p
   CREATE DATABASE bmi_project;
   ```

2. **Make the script executable**
   ```bash
   chmod +x run_pipeline.sh
   ```

3. **Run the pipeline**
   ```bash
   ./run_pipeline.sh
   ```

---

## Output

- CSV file with k-mer frequency table
- Logs printed to console with summary statistics
- SQL tables `Sample_Metadata` and `Kmer_Frequencies` populated

---

## Project Component
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
  
---

## Data Provenance
- The Human Microbiome Project (HMP): https://portal.hmpdacc.org/
The Human Microbiome Project supplies de-identified 16S rRNA sequencing data with metadata that encompasses oral cavity samples along with health status information.

- You can find the Human Oral Microbiome dataset among Kaggle's public datasets at https://www.kaggle.com/.
Public individuals upload these datasets to Kaggle where they can be accessed for research and educational use according to Kaggle's data use guidelines.

---

## Users
The project serves the following groups:

1. **Bioinformatics Students and Educators**  
- The project provides practical experience with microbiome data analysis techniques and SQL database design along with bash scripting automation.
- Educational setting: coursework, labs, and reproducibility exercises.

2. **Early-Career Researchers in Microbial Genomics or Oncology**  
- People who want to find microbial biomarkers and study how microbiome composition relates to various diseases.
- Researchers can use this tool during initial exploration projects or proof-of-concept testing.

3. **Healthcare Data Science Enthusiasts**  
- People who possess technical knowledge about Python or SQL programming are included in this context.
- This tool serves as a foundational resource for researchers who want to investigate non-invasive diagnostic methods or merge data with existing public health datasets.

---

## Implementation Constraints
- **Data Source Limitations**: Publicly available oral microbiome datasets serve as the foundation for this project. The presence of inconsistent metadata or limited annotations in these datasets affects the precision with which microbial signatures can be linked to disease status.

- **Computational Constraints**: The analysis of k-mer frequencies demands substantial memory resources when working with large FASTA files. This pipeline functions optimally with small to medium datasets which are appropriate for educational and research prototype applications but unsuitable for extensive clinical deployment.

- **Tooling Scope**: The project relies on fundamental Python programming, MySQL database management and Bash scripting without incorporating cloud deployment or complex workflow management systems like Snakemake or Nextflow.

- **No Clinical Validation**: The project incorporates Fusobacterium nucleatum as a biological marker but lacks clinical trial data and validated diagnostic standards. This project serves solely as a demonstration and learning tool.


- **Manual Integration Step**: The process of importing the SQL database from CSV files is semi-automated but may need manual checks due to MySQL settings and system access rights.
  
---

## References

- Badal, V. D., Balasubramanian, S., Sikaria, D., & Misra, V. (2020). Role of the gut microbiome in ageing and longevity: A systematic review. *Journal of Microbial Health and Aging, 6*(2), 123–135.
- Breiman, L. (2017). *Classification and Regression Trees*. Routledge, Taylor & Francis, New York.
- Bolyen, E., Rideout, J. R., Dillon, M. R., Bokulich, N. A., Abnet, C. C., et al. (2019). Reproducible, interactive, scalable, and extensible microbiome data science using QIIME 2. *Nature Biotechnology, 37*(8), 852–857.
- Chandrababu, R., & Bastola, A. (2022). The role of oral microbiota in regulating host immune responses: A systems perspective. *Oral Microbiology and Immunology, 15*(4), 241–253.
- Chattopadhyay, I., Verma, M., & Panda, M. (2019). Oral microbiome signatures in oral carcinoma: Diagnostic and therapeutic implications. *Journal of Oral Pathology and Medicine, 48*(6), 474–482.
- Gopinath, D., Mahesh, S., & Muthu, K. (2020). The role of oral microbiota in oral cancer development: An insight into the inflammatory and immune-modulatory mechanisms. *Frontiers in Immunology, 11*, Article 591088. https://doi.org/10.3389/fimmu.2020.591088
- Kim, S., Thapa, I., & Ali, H. (2024). A novel computational approach for the mining of signature pathways using species co-occurrence networks in gut microbiomes. *BMC Microbiology, 24*. https://doi.org/10.1186/s12866-024-03633-6
- Kostic, A. D., Chun, E., Robertson, L., Glickman, J. N., Gallini, C. A., et al. (2013). *Fusobacterium nucleatum* potentiates intestinal tumorigenesis and modulates the tumor-immune microenvironment. *Cell Host & Microbe, 14*(2), 207–215. https://doi.org/10.1016/j.chom.2013.07.007
- Kostic, A. D., Gevers, D., Pedamallu, C. S., Michaud, M., Duke, F., et al. (2013). Genomic analysis identifies association of *Fusobacterium* with colorectal carcinoma. *Genome Research, 22*(2), 292–298.
- Love, M. I., Huber, W., & Anders, S. (2014). Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2. *Genome Biology, 15*(12), 550–565.
- Putri, G. H., Anders, S., Pyl, P. T., Pimanda, J. E., & Zanini, F. (2022). Analysing high-throughput sequencing data in Python with HTSeq 2.0. *Bioinformatics, 38*(10), 2943–2945. https://doi.org/10.1093/bioinformatics/btac166
- Rubinstein, M. R., Wang, X., Liu, W., Hao, Y., Cai, G., & Han, Y. W. (2019). *Fusobacterium nucleatum* promotes colorectal cancer by modulating E-cadherin/β-catenin signaling via its FadA adhesin. *Cell Host & Microbe, 14*(2), 207–215. https://doi.org/10.1016/j.chom.2013.07.007
- Srinivasan, K., et al. (2020). Seasonal Effects of Humidity on Oral Microbiome Diversity. *Journal of Oral Ecology, 12*(3), 45–63.
- Johnson, T., & Williams, J. (2021). Statistical Methods in Microbiome Research. *Biostatistics Review, 18*(2), 101–120.
- Warnke-Sommer, J. D., & Ali, H. H. (2024). Evaluation of the Oral Microbiome as a Biomarker for Early Detection of Human Oral Carcinomas. *University of Nebraska Medical Center*.
- Xiao, E., Wang, Y., & Li, X. (2023). Oral microbiota dysbiosis in oral cancer progression and its therapeutic implications. *Phenomics, 3*(2), 124–133. https://doi.org/10.1007/s43657-023-00124-y

## Privacy Statement

The analysis in this project utilizes oral microbiome sequencing data that is publicly accessible from sources including the Human Microbiome Project and Kaggle.
The dataset contains no personal identifiers or protected health information (PHI) because it has undergone complete anonymization and de-identification.

The project's MySQL database avoids HIPAA, FERPA, and other data privacy regulation requirements.

The project is designed exclusively for educational and research activities and follows ethical guidelines when utilizing openly accessible data.

## License

This project is licensed under the [MIT License](./LICENSE).  
You are free to use, modify, and distribute this software, provided that proper credit is given and the license terms are followed.

For full details, see the LICENSE file included in this repository.
