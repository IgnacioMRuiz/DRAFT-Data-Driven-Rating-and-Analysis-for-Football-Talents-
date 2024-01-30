import pandas as pd
from datetime import datetime

# Adjust the path as per your file structure
file_path_2018_2022 = '/Users/nacho/Desktop/DV7/Pyhton_Coded_Algorithem/data/Raw/player_stats_2018_2022_raw.xlsx'
file_path_2013 = '/Users/nacho/Desktop/DV7/Pyhton_Coded_Algorithem/data/Raw/player_stats_2013_raw.xlsx'

# Read the Excel files
player_stats_2018_2022_raw = pd.read_excel(file_path_2018_2022, engine='openpyxl')
player_stats_2013_raw = pd.read_excel(file_path_2013, engine='openpyxl')

# Merge data from different seasons
player_stats_all_seasons = pd.concat([player_stats_2018_2022_raw, player_stats_2013_raw], ignore_index=True)

# Clean the data by replacing NA values with zeros
player_stats_all_seasons.fillna(0, inplace=True)

# Select specific columns to keep
columns_to_keep = [
    "id", "full_name", "name", "image", "primary_position", "secondary_position",
    "passport_country_names1", "passport_country_names2", "birth_date", "age",
    "last_club_name", "current_team_logo", "total_matches", "minutes_on_field",
    "height", "foot", "market_value", "Competition", "Season", "fouls_avg",
    "yellow_cards", "yellow_cards_avg", "red_cards", "red_cards_avg",
    "foul_suffered_avg", "accelerations_avg", "progressive_run_avg",
    "conceded_goals", "conceded_goals_avg", "xg_save", "xg_save_avg",
    "clean_sheets", "shots_against", "shots_against_avg", "shot_block_avg",
    "save_percent", "prevented_goals", "goalkeeper_exits_avg",
    "gk_aerial_duels_avg", "prevented_goals_avg", "successful_defensive_actions_avg",
    "interceptions_avg", "possession_adjusted_interceptions", "tackle_avg",
    "possession_adjusted_tackle", "duels_avg", "duels_won",
    "defensive_duels_won", "defensive_duels_avg", "aerial_duels_avg",
    "aerial_duels_won", "offensive_duels_won", "offensive_duels_avg",
    "passes_avg", "accurate_passes_percent", "short_medium_pass_avg",
    "accurate_short_medium_pass_percent", "average_pass_length",
    "forward_passes_avg", "successful_forward_passes_percent",
    "vertical_passes_avg", "successful_vertical_passes_percent",
    "key_passes_avg", "smart_passes_avg", "accurate_smart_passes_percent",
    "passes_to_final_third_avg", "accurate_passes_to_final_third_percent",
    "successful_through_passes_percent", "through_passes_avg",
    "deep_completed_pass_avg", "accurate_crosses_percent",
    "progressive_pass_avg", "successful_progressive_pass_percent",
    "pass_to_penalty_area_avg", "accurate_pass_to_penalty_area_percent",
    "crosses_avg", "cross_from_right_avg", "successful_cross_from_right_percent",
    "cross_from_left_avg", "successful_cross_from_left_percent",
    "cross_to_goalie_box_avg", "deep_completed_cross_avg", "long_passes_avg",
    "average_long_pass_length", "successful_long_passes_percent",
    "received_pass_avg", "received_long_pass_avg", "assists", "assists_avg",
    "xg_assist", "xg_assist_avg", "pre_assist_avg", "pre_pre_assist_avg",
    "shot_assists_avg", "back_passes_avg", "successful_back_passes_percent",
    "back_pass_to_gk_avg", "successful_attacking_actions_avg", "dribbles_avg",
    "successful_dribbles_percent", "shots", "shots_avg",
    "shots_on_target_percent", "xg_shot", "xg_shot_avg", "goals", "goals_avg",
    "head_goals", "head_goals_avg", "touch_in_box_avg", "non_penalty_goal",
    "non_penalty_goal_avg", "penalties_taken", "penalties_conversion_percent",
    "goal_conversion_percent", "free_kicks_taken_avg",
    "direct_free_kicks_taken_avg", "direct_free_kicks_on_target_percent",
    "corners_taken_avg"
]
player_stats_all_seasons = player_stats_all_seasons[columns_to_keep]

