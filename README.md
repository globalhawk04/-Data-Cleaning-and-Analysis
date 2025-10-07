Data Cleaning and Analysis Scripts

This repository contains a suite of Python scripts focused on data cleaning, transformation, analysis, and preparation. These scripts are designed to handle common data wrangling tasks, such as splitting columns, parsing fixed-width files, identifying duplicate entries, and tagging data based on specific criteria.

Table of Contents

Description

Scripts Included

Prerequisites

Usage

General Notes

Description

The scripts in this collection are built primarily using the pandas and built-in csv libraries to process data stored in CSV files. They address real-world data challenges, from cleaning inconsistently formatted source files to performing comparative analysis across multiple datasets. This repository is ideal for anyone looking for practical examples of data manipulation tasks in Python.

Scripts Included

Here is a breakdown of the scripts available in this repository:

1. cision_split.py

Purpose: Cleans media contact data where the outlet name and its location are merged into a single cell.

Functionality: Reads a CSV file named All_Media.csv. It searches for various delimiters (–, -, --, etc.) within a specific column. When a delimiter is found, it splits the string into two parts—media_name and media_city—and appends them to separate lists. This is a classic data cleaning task for handling inconsistent entry formats.

Dependencies: pandas, csv.

2. fm_split.py

Purpose: Parses fixed-width text data to extract structured information.

Functionality: This script is designed to handle a specific fixed-width format. It reads rows from am_split.csv and uses Python's string slicing to extract specific character ranges that correspond to station, city, and state. The extracted data is then saved into a new, well-structured CSV file named am.csv.

Dependencies: pandas, csv.

3. compare_create.py

Purpose: Compares keyword data from multiple sources to find common (duplicate) keywords.

Functionality: The script reads a list of CSV files, each containing keyword data for a different entity (e.g., a university). It combines all data into a single DataFrame and then uses pandas.groupby() to identify and isolate keywords that appear in more than one source file. This is useful for competitive analysis to find overlapping areas of interest.

Dependencies: pandas, csv.

4. search_keyword.py

Purpose: Filters a large keyword dataset to find rows containing specific, predefined terms.

Functionality: Reads a master CSV file (All_Schools_All_Keyword.csv) and searches for a list of keywords (e.g., 'anthropology', 'biology'). It extracts every row where the keyword column contains one of these terms and saves the results to a new CSV. This is a powerful tool for segmenting large datasets based on specific criteria.

Dependencies: pandas, csv.

5. transport.py

Purpose: Analyzes and segments web traffic data from a transportation services website.

Functionality: This script processes a web analytics export (transport_main.csv). It defines a list of categories (e.g., 'parking', 'transit', 'football'). It then iterates through the data, "tagging" each URL that matches a category. It calculates and compares key metrics (like bounce rate and average time on page) for the tagged segments versus the overall traffic and removes duplicate entries before saving.

Dependencies: pandas, csv.

6. Fan_Loop_Tag.py

Purpose: Provides a structural template for enriching a dataset by cross-referencing it with a "tag" file.

Functionality: Although using placeholder file names, the logic of this script is to read a main data file and a second file containing tags (e.g., a list of names and their corresponding categories). It then loops through the main file and adds the correct tag to each row based on a matching key. This is a foundational script for data enrichment tasks.

Dependencies: pandas, csv.

Prerequisites

To run these scripts, you will need Python 3 installed. You will also need to install the pandas library.

You can install the necessary library using pip:

code
Bash
download
content_copy
expand_less
pip install pandas
Usage

Clone the repository:

code
Bash
download
content_copy
expand_less
git clone https://github.com/your-username/data-cleaning-and-analysis.git
cd data-cleaning-and-analysis

Prepare your input files:

Place the required input CSV files (e.g., All_Media.csv, transport_main.csv) in the same directory as the scripts.

Ensure the CSV files are formatted as expected by the script you intend to run.

Modify the script:

Open the script you want to use and update any hardcoded file names or paths to match your own files.

Run the script from your terminal:

code
Bash
download
content_copy
expand_less
python cision_split.py
General Notes

Hardcoded Filenames: Most scripts contain hardcoded input and output filenames. You will need to modify these variables within the scripts to suit your needs.

Data Structure: The scripts are tailored to specific CSV structures. If your data format differs, you will need to adjust the column indices or header names accordingly.
