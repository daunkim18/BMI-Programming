# A Reproducible SQL-Driven Pipeline for Oral Microbiome Analysis and Visualization of Genus-Level Biomarkers in Depression 
**Author: Daun Kim**  
**Course: BMI 8540 – Final Project**

---

## Abstract & Purpose
The project introduces a repeatable bioinformatics pipeline that processes oral microbiome information to evaluate its connection with mental health disorders with depression as the central focus. The main goal of this study is to show the variations in oral microbial composition between depressed individuals and healthy controls by examining the prevalence of the Prevotella genus. The pipeline integrates three key components: The project pipeline features Python scripts that manage data and create visualizations in conjunction with an SQL database schema for organized data storage and a Bash script designed to automate tasks.

The `import_microbiome_csv.py` script extracts selected rows from the large `oral_microbiome.csv` file to load them into a MySQL database. The `visualize_prevotella.py` script accesses database information to generate a boxplot that compares the abundance of Prevotella between depressed and non-depressed individuals. The database itself is defined using the `oral_microbiome_schema.sql` file, which creates two tables: `Subject_metadata` table saves participant IDs alongside depression status information while `genus_abundance` table contains relative abundance data sorted by genus. The `pipeline.sh` script connects all components to provide an automated workflow that functions smoothly.
 
