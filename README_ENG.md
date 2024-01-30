# DRAFT Algorithm (Data-Driven Rating and Analysis for Football Talents)

The Football Analytics Suite project is designed to collect, process, normalize, and analyze football players' data. Using the DRAFT algorithm, the project assesses the performance and value of players on the field.

---

## Detailed Explanation of the DRAFT Algorithm

The DRAFT (Data-Driven Rating and Analysis for Football Talents) algorithm is an advanced system for analyzing football players. Its goal is to comprehensively evaluate player performance through a combination of advanced statistics and normalization methods.

### Use of the Algorithm

#### Multidimensional Evaluation
DRAFT evaluates multiple aspects of the game, including offensive and defensive skills, aerial play, and tactical contributions.

#### Data-Driven
Evaluations are based on data collected, cleaned, and normalized from reliable sources, ensuring an objective and performance-based evaluation.

### Interpretation of Results

#### Scale of 0 to 100
Each player receives a score on a scale of 0 to 100, where a higher score indicates superior performance.

#### Divisions by Seasons, Positions, and Leagues
Players are evaluated within their specific context: by seasons, positions, and leagues. This allows for monitoring performance evolution, recognizing different requirements by position, and comparing within the same competitive level.

### Practical Use

#### Scouting and Talent Analysis
DRAFT is essential for identifying standout or underestimated talents in different leagues and positions.

#### Strategic Evaluation
Enables coaches and strategists to assess strengths and weaknesses of their own team and opponents.

#### Player Development
Helps coaches identify specific areas for player improvement.

#### Comparisons and Benchmarks
Facilitates benchmarks among players from different leagues or seasons.

### Final Considerations

DRAFT is a dynamic and adaptable tool, capable of adjusting and evolving with new information and metrics.

### Conclusion

DRAFT provides a detailed and multifaceted view of player performance, making it an indispensable tool for football professionals worldwide.

---

## Discussion on the DRAFT Algorithm

### Challenges and Future of DRAFT

It is important to be transparent about potential issues and limitations of the DRAFT model, as well as its output. Below are some of these challenges, as well as possible improvements and future developments.

#### Current Challenges

- **Automation and Data Updating**: Although the process is now automated, it still requires time to navigate and update data on the Wyscout platform.
- **Interpretation of Scores**: Scores, after being manipulated and weighted, primarily serve to classify players in their roles.
- **Comparability of Scores**: Rankings are made within a specific data set, which can complicate comparisons between different data sets.
- **Defensive Data**: Classifying defensive attributes using only event data is complex and may not be as reliable as offensive data.
- **Physical Attributes**: It is currently not possible to classify or evaluate physical attributes.
- **Differentiation of Roles**: Some roles may be difficult to differentiate if key differences cannot be measured with the available data.
- **Data Quality**: The efficacy of the DRAFT model depends on the quality of the input data.

#### Future Developments

- **Use of Positional Attribute Averages**: To compare player performance more reliably and provide a counterpoint to relational scores.
- **Improvement of Data Presentation**: Work on the interpretation and visualization of data to make it understandable to the end user.
- **Integration of Visual Scouting**: Develop and combine visual scouting forms with the data-driven system for a holistic view of the player.
- **Easy Adjustment of Final Scores**: Allow end-users to apply different weightings, such as increasing 1v1 defense weighting for fullbacks.
- **Inclusion of Advanced Metrics**: Such as expected threat (xT) to add more context to key attributes.
- **Use of Possession and Field Tilt Data**: To reduce team bias in player data.
- **Use of League and Club Ratings**: To compare more effectively across leagues.

#### Final Thoughts and Feedback

If you have comments or suggestions about the DRAFT model, whether positive or negative, they are always welcome. You can contact me via email at nachomolinaruiz@gmail.com.

---

## Technical Process
### 1. Data Extraction (`01_data_extraction_2018_2022.R / 01_data_extraction_2023.R`)
#### Objective
Collect detailed data on football players.

#### Key Features
- Connection with API to obtain player statistics.
- Filtering and selection of relevant leagues and seasons.
- Data storage in Excel format.

