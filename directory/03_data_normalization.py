import pandas as pd
import numpy as np

# Adjust the path as per your file structure
player_stats_all_seasons = '/Users/nacho/Desktop/DV7/Pyhton_Coded_Algorithem/data/Processed/player_stats_all_seasons.xlsx'

# Read the Excel files
player_stats_all_seasons = pd.read_excel(player_stats_all_seasons, engine='openpyxl')

def normalizar_estadisticas_por_grupo(df, columnas):
    """
    Normalize player statistics by applying season filters and
    normalizing values to the 0-100 range.
    """
    # Calculate the minute threshold for the 2023 season
    umbral_2023 = df[df['Temporada'] == 2023]['Minutos'].max() * 0.1

    # Prepare a DataFrame for normalized columns
    df_norm = pd.DataFrame(index=df.index)

    # Iterate over columns to normalize
    for columna in columnas:
        df_norm[columna + '_norm'] = np.nan  # Initialize with NaN

        # Group by 'Posición_General', 'Temporada', and 'Competición'
        for (posicion, temporada, competicion), group_df in df.groupby(['Posición_General', 'Temporada', 'Competición']):
            # Apply filter conditions from the first function
            if temporada in [2018, 2019, 2020, 2021, 2022]:
                indices = group_df[group_df['Minutos'] >= 400].index
            elif temporada == 2023:
                indices = group_df[group_df['Minutos'] >= umbral_2023].index
            else:
                continue  # No normalization applied for other seasons

            # Calculate z-scores and scale to the range 0-100 for selected indices
            if not indices.empty:
                mean = df.loc[indices, columna].mean()
                std = df.loc[indices, columna].std()
                if std > 0:
                    z_scores = (df.loc[indices, columna] - mean) / std
                    min_z = z_scores.min()
                    max_z = z_scores.max()
                    scaled = (z_scores - min_z) / (max_z - min_z) * 100
                    df_norm.loc[indices, columna + '_norm'] = scaled
                else:
                    df_norm.loc[indices, columna + '_norm'] = 50  # Neutral value if no variation

    # Combine the original DataFrame with new normalized columns
    df_final = pd.concat([df, df_norm], axis=1)

    return df_final

columnas_a_normalizar = [
    "Minutos", "Faltas x90","Tarjetas Amarillas", "Tarjetas Amarillas x90",
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

# Call the function with the DataFrame and specified columns
df_normalized = normalizar_estadisticas_por_grupo(player_stats_all_seasons, columnas_a_normalizar)

# Export the processed data to an Excel file
processed_file_path = '/Users/nacho/Desktop/DV7/Pyhton_Coded_Algorithem/data/Normalized/player_stats_all_seasons_normalized.xlsx'
df_normalized.to_excel(processed_file_path, index=False, engine='openpyxl')