![image](https://github.com/user-attachments/assets/1587cbd1-7c04-4de9-9604-7cbf136ba062)

Initial results from this limited demonstration indicate a higher median level of Prevotella among people categorized with depression than those without depression which indicates potential for further research into Prevotella as a non-invasive microbial biomarker for mental health conditions. This project demonstrates the combined application of Python, SQL, and Bash foundational tools to perform valuable biomedical informatics analyses.

The project delivers a proof-of-concept tool for detecting depression biomarkers through streamlined oral microbiome analysis using a modular and reproducible method. The early data demonstrates that samples identified as oral carcinoma exhibit increased relative frequencies of patterns connected to Prevotella which suggests its usefulness as a diagnostic microbial marker.

## Research Question
How does the relative abundance of *Prevotella* differ between individuals with and without depression, and can this difference suggest a potential microbial biomarker for mental health screening?

---

## Objectives & Goals
1. Build a Python-based importer to load microbiome data into MySQL.
2. Define SQL schema linking metadata and genus abundance.
3. Generate a visualization showing abundance differences in *Prevotella* between groups.
4. Automate the full workflow using Bash for reproducibility.
![image](https://github.com/user-attachments/assets/df111a2f-4501-4688-a5d4-91f3f94b7d71)

---

## Background



As one of the most widespread and lethal head and neck cancers globally oral squamous cell carcinoma (OSCC) continues to be diagnosed primarily at late stages because of insufficient early, non-invasive detection methods. Emerging microbiome research demonstrates how oral microbiota significantly impacts human health and disease development including cancer formation. The oral cavity hosts a complex microbiome ecosystem consisting of bacteria, viruses and fungi which maintains continuous interaction with the host immune system and mucosal surfaces to potentially serve as biomarkers for early cancer detection (Chattopadhyay et al., 2019; Xiao et al., 2023).

Fusobacterium nucleatum stands out as a significant microbe associated with the development of oral and colorectal cancers among microbial taxa that impact cancer progression. Research demonstrates that this bacterium disrupts epithelial barriers and triggers immune responses and inflammation which together advance tumorigenesis (Rubinstein et al., 2019). Fusobacterium nucleatum enhances colorectal cancer progression through E-cadherin/β-catenin signaling activation and tumor microenvironment modulation (Kostic et al., 2013). Research into oral cancer reveals mechanisms that allow bacteria to establish environments conducive to malignant transformation using inflammatory pathways and immune evasion strategies (Chandrababu & Bastola, 2022; Gopinath et al., 2020).

Microbial changes that result in microbiome dysbiosis can function as early indicators for cancer development. Changes in the abundance of specific microbial taxa occur during dysbiosis in cancer patients as shown by elevated levels of Prevotella and Fusobacterium compared to healthy individuals (Warnke-Sommer & Ali, 2024). The analysis of Prevotella bacterial genera composition and abundance helps researchers discover non-invasive biomarkers useful for diagnosis and prognosis. Biomarker development holds substantial value in areas lacking advanced medical resources and for patients who cannot access high-end imaging or biopsy methods.

This project investigates how to build a structured pipeline for oral microbiome data analysis through the use of open-source bioinformatics tools in response to this need. The workflow combines Python's data processing capabilities with MySQL's structured storage solution and Bash scripting automation to achieve a lightweight and repeatable system. Users can import microbiome data from CSV files into a relational database and create visualizations of specific bacterial genus abundances such as Prevotella based on depression status through the pipeline. Even though the primary goal was cancer detection research I shifted my focus to mental health associations after discovering depression-labeled data from public datasets like Kaggle.

Accessible sequencing data paired with computational tools enables researchers to discover significant biological patterns. This framework demonstrates scalability for larger studies of 16S rRNA or metagenomic data despite its current analysis being restricted to a small subset of rows. This system facilitates future research targeting the discovery of microbiota-based disease biomarkers while enhancing early detection methods and developing digital infrastructure essential for precision medicine based on microbiome data.

![image](https://github.com/user-attachments/assets/d227ea4d-2d88-4e9b-8ba1-d9831f67a2f8)

![image](https://github.com/user-attachments/assets/41dae534-8105-4530-9386-136817633110)

Image Source: ScienceDirect Topics on Prevotella

---

## Installation & Usage
### Dependencies
- Python 3.x
- MySQL Server
- Bash shell
- mysql-connector-python==9.3.0
- SQLAlchemy==2.0.40
- pandas
- matplotlib

- Install required Python packages:
  ```bash
  pip install mysql-connector-python pandas matplotlib sqlalchemy
  ```

### Step-by-Step
1. **Create MySQL Database**
   ```bash
   mysql -u root -p < oral_microbiome_schema.sql
   ```

2. **Make Bash script executable**
   ```bash
   chmod +x pipeline.sh
   ```

3. **Run the pipeline**
   ```bash
   ./pipeline.sh
   ```

---

## Output
- MySQL database


![image](https://github.com/user-attachments/assets/8f5beb79-fa4a-40c0-a740-7c4b1a8d70ac)
  
![image](https://github.com/user-attachments/assets/0d243c1d-026f-4b52-a516-c1fa094da02c)

- CSV output 
- Box plot comparing *Prevotella* abundance between depression groups

![image](https://github.com/user-attachments/assets/6606aed7-c616-47a4-ab02-80af32d8019d)

---

## Project Component
### 1. Python Scripts
- Import CSV to database 
- Plot *Prevotella* genus abundance using `matplotlib`

### 2. SQL File
- Creates `bmi_project` database
- Defines table structure to hold metadata and genus abundance

### 3. Bash Script
- Run the full pipeline

![image](https://github.com/user-attachments/assets/0227b150-de80-4180-a359-e708b5887fa6)

---

## Data Provenance
- I downloaded the dataset from Kaggle by accessing it directly as a CSV file.
- Dataset Source: [Kaggle - Oral Microbiome in Depression and Non-Depression](https://www.kaggle.com/datasets/forestlan/oral-microbiome)
- The dataset is public and fully anonymized without including any personally identifiable information (PII) which assures adherence to standard privacy and ethical research standards.
- The original contributors who posted the dataset on Kaggle retain ownership while permitting its reuse for non-commercial purposes including academic research and data science education. The use of this data did not require extra permissions and no preprocessing activities threatened subject privacy.

---


## Target Users
- **Bioinformatics Students**: Apply SQL, scripting, and visualization in a unified workflow.
- **Researchers in Microbiome & Mental Health**: Prototype and explore microbial biomarkers.
- **Data Science Practitioners**: Extend the project to other public microbiome datasets or integrate with external clinical data.

---

## Implementation Constraints
- **Data Source Limitations**: Publicly available oral microbiome datasets serve as the foundation for this project. The presence of inconsistent metadata or limited annotations in these datasets affects the precision with which microbial signatures can be linked to disease status.

- **Computational Constraints**: This pipeline functions optimally with small to medium datasets which are appropriate for educational and research prototype applications but unsuitable for extensive clinical deployment. Not designed for high-throughput or clinical-scale datasets. Only supports small datasets in demonstration mode.

- **Tooling Scope**: The project relies on fundamental Python programming, MySQL database management and Bash scripting. Command-line only; no web or graphical interface.

- **No Clinical Validation**: The project incorporates Prevotella as a biological marker but lacks clinical trial data and validated diagnostic standards. This project serves solely as a demonstration and learning tool. Not clinically validated.

- **Manual Integration Step**: The process of importing the SQL database from CSV files is semi-automated but may need manual checks due to MySQL settings and system access rights. MySQL setup may require admin access.
  
---

## References

1. Badal, V. D., Balasubramanian, S., Sikaria, D., & Misra, V. (2020). Role of the gut microbiome in ageing and longevity: A systematic review. *Journal of Microbial Health and Aging*, 6(2), 123–135.

2. Bolyen, E., Rideout, J. R., Dillon, M. R., Bokulich, N. A., Abnet, C. C., et al. (2019). Reproducible, interactive, scalable, and extensible microbiome data science using QIIME 2. *Nature Biotechnology*, 37(8), 852–857.

3. Breiman, L. (2017). *Classification and Regression Trees*. Routledge, Taylor & Francis, New York.

4. Chandrababu, R., & Bastola, A. (2022). The role of oral microbiota in regulating host immune responses: A systems perspective. *Oral Microbiology and Immunology*, 15(4), 241–253.

5. Chattopadhyay, I., Verma, M., & Panda, M. (2019). Oral microbiome signatures in oral carcinoma: Diagnostic and therapeutic implications. *Journal of Oral Pathology and Medicine*, 48(6), 474–482.

6. Elsevier. (n.d.). *Prevotella*. In *ScienceDirect Topics*. Retrieved April 28, 2025, from https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/prevotella

7. Gopinath, D., Mahesh, S., & Muthu, K. (2020). The role of oral microbiota in oral cancer development: An insight into the inflammatory and immune-modulatory mechanisms. *Frontiers in Immunology*, 11, Article 591088. https://doi.org/10.3389/fimmu.2020.591088

8. Johnson, T., & Williams, J. (2021). Statistical Methods in Microbiome Research. *Biostatistics Review*, 18(2), 101–120.

9. Kim, S., Thapa, I., & Ali, H. (2024). A novel computational approach for the mining of signature pathways using species co-occurrence networks in gut microbiomes. *BMC Microbiology*, 24. https://doi.org/10.1186/s12866-024-03633-6

10. Kostic, A. D., Chun, E., Robertson, L., Glickman, J. N., Gallini, C. A., et al. (2013). Fusobacterium nucleatum potentiates intestinal tumorigenesis and modulates the tumor-immune microenvironment. *Cell Host & Microbe*, 14(2), 207–215. https://doi.org/10.1016/j.chom.2013.07.007

11. Kostic, A. D., Gevers, D., Pedamallu, C. S., Michaud, M., Duke, F., et al. (2013). Genomic analysis identifies association of Fusobacterium with colorectal carcinoma. *Genome Research*, 22(2), 292–298.

12. Love, M. I., Huber, W., & Anders, S. (2014). Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2. *Genome Biology*, 15(12), 550–565.

13. Putri, G. H., Anders, S., Pyl, P. T., Pimanda, J. E., & Zanini, F. (2022). Analysing high-throughput sequencing data in Python with HTSeq 2.0. *Bioinformatics*, 38(10), 2943–2945. https://doi.org/10.1093/bioinformatics/btac166

14. Rubinstein, M. R., Wang, X., Liu, W., Hao, Y., Cai, G., & Han, Y. W. (2019). Fusobacterium nucleatum promotes colorectal cancer by modulating E-cadherin/β-catenin signaling via its FadA adhesin. *Cell Host & Microbe*, 14(2), 207–215. https://doi.org/10.1016/j.chom.2013.07.007

15. Srinivasan, K., et al. (2020). Seasonal Effects of Humidity on Oral Microbiome Diversity. *Journal of Oral Ecology*, 12(3), 45–63.

16. Warnke-Sommer, J. D., & Ali, H. H. (2024). Evaluation of the Oral Microbiome as a Biomarker for Early Detection of Human Oral Carcinomas. *University of Nebraska Medical Center*.

17. Xiao, E., Wang, Y., & Li, X. (2023). Oral microbiota dysbiosis in oral cancer progression and its therapeutic implications. *Phenomics*, 3(2), 124–133. https://doi.org/10.1007/s43657-023-00124-y
    
---

## Privacy Statement

The analysis in this project utilizes oral microbiome sequencing data that is publicly accessible from sources including the Human Microbiome Project and Kaggle.
The dataset contains no personal identifiers or protected health information (PHI) because it has undergone complete anonymization and de-identification.

The project's MySQL database avoids HIPAA, FERPA, and other data privacy regulation requirements.

The project is designed exclusively for educational and research activities and follows ethical guidelines when utilizing openly accessible data.

---

## License

This project is licensed under the [MIT License](./LICENSE).  
You are free to use, modify, and distribute this software, provided that proper credit is given and the license terms are followed.

For full details, see the LICENSE file included in this repository.
