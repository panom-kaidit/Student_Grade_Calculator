---
## Student Grade Calculator & Archive Manager
---
## Project Overview

A simple student grade calculator and archival utility that accepts assignment names, categories, grades, and weights, calculates weighted results for Formative and Summative assessments, generates GPA and pass/fail status, exports grade records to CSV, and archives generated CSV files with timestamps.

## Author

Panom Kaidit

## Folder Structure

- `grade-generator.py` - Python script for interactive grade input, validation, weighted grade calculation, GPA generation, and CSV export.
- `organizer.sh` - Bash script for archiving generated CSV files into an `archive` folder with timestamped filenames and a log file.
- `README.md` - Project documentation.

## How to Run

1. Open a terminal in the project folder.
2. Run the grade calculator with:

   ```bash
   python grade-generator.py
   ```

3. Follow the prompts to enter assignment name, category (`FA` or `SA`), grade, and weight.
4. After all required weights are entered (Formative total 60, Summative total 40), the script will display results and save data.

## Archiving Generated CSV Files

1. Run the archiving script after the grade calculator creates a CSV file:

   ```bash
   bash organizer.sh
   ```

2. The script moves any `.csv` file into the `archive` directory and appends archive details to `organizer.log`.
