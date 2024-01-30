import pandas as pd
import numpy as np

# Adjust the path as per your file structure
player_stats_all_seasons = '/Users/nacho/Desktop/DV7/Pyhton_Coded_Algorithem/data/Normalized/player_stats_all_seasons_normalized.xlsx'
# Read the Excel files
player_stats_all_seasons_normalized = pd.read_excel(player_stats_all_seasons, engine='openpyxl')

def aplicar_pesos(df, pesos_por_posicion):
    """
    Applies the specific weights to the normalised metrics to calculate the players' final ratings based on their `Overall_Position
    players' final ratings based on their `Overall_Position`.

    Assumes all metrics in `df` are already normalised.

    Param df: DataFrame with player statistics already normalised.
    :param weights_by_position: Dictionary containing the weights for each metric according to the `General_Position`.
    return: DataFrame with the final ratings added.
    """
    # Initialise performance column in the DataFrame
    df['Rendimiento'] = 0.0
    
    for posicion, pesos in pesos_por_posicion.items():
        # Create a mask to filter players from the current position
        mask = df['Posición_General'] == posicion
        
        for metrica, peso in pesos.items():
            # Construct the metric column name
            columna_metrica = metrica  # Ya no añadimos '_norm' porque asumimos que todas están normalizadas
            
            if columna_metrica in df.columns:
                # Apply weight and accumulate in 'Performance'.
                df.loc[mask, 'Rendimiento'] += df.loc[mask, columna_metrica] * peso

    return df

