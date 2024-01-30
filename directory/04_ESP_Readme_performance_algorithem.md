# Descripción General
Este script se enfoca en el procesamiento de estadísticas de jugadores de fútbol, aplicando pesos específicos a métricas normalizadas para calcular las calificaciones finales de los jugadores.

# Prerrequisitos
- Python 3
- Bibliotecas Pandas y NumPy
- Biblioteca openpyxl (para manejar archivos de Excel)

# Archivo de Datos
- `player_stats_all_seasons_normalized.xlsx`: Contiene estadísticas normalizadas de jugadores de fútbol.

# Pasos Clave en el Script
1. **Carga de Datos**: Se cargan las estadísticas de jugadores de un archivo Excel.

2. **Función de Aplicación de Pesos**: Se define la función `aplicar_pesos` que toma un DataFrame y un diccionario de pesos por posición. Esta función aplica los pesos a las métricas normalizadas para calcular las calificaciones finales de los jugadores.

3. **Definición de Pesos por Posición**: Se define un diccionario con los pesos específicos para cada posición de jugador.

4. **Cálculo de Calificaciones Finales**: Se utiliza la función `aplicar_pesos` para calcular las calificaciones finales de los jugadores en el DataFrame.

5. **Reescalado de Resultados**: Se reescalan los resultados a un rango de 0 a 100 y se redondean.

6. **Limpieza de Columnas**: Se eliminan las columnas resultantes de la normalización y se mantiene solo las columnas relevantes.

7. **Exportación de Datos Procesados**: Los datos procesados se exportan a un archivo Excel para su uso posterior.

# Personalización
Este script se puede adaptar para diferentes conjuntos de datos o criterios de evaluación de jugadores, modificando los pesos y las métricas utilizadas.

# Nota sobre las Rutas de Archivos
Asegúrate de que las rutas a los archivos Excel estén configuradas correctamente para coincidir con la estructura de tu directorio.
