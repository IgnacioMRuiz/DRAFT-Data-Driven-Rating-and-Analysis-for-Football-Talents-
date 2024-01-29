# Overview
This project focuses on normalizing player statistics from various sports seasons. The primary goal is to standardize these statistics to a 0-100 range, making comparisons across different seasons and conditions more straightforward and meaningful.

# Prerequisites
- Python 3
- Pandas library
- NumPy library
- openpyxl library for handling Excel files

# File Description
player_stats_all_seasons.xlsx: Excel file containing raw player statistics data across different seasons.

# Implementation Details
# Data Loading
The script starts by loading player statistics data from an Excel file using Pandas. Adjust the path to the Excel file as per your directory structure.

# Normalization Function
normalizar_estadisticas_por_grupo is the core function used for normalizing the statistics. It takes a DataFrame and a list of column names to be normalized.

- Parameters:
  - df: DataFrame containing player statistics.
  - columnas: List of columns to be normalized.

- Functionality:
  - The function calculates the minute threshold for the 2023 season and prepares a DataFrame for normalized columns.
  - It then iterates over the specified columns, grouping data by general position, season, and competition.
  - For each group, it normalizes the data to the 0-100 range based on z-scores.

# Normalization Process
Columns to be normalized are listed and fed into the function along with the DataFrame. The resultant DataFrame includes both original and normalized data.

# Data Export
The processed data is then exported to an Excel file for further analysis or usage.

# Note on Function Names
Function names are in Spanish due to the context of the project's application. Maintaining consistency in naming conventions throughout a project is essential. These names can be changed as long as the changes are orderly and consistent throughout the project. Specific steps for translating values or variable names are provided if necessary; if not required, this step can be omitted.