#Renaming columns
column_names_spanish = {
    "id": "Id",
    "full_name": "Nombre Completo",
    "name": "Nombre",
    "image": "Imagen",
    "primary_position": "Posición Principal",
    "secondary_position": "Posición Secundaria",
    "passport_country_names1": "Nacionalidad 1",
    "passport_country_names2": "Nacionalidad 2",
    "birth_date": "Fecha De Nacimiento",
    "age": "Edad",
    "last_club_name": "Último Club",
    "current_team_logo": "Logo del Club",
    "total_matches": "Partidos",
    "minutes_on_field": "Minutos",
    "height": "Altura",
    "foot": "Lateralidad",
    "market_value": "Valor De Mercado",
    "Competition": "Competición",
    "Season": "Temporada",
    "fouls_avg": "Faltas x90",
    "yellow_cards": "Tarjetas Amarillas",
    "yellow_cards_avg": "Tarjetas Amarillas x90",
    "red_cards": "Tarjetas Rojas",
    "red_cards_avg": "Tarjetas Rojas x90",
    "foul_suffered_avg": "Faltas Sufridas x90",
    "accelerations_avg": "Aceleraciones x90",
    "progressive_run_avg": "Carreras Progresivas x90",
    "conceded_goals": "Goles Concedidos",
    "conceded_goals_avg": "Goles Concedidos x90",
    "xg_save": "Xg Parado",
    "xg_save_avg": "Xg Parado x90",
    "clean_sheets": "Porterías A Cero",
    "shots_against": "Tiros En Contra",
    "shots_against_avg": "Tiros En Contra x90",
    "shot_block_avg": "Paradas x90",
    "save_percent": "Paradas, %",
    "prevented_goals": "Goles Prevenidos",
    "goalkeeper_exits_avg": "Salidas Del Portero x90",
    "gk_aerial_duels_avg": "Duelos Aéreos Del Portero x90",
    "prevented_goals_avg": "Goles Prevenidos x90",
    "successful_defensive_actions_avg": "Acciones Defensivas Exitosas x90",
    "interceptions_avg": "Intercepciones x90",
    "possession_adjusted_interceptions": "Intercepciones AjPos x90",
    "tackle_avg": "Entradas x90",
    "possession_adjusted_tackle": "Entradas AjPos x90",
    "duels_avg": "Duelos x90",
    "duels_won": "Duelos Ganados",
    "defensive_duels_won": "Duelos Defensivos Ganados",
    "defensive_duels_avg": "Duelos Defensivos x90",
    "aerial_duels_avg": "Duelos Aéreos x90",
    "aerial_duels_won": "Duelos Aéreos Ganados",
    "offensive_duels_won": "Duelos Ofensivos Ganados",
    "offensive_duels_avg": "Duelos Ofensivos x90",
    "passes_avg": "Pases x90",
    "accurate_passes_percent": "Pases Completados, %",
    "short_medium_pass_avg": "Pases Cortos Y Medios x90",
    "accurate_short_medium_pass_percent": "Pases Cortos Y Medios Completados, %",
    "average_pass_length": "Longitud Promedio De Pase",
    "forward_passes_avg": "Pases Hacia Adelante x90",
    "successful_forward_passes_percent": "Pases Hacia Adelante Completados, %",
    "vertical_passes_avg": "Pases Verticales x90",
    "successful_vertical_passes_percent": "Pases Verticales Completados, %",
    "key_passes_avg": "Pases Clave x90",
    "smart_passes_avg": "Pases Inteligentes x90",
    "accurate_smart_passes_percent": "Pases Inteligentes Completados, %",
    "passes_to_final_third_avg": "Pases a Último Tercio x90",
    "accurate_passes_to_final_third_percent": "Pases Completados a Último Tercio, %",
    "successful_through_passes_percent": "Pases al espacio Exitosos, %",
    "through_passes_avg": "Pases al espacio x90",
    "deep_completed_pass_avg": "Pase Profundo Completado x90",
    "accurate_crosses_percent": "Centros Completados, %",
    "progressive_pass_avg": "Pase Progresivo x90",
    "successful_progressive_pass_percent": "Pase Progresivo Completados, %",
    "pass_to_penalty_area_avg": "Pase A Área De Penalti x90",
    "accurate_pass_to_penalty_area_percent": "Pase Preciso A Área De Penalti, %",
    "crosses_avg": "Centros x90",
    "cross_from_right_avg": "Centros Desde La Derecha x90",
    "successful_cross_from_right_percent": "Centros Completados Desde La Derecha, %",
    "cross_from_left_avg": "Centros Desdes La Izquierda x90",
    "successful_cross_from_left_percent": "Centros Completados Desde La Izquierda, %",
    "cross_to_goalie_box_avg": "Centros al Área x90",
    "deep_completed_cross_avg": "Centros Profundos Completados x90",
    "long_passes_avg": "Pases Largos x90",
    "average_long_pass_length": "Longitud Promedio De Pase Largo",
    "successful_long_passes_percent": "Pases Largos Completados, %",
    "received_pass_avg": "Pases Recibidos x90",
    "received_long_pass_avg": "Pases Largos Recibido x90",
    "assists": "Asistencias",
    "assists_avg": "Asistencias x90",
    "xg_assist": "xA",
    "xg_assist_avg": "xA x90",
    "pre_assist_avg": "Preasistencia x90",
    "pre_pre_assist_avg": "Pre Preasistencia x90",
    "shot_assists_avg": "Asistencias De Tiro x90",
    "back_passes_avg": "Pases Hacia Atrás x90",
    "successful_back_passes_percent": "Pases Hacia Atrás Completados, %",
    "back_pass_to_gk_avg": "Pase Hacia Atrás Al Portero x90",
    "successful_attacking_actions_avg": "Acciones Ofensivas Completados x90",
    "dribbles_avg": "Regates x90",
    "successful_dribbles_percent": "Regates Completados, %",
    "shots": "Tiros",
    "shots_avg": "Tiros x90",
    "shots_on_target_percent": "Tiros A Puerta, %",
    "xg_shot": "Xg",
    "xg_shot_avg": "Xg x90",
    "goals": "Goles",
    "goals_avg": "Goles x90",
    "head_goals": "Goles De Cabeza",
    "head_goals_avg": "Goles De Cabeza x90",
    "touch_in_box_avg": "Toques En El Área x90",
    "non_penalty_goal": "Goles sin Penalti",
    "non_penalty_goal_avg": "Goles sin Penalti x90",
    "penalties_taken": "Penaltis Tirados",
    "penalties_conversion_percent": "Penaltis Marcados, %",
    "goal_conversion_percent": "Tasa de Conversión de Gol, %",
    "free_kicks_taken_avg": "Tiros Libres Tirados x90",
    "direct_free_kicks_taken_avg": "Tiros Libres Directos Tirados x90",
    "direct_free_kicks_on_target_percent": "Tiros Libres Directos A Puerta, %",
    "corners_taken_avg": "Córners Tirados x90"
}
player_stats_all_seasons.rename(columns=column_names_spanish, inplace=True)

