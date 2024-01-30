# Overview
This script focuses on processing soccer player statistics, applying specific weights to normalized metrics to calculate players' final ratings.

# Prerequisites
- Python 3
- Pandas and NumPy libraries
- openpyxl library (for handling Excel files)

# Data File
- `player_stats_all_seasons_normalized.xlsx`: Contains normalized football player statistics.

# Key Steps in the Script
1. **Data Loading**: Player statistics data is loaded from an Excel file.

2. **Weight Application Function**: The function `aplicar_pesos` is defined, which takes a DataFrame and a dictionary of weights by position. This function applies the weights to the normalized metrics to calculate the final ratings of the players.

3. **Defining Weights by Position**: A dictionary with specific weights for each player position is defined.

4. **Calculating Final Ratings**: The `aplicar_pesos` function is used to calculate the final ratings of players in the DataFrame.

5. **Rescaling Results**: Results are rescaled to a range of 0 to 100 and rounded off.

6. **Column Cleanup**: Columns resulting from normalization are removed, and only relevant columns are kept.

7. **Exporting Processed Data**: The processed data is exported to an Excel file for later use.

# Customization
This script can be adapted for different data sets or player evaluation criteria by modifying the weights and metrics used.

# Note on File Paths
Make sure that the paths to the Excel files are correctly set to match your directory structure.
