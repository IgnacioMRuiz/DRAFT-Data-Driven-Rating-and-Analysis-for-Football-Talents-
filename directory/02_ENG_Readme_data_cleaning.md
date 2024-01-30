# Soccer Player Statistics Processing

## Overview
This script processes raw data of soccer player statistics from various seasons. It involves reading, cleaning, merging, and transforming data for further analysis and application.

## Prerequisites
- Python 3
- Pandas library
- openpyxl library (for handling Excel files)

## Data Files
- `player_stats_2018_2022_raw.xlsx`: Contains player statistics for the years 2018-2022.
- `player_stats_2013_raw.xlsx`: Contains player statistics for the year 2013.

## Key Steps in the Script
1. **Data Loading**: The script starts by loading player statistics data from the 2018-2022 and 2013 seasons using Pandas. Paths to these files should be adjusted according to your file structure.

2. **Data Merging**: Data from different seasons (2018-2022 and 2013) are merged into a single DataFrame.

3. **Data Cleaning**: The script cleans the data by replacing NA values with zeros, to be able to work with the numerical columns.

4. **Column Selection**: Specific columns are selected to be kept in the final dataset.

5. **Renaming Columns**: Columns are renamed to Spanish for better understanding in the given context.

6. **Type Conversion**: Certain columns are converted to numeric types for appropriate data handling.

7. **Position Mapping**: Detailed player positions are mapped to general position categories.

8. **Unique ID Creation**: A unique ID is created for each player based on multiple attributes.

9. **Date Processing**: Birth dates are converted to datetime, and players' ages are calculated.

10. **Data Translation**: Competition names and player footedness are translated from English to Spanish.

11. **Duplicate Removal**: Duplicate rows based on the unique ID are removed.

12. **Data Export**: The processed data is exported to an Excel file for further use.

## Note on File Paths
Please ensure that the paths to the Excel files are correctly set to match your directory structure.

## Customization
Feel free to modify the script to suit your specific data processing needs.
