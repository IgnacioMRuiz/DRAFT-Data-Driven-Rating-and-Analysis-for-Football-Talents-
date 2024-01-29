# Resumen
Este proyecto se enfoca en normalizar las estadísticas de jugadores de diversas temporadas deportivas. El objetivo principal es estandarizar estas estadísticas en un rango de 0-100, haciendo las comparaciones entre diferentes temporadas y condiciones más directas y significativas.

# Prerrequisitos
- Python 3
- Biblioteca Pandas
- Biblioteca NumPy
- Biblioteca openpyxl para manejar archivos de Excel

# Descripción del Archivo
player_stats_all_seasons.xlsx: Archivo Excel que contiene datos crudos de estadísticas de jugadores a lo largo de diferentes temporadas.

# Detalles de Implementación

## Carga de Datos
El script comienza cargando los datos de estadísticas de jugadores desde un archivo Excel usando Pandas. Ajusta la ruta al archivo Excel según la estructura de tu directorio.

## Función de Normalización
normalizar_estadisticas_por_grupo es la función principal utilizada para normalizar las estadísticas. Toma un DataFrame y una lista de nombres de columnas para normalizar.

- Parámetros:
  - df: DataFrame que contiene estadísticas de jugadores.
  - columnas: Lista de columnas a normalizar.

- Funcionalidad:
  - La función calcula el umbral de minutos para la temporada 2023 y prepara un DataFrame para las columnas normalizadas.
  - Luego itera sobre las columnas especificadas, agrupando los datos por posición general, temporada y competición.
  - Para cada grupo, normaliza los datos al rango de 0-100 basado en puntuaciones z.

## Proceso de Normalización
Las columnas a normalizar se enumeran y se introducen en la función junto con el DataFrame. El DataFrame resultante incluye tanto los datos originales como los normalizados.

## Exportación de Datos
Los datos procesados se exportan luego a un archivo Excel para su posterior análisis o uso.

# Nota sobre los Nombres de las Funciones
Los nombres de las funciones están en español debido al contexto de aplicación del proyecto. Mantener la consistencia en las convenciones de nomenclatura a lo largo de un proyecto es esencial. Estos nombres pueden cambiar siempre y cuando los cambios sean ordenados y consistentes en todo el proyecto. Se proporcionan pasos específicos para traducir valores o nombres de variables si es necesario; si no se requiere, este paso puede omitirse.