# Convert certain columns to numeric types
columns_to_convert = [
    "Edad", "Minutos", "Altura", "Valor De Mercado", "Temporada", "Faltas x90","Tarjetas Amarillas", "Tarjetas Amarillas x90",
    "Tarjetas Rojas", "Tarjetas Rojas x90", "Faltas Sufridas x90", "Aceleraciones x90", "Carreras Progresivas x90",
    "Goles Concedidos", "Goles Concedidos x90", "Xg Parado", "Xg Parado x90", "Porterías A Cero", "Tiros En Contra", "Tiros En Contra x90", 
    "Paradas x90", "Paradas, %", "Goles Prevenidos", "Salidas Del Portero x90", "Duelos Aéreos Del Portero x90", "Goles Prevenidos x90", 
    "Acciones Defensivas Exitosas x90", "Intercepciones x90", "Intercepciones AjPos x90", "Entradas x90", "Entradas AjPos x90", "Duelos x90", 
    "Duelos Ganados", "Duelos Defensivos Ganados", "Duelos Defensivos x90", "Duelos Aéreos x90", "Duelos Aéreos Ganados", 
    "Duelos Ofensivos Ganados", "Duelos Ofensivos x90", "Pases x90", "Pases Completados, %", "Pases Cortos Y Medios x90", 
    "Pases Cortos Y Medios Completados, %", "Longitud Promedio De Pase", "Pases Hacia Adelante x90", "Pases Hacia Adelante Completados, %",
    "Pases Verticales x90", "Pases Verticales Completados, %", "Pases Clave x90", "Pases Inteligentes x90", "Pases Inteligentes Completados, %", 
    "Pases a Último Tercio x90", "Pases Completados a Último Tercio, %", "Pases al espacio Exitosos, %", "Pases al espacio x90",
    "Pase Profundo Completado x90", "Centros Completados, %", "Pase Progresivo x90", "Pase Progresivo Completados, %", 
    "Pase A Área De Penalti x90", "Pase Preciso A Área De Penalti, %", "Centros x90", "Centros Desde La Derecha x90", 
    "Centros Completados Desde La Derecha, %", "Centros Desdes La Izquierda x90", "Centros Completados Desde La Izquierda, %",
    "Centros al Área x90", "Centros Profundos Completados x90", "Pases Largos x90", "Longitud Promedio De Pase Largo", 
    "Pases Largos Completados, %", "Pases Recibidos x90", "Pases Largos Recibido x90", "Asistencias", "Asistencias x90", "xA", "xA x90",
    "Preasistencia x90", "Pre Preasistencia x90", "Asistencias De Tiro x90", "Pases Hacia Atrás x90", "Pases Hacia Atrás Completados, %", 
    "Pase Hacia Atrás Al Portero x90", "Acciones Ofensivas Completados x90", "Regates x90", "Regates Completados, %", "Tiros", "Tiros x90", 
    "Tiros A Puerta, %", "Xg", "Xg x90", "Goles", "Goles x90", "Goles De Cabeza", "Goles De Cabeza x90", "Toques En El Área x90",
    "Goles sin Penalti", "Goles sin Penalti x90", "Penaltis Tirados", "Penaltis Marcados, %", "Tasa de Conversión de Gol, %", 
    "Tiros Libres Tirados x90", "Tiros Libres Directos Tirados x90", "Tiros Libres Directos A Puerta, %", "Córners Tirados x90"
]
player_stats_all_seasons[columns_to_convert] = player_stats_all_seasons[columns_to_convert].apply(pd.to_numeric, errors='coerce')

