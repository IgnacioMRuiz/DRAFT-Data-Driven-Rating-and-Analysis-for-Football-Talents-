# Algoritmo DRAFT (Data-Driven Rating and Analysis for Football Talents)

El proyecto Football Analytics Suite está diseñado para recopilar, procesar, normalizar y analizar datos de jugadores de fútbol. Utilizando el algoritmo DRAFT, el proyecto evalúa el rendimiento y valor de los jugadores en el campo.

## 1. Extracción de datos (`01_data_extraction_2018_2022.R / 01_data_extraction_2023.R`)
### Objetivo
Recopilar datos detallados de jugadores de fútbol.

### Funcionalidades Clave
- Conexión con API para obtener estadísticas de jugadores.
- Filtrado y selección de ligas y temporadas relevantes.
- Almacenamiento de datos en formato Excel.

### Bibliotecas de R Utilizadas
- `rjson`
- `readxl`
- `dplyr`
- `stringr`
- `writexl`

### Proceso
- Obtención del token de acceso para la API.
- Extracción de estadísticas de jugadores de diferentes ligas.
- Limpieza inicial y formateo de los datos.
- Exportación de los datos a un archivo Excel.

---

## 2. Limpieza de datos (`02_data_cleaning.ipynb`)
### Objetivo
Preparar los datos para el análisis.

### Funcionalidades Clave
- Lectura de los datos desde archivos Excel.
- Selección y renombrado de columnas específicas.
- Limpieza de valores nulos y transformaciones necesarias.

### Bibliotecas de Python Utilizadas
- `pandas`

### Proceso
- Carga de datos de Excel usando `pandas`.
- Renombrado de columnas para mejorar la claridad.
- Tratamiento de valores faltantes o incorrectos.
- Consolidación de datos de diferentes temporadas.

---

## 3. Normalización de datos (`03_data_normalization.ipynb`)
### Objetivo
Normalizar las estadísticas de los jugadores.

### Funcionalidades Clave
- Aplicación de técnicas de normalización a las métricas de los jugadores.
- Asegurar comparabilidad entre jugadores de diferentes ligas y temporadas.

### Bibliotecas de Python Utilizadas
- `pandas`
- `numpy`

### Proceso
- Cálculo de umbrales y criterios para la normalización.
- Normalización de estadísticas individuales a una escala común.
- Combinación de los datos normalizados con el conjunto de datos original.

---

## 4. Performance Analysis (`04_performance_algorithem.ipynb`)
### Objetivo
Evaluar el rendimiento de los jugadores utilizando métricas ponderadas.

### Funcionalidades Clave
- Aplicación de un conjunto de pesos a las estadísticas normalizadas.
- Cálculo de una puntuación de rendimiento global para cada jugador.

### Bibliotecas de Python Utilizadas
- `pandas`
- `numpy`

### Proceso
- Definición de pesos para diferentes posiciones y métricas.
- Cálculo del rendimiento basado en los pesos asignados.
- Reescalamiento de las puntuaciones para comparación uniforme.
- Exportación de los datos finales para su uso en análisis o visualizaciones.

---

## Consideraciones Adicionales
- **Integración de Datos**: Asegurar un flujo de datos sin problemas entre las etapas.
- **Actualización y Mantenimiento**: Establecer protocolos para actualizaciones y ajustes.
- **Visualización y Reportes**: Desarrollar herramientas para visualizar y reportar los hallazgos.

---

### Insipiración
Liam Henshaw - [Henshaw Analysis player ratings — methodology, discussion & examples](https://henshawanalysis.medium.com/henshaw-analysis-player-ratings-methodology-discussion-examples-555351393b9a)
Andy Watson - [AW Role Scouting System: The Launch](https://andywatsonsport.wordpress.com/2022/02/02/aw-role-scouting-system-the-launch/)
Rubén Sánchez-López, Ibon Echeazarra y Julen Castellano Paulis - [Validation of an instrument to qualify football competence via WyScout](https://revista-apunts.com/en/validation-of-an-instrument-to-qualify-football-competence-via-wyscout/)
Anterior trabajo propio - [Proceso de scouting y confección de plantilla R.C.D Espanyol para la temporada 23/24](https://www.linkedin.com/posts/ignaciomruiz_scouting-y-confecci%C3%B3n-de-plantilla-rcd-activity-7091011895117111296-AR6g?utm_source=share&utm_medium=member_desktop)

Este proyecto ofrece insights valiosos y detallados sobre el rendimiento de los jugadores en el fútbol, apoyando en la toma de decisiones en scouting, gestión de equipos y análisis deportivo.