#### R Libraries Used
- `rjson`
- `readxl`
- `dplyr`
- `stringr`
- `writexl`

#### Process
- Obtaining access token for the API.
- Extracting player statistics from different leagues.
- Initial data cleaning and formatting.
- Exporting data to an Excel file.

### 2. Data Cleaning (`02_data_cleaning.ipynb`)
#### Objective
Prepare data for analysis.

#### Key Features
- Reading data from Excel files.
- Selection and renaming of specific columns.
- Cleaning of null values and necessary transformations.

#### Python Libraries Used
- `pandas`

#### Process
- Loading data from Excel using `pandas`.
- Renaming columns for clarity.
- Handling missing or incorrect values.
- Consolidation of data from different seasons.

### 3. Data Normalization (`03_data_normalization.ipynb`)
#### Objective
Normalize player statistics.

#### Key Features
- Application of normalization techniques to player metrics.
- Ensuring comparability between players from different leagues and seasons.

#### Python Libraries Used
- `pandas`
- `numpy`

#### Process
- Calculation of thresholds and criteria for normalization.
- Normalization of individual statistics to a common scale.
- Combining normalized data with the original data set.

### 4. Performance Analysis (`04_performance_analysis.ipynb`)
#### Objective
Evaluate player performance using weighted metrics.

#### Key Features
- Application of a set of weights to normalized statistics.
- Calculation of a global performance score for each player.

#### Python Libraries Used
- `pandas`
- `numpy`

#### Process
- Definition of weights for different positions and metrics.
- Calculation of performance based on assigned weights.
- Rescaling of scores for uniform comparison.
- Exporting final data for analysis and visualization.

### Additional Considerations
- **Data Integration**: Ensuring a seamless data flow between stages.
- **Update and Maintenance**: Establishing protocols for updates and adjustments.
- **Visualization and Reporting**: Developing tools to visualize and report findings.

## Structure
This project includes several folders and files organized to facilitate development and analysis:

## Data Directory
- `data/`: Main folder for all data sets.
  - `raw/`: Stores raw data obtained from sources.
  - `cleaned/`: Contains data that has been cleaned and preprocessed.
  - `normalized/`: Data after applying normalization processes.
  - `final/`: Final processed data ready for analysis.

## Scripts and Notebooks Directory
- `directory/`: Includes project scripts and notebooks.
  - `R/`: R scripts for data extraction.
    - `01_data_extraction_2018_2022.R`: Data extraction for the 2018 to 2022 seasons.
    - `01_data_extraction_2023.R`: Data extraction for the 2023 season.
  - `Python/`: Python notebooks for cleaning, normalization, and analysis.
    - `02_data_cleaning.ipynb`: Notebook for data cleaning.
    - `03_data_normalization.ipynb`: Notebook for data normalization.
    - `04_performance_analysis.ipynb`: Notebook for performance analysis.
  - `READMES/`: READMEs for each script or notebook.

## Documentation
- `docs/`: Project documentation, additional notes, and reference materials.

## Main README
- `README.md`: General and detailed description of the project.

---

## Inspiration
Liam Henshaw - [Henshaw Analysis player ratings — methodology, discussion & examples](https://henshawanalysis.medium.com/henshaw-analysis-player-ratings-methodology-discussion-examples-555351393b9a)

Andy Watson - [AW Role Scouting System: The Launch](https://andywatsonsport.wordpress.com/2022/02/02/aw-role-scouting-system-the-launch/)

Rubén Sánchez-López, Ibon Echeazarra, and Julen Castellano Paulis - [Validation of an instrument to qualify football competence via WyScout](https://revista-apunts.com/en/validation-of-an-instrument-to-qualify-football-competence-via-wyscout/)

Previous personal work - [Scouting process and squad assembly R.C.D Espanyol for the season 23/24](https://www.linkedin.com/posts/ignaciomruiz_scouting-y-confecci%C3%B3n-de-plantilla-rcd-activity-7091011895117111296-AR6g?utm_source=share&utm_medium=member_desktop)