# Mapping detailed positions to general position categories with Spanish names
position_mapping = {
    'GK': 'Portero',
    'RB': 'Lateral Derecho', 'RWB': 'Lateral Derecho', 'RB5': 'Lateral Derecho',
    'LB': 'Lateral Izquierdo', 'LWB': 'Lateral Izquierdo', 'LB5': 'Lateral Izquierdo',
    'CB': 'Central', 'LCB': 'Central', 'RCB': 'Central', 'RCB3': 'Central', 'LCB3': 'Central',
    'DMF': 'Mediocentro (6)', 'LDMF': 'Mediocentro (6)', 'RDMF': 'Mediocentro (6)',
    'LCMF': 'Mediocentro (8)', 'LCMF3': 'Mediocentro (8)', 'RCMF': 'Mediocentro (8)', 'RCMF3': 'Mediocentro (8)',
    'AMF': 'Mediocentro (10)',
    'LW': 'Extremo Izquierdo', 'LWF': 'Extremo Izquierdo', 'LAMF': 'Extremo Izquierdo',
    'RW': 'Extremo Derecho', 'RWF': 'Extremo Derecho', 'RAMF': 'Extremo Derecho',
    'CF': 'Delantero'
}

# Apply the mapping to create a new 'Posición_General' column
player_stats_all_seasons['Posición_General'] = player_stats_all_seasons['Posición Principal'].map(position_mapping)

# Note: Ensure 'Posición Principal' is the correct column in your DataFrame that contains the position siglas.
# If the column name is different, replace 'Posición Principal' with the actual column name.