pesos_por_posicion = {
    'Portero': {
        'Minutos_norm': 0.1,
        'Intercepciones AjPos x90_norm': 0.05,
        'Pases x90_norm': 0.075,
        'Pases Completados, %_norm': 0.075,
        'Pases Largos Completados, %_norm': 0.05,
        'Longitud Promedio De Pase_norm': 0.05,
        'Goles Prevenidos x90_norm': 0.2,
        'Paradas, %_norm': 0.125,
        'Salidas Del Portero x90_norm': 0.1,
        'Porterías A Cero_norm': 0.1,
        'Duelos Aéreos Del Portero x90_norm': 0.075,
    },
    'Central': {
        'Minutos_norm': 0.1,
        'Duelos Defensivos x90_norm': 0.1,
        'Duelos Defensivos Ganados_norm': 0.14,
        'Duelos Aéreos Ganados_norm': 0.12,
        'Pases a Último Tercio x90_norm': 0.12,
        'Intercepciones AjPos x90_norm': 0.12,
        'Xg x90_norm': 0.1,
        'Pases x90_norm': 0.07,
        'Pases Completados, %_norm': 0.04,
        'Pases Largos Completados, %_norm': 0.04,
        'Longitud Promedio De Pase_norm': 0.05,
    },
    'Lateral Derecho': {
        'Minutos_norm': 0.1,
        'Duelos Defensivos Ganados_norm': 0.15,
        'Duelos Aéreos Ganados_norm': 0.1,
        'Pases a Último Tercio x90_norm': 0.1,
        'Intercepciones AjPos x90_norm': 0.1,
        'Xg x90_norm': 0.05,
        'Centros x90_norm': 0.075,
        'Centros Completados, %_norm': 0.075,
        'xA x90_norm': 0.075,
        'Pases Clave x90_norm': 0.075,
        'Pases al espacio x90_norm': 0.025,
        'Pases al espacio Exitosos, %_norm': 0.025,
        'Carreras Progresivas x90_norm': 0.05,
    },
    'Lateral Izquierdo': {
        'Minutos_norm': 0.1,
        'Duelos Defensivos Ganados_norm': 0.15,
        'Duelos Aéreos Ganados_norm': 0.1,
        'Pases a Último Tercio x90_norm': 0.1,
        'Intercepciones AjPos x90_norm': 0.1,
        'Xg x90_norm': 0.05,
        'Centros x90_norm': 0.075,
        'Centros Completados, %_norm': 0.075,
        'xA x90_norm': 0.075,
        'Pases Clave x90_norm': 0.075,
        'Pases al espacio x90_norm': 0.025,
        'Pases al espacio Exitosos, %_norm': 0.025,
        'Carreras Progresivas x90_norm': 0.05,
    },
    'Mediocentro (6)': {
        'Minutos_norm': 0.1,
        'Duelos Defensivos x90_norm': 0.1,
        'Duelos Defensivos Ganados_norm': 0.1,
        'Duelos Aéreos Ganados_norm': 0.12,
        'Pases a Último Tercio x90_norm': 0.12,
        'Intercepciones AjPos x90_norm': 0.12,
        'Faltas x90_norm': 0.04,
        'Xg x90_norm': 0.05,
        'Pases x90_norm': 0.075,
        'Pases Completados, %_norm': 0.1,
        'xA x90_norm': 0.025,
        'Pases Clave x90_norm': 0.025,
        'Pases Completados a Último Tercio, %_norm': 0.025,
    },
    'Mediocentro (8)': {
        'Minutos_norm': 0.1,
        'Duelos Defensivos x90_norm': 0.1,
        'Duelos Defensivos Ganados_norm': 0.15,
        'Duelos Aéreos Ganados_norm': 0.125,
        'Pases a Último Tercio x90_norm': 0.075,
        'Intercepciones AjPos x90_norm': 0.1,
        'Xg x90_norm': 0.05,
        'Duelos Ofensivos x90_norm': 0.1,
        'Duelos Ofensivos Ganados_norm': 0.1,
        'Toques En El Área x90_norm': 0.025,
        'Pases Completados a Último Tercio, %_norm': 0.05,
        'xA x90_norm': 0.025,
    },
    'Mediocentro (10)': {
        'Minutos_norm': 0.1,
        'Duelos Defensivos Ganados_norm': 0.075,
        'Xg x90_norm': 0.075,
        'Regates x90_norm': 0.025,
        'Regates exitosos, %_norm': 0.05,
        'Duelos Ofensivos Ganados_norm': 0.1,
        'Pases x90_norm': 0.075,
        'Pases Completados, %_norm': 0.075,
        'xA x90_norm': 0.15,
        'Pases Clave x90_norm': 0.15,
        'Pases al espacio x90_norm': 0.05,
        'Pases al espacio Exitosos, %_norm': 0.05,
        'Diferencia xG/ Goles_norm': 0.025,
    },
    'Extremo Derecho': {
        'Minutos_norm': 0.1,
        'Xg x90_norm': 0.15,
        'Regates x90_norm': 0.05,
        'Regates exitosos, %_norm': 0.05,
        'Toques En El Área x90_norm': 0.05,
        'Carreras Progresivas x90_norm': 0.05,
        'xA x90_norm': 0.15,
        'Aceleraciones x90_norm': 0.075,
        'Pases Clave x90_norm': 0.1,
        'Pases Completados a Último Tercio, %_norm': 0.1,
        'Pases al espacio x90_norm': 0.05,
        'Pases al espacio Exitosos, %_norm': 0.025,
        'Diferencia xG/ Goles_norm': 0.05,
    },
    'Extremo Izquierdo': {
        'Minutos_norm': 0.1,
        'Xg x90_norm': 0.15,
        'Regates x90_norm': 0.05,
        'Regates exitosos, %_norm': 0.05,
        'Toques En El Área x90_norm': 0.05,
        'Carreras Progresivas x90_norm': 0.05,
        'xA x90_norm': 0.15,
        'Aceleraciones x90_norm': 0.075,
        'Pases Clave x90_norm': 0.1,
        'Pases Completados a Último Tercio, %_norm': 0.1,
        'Pases al espacio x90_norm': 0.05,
        'Pases al espacio Exitosos, %_norm': 0.025,
        'Diferencia xG/ Goles_norm': 0.05,
    },
    'Delantero': {
        'Minutos_norm': 0.1,
        'Duelos Aéreos Ganados_norm': 0.05,
        'Intercepciones AjPos x90_norm': 0.05,
        'Faltas x90_norm': 0.05,
        'Xg x90_norm': 0.15,
        'Regates x90_norm': 0.01,
        'Regates exitosos, %_norm': 0.04,
        'Duelos Ofensivos Ganados_norm': 0.1,
        'Toques En El Área x90_norm': 0.1,
        'xA x90_norm': 0.1,
        'Aceleraciones x90_norm': 0.05,
        'Pases Clave x90_norm': 0.05,
        'Diferencia xG/ Goles_norm': 0.15,
    }
}
player_stats_all_seasons_final = aplicar_pesos(player_stats_all_seasons_normalized, pesos_por_posicion)

# Function for rescaling results
def reescalar_a_100(grupo):
    minimo = grupo.min()
    maximo = grupo.max()
    # Avoid division by zero in case all values in the group are equal.
    if maximo == minimo:
        return grupo
    else:
        return (grupo - minimo) / (maximo - minimo) * 100    
# Rescale to 100 and then round off
player_stats_all_seasons_final['Rendimiento_Reescalado'] = player_stats_all_seasons_final.groupby(['Posición_General', 'Temporada', 'Competición'])['Rendimiento'].transform(reescalar_a_100).round()

#Eliminate the colunae resulting from standardisation
# Select columns that do not end in "_norm" 
columnas_a_mantener = [col for col in player_stats_all_seasons_final.columns if not col.endswith('_norm')]
# Reassign the DataFrame only to those columns
player_stats_all_seasons_final = player_stats_all_seasons_final[columnas_a_mantener]

# Export the processed data to an Excel file
processed_file_path = '/Users/nacho/Desktop/DV7/Pyhton_Coded_Algorithem/data/Final/player_stats_all_seasons_final.xlsx'
player_stats_all_seasons_final.to_excel(processed_file_path, index=False, engine='openp