#Creating a Unique ID
player_stats_all_seasons['ID_unico'] = player_stats_all_seasons.apply(lambda row: f"{row['Id']}-{row['Temporada']}-{row['Último Club']}", axis=1)

# Convert 'Fecha De Nacimiento' to datetime
player_stats_all_seasons['Fecha De Nacimiento'] = pd.to_datetime(player_stats_all_seasons['Fecha De Nacimiento'])

# Calculate 'Birth Year'
player_stats_all_seasons['Año de nacimiento'] = player_stats_all_seasons['Fecha De Nacimiento'].dt.year

# Calculate 'Age at the Start of the Season' and 'Current Age'
current_year = datetime.now().year

player_stats_all_seasons['Edad Temporada'] = player_stats_all_seasons['Temporada'].astype(int) - player_stats_all_seasons['Año de nacimiento']

player_stats_all_seasons['Edad Actual'] = current_year - player_stats_all_seasons['Año de nacimiento']

# Create the new column "Diferencia xG/Goles"
player_stats_all_seasons['Diferencia xG/Goles'] = player_stats_all_seasons['Goles'] - player_stats_all_seasons['Xg']

# Translating competition names from English to Spanish
competition_translation = {
    "England  1": "Inglaterra 1º Dv",
    "England  2": "Inglaterra 2º Dv",
    "England  3": "Inglaterra 3º Dv",
    "France  1": "Francia 1º Dv",
    "France  2": "Francia 2º Dv",
    "France  3": "Francia 3º Dv",
    "Italy  1": "Italia 1º Dv",
    "Italy  2": "Italia 2º Dv",
    "Italy  3": "Italia 3º Dv",
    "Germany  1": "Alemania 1º Dv",
    "Germany  2": "Alemania 2º Dv",
    "Germany  3": "Alemania 3º Dv",
    "Spain  1": "España 1º Dv",
    "Spain  2": "España 2º Dv",
    "Spain  3": "España 3º Dv"
}
player_stats_all_seasons['Competición'] = player_stats_all_seasons['Competición'].map(competition_translation).fillna(player_stats_all_seasons['Competición'])

# Create a dictionary for mapping
mapeo_lateralidad = {'left': 'Zurdo', 'right': 'Diestro'}

# Apply the mapping to the column 'Laterality'.
player_stats_all_seasons['Lateralidad'] = player_stats_all_seasons['Lateralidad'].map(mapeo_lateralidad)

#Creating a dictionary for position mapping
mapeo_posiciones = {
    'GK': 'POR',
    'RB': 'LD', 
    'RWB': 'LDO', 
    'RB5': 'LD5',
    'LB': 'LI', 
    'LWB': 'LIO', 
    'LB5': 'LI5',
    'CB': 'DC', 
    'LCB': 'DCI', 
    'RCB': 'DCD', 
    'RCB3': 'DCD3', 
    'LCB3': 'DCI3',
    'DMF': 'MCD', 
    'LDMF': 'MCDI', 
    'RDMF': 'MCDD',
    'LCMF': 'MI', 
    'LCMF3': 'MI3', 
    'RCMF': 'MD', 
    'RCMF3': 'MD3',
    'AMF': 'MCO',
    'LW': 'EI', 
    'LWF': 'DEI', 
    'LAMF': 'MCOI',
    'RW': 'ED', 
    'RWF': 'DED', 
    'RAMF': 'MCOD',
    'CF': 'D'
}

# Apply the mapping to the columns 'Posición Principal' and 'Posición Secundaria'.
player_stats_all_seasons['Posición Principal'] = player_stats_all_seasons['Posición Principal'].map(mapeo_posiciones)
player_stats_all_seasons['Posición Secundaria'] = player_stats_all_seasons['Posición Secundaria'].map(mapeo_posiciones)

# Remove duplicate rows based on 'ID_unico'
player_stats_all_seasons.drop_duplicates(subset='ID_unico', keep='first', inplace=True)

# Export the processed data to an Excel file
processed_file_path = '/Users/nacho/Desktop/DV7/Pyhton_Coded_Algorithem/data/Processed/player_stats_all_seasons.xlsx'
player_stats_all_seasons.to_excel(processed_file_path, index=False, engine='openpyxl')
