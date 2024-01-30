# Algoritmo DRAFT (Data-Driven Rating and Analysis for Football Talents)

El proyecto Football Analytics Suite está diseñado para recopilar, procesar, normalizar y analizar datos de jugadores de fútbol. Utilizando el algoritmo DRAFT, el proyecto evalúa el rendimiento y valor de los jugadores en el campo.

# Índice

- [Introducción](#introducción)
- [Explicación del Algoritmo DRAFT](#explicación-del-algoritmo-draft)
  - [Uso del Algoritmo](#uso-del-algoritmo)
  - [Interpretación de Resultados](#interpretación-de-resultados)
  - [Uso Práctico](#uso-práctico)
  - [Consideraciones Finales](#consideraciones-finales)
- [Discusión sobre el Algoritmo DRAFT](#discusión-sobre-el-algoritmo-draft)
  - [Desafíos y Futuro](#desafíos-y-futuro)
- [Proceso Técnico](#proceso-técnico)
  - [Extracción de Datos](#extracción-de-datos)
  - [Limpieza de Datos](#limpieza-de-datos)
  - [Normalización de Datos](#normalización-de-datos)
  - [Análisis de Rendimiento](#análisis-de-rendimiento)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Inspiración y Referencias](#inspiración-y-referencias)

---

## Explicación Detallada del Algoritmo DRAFT

El algoritmo DRAFT (Data-Driven Rating and Analysis for Football Talents) es un avanzado sistema de análisis de jugadores de fútbol. Su objetivo es evaluar integralmente el rendimiento de los jugadores a través de una combinación de estadísticas avanzadas y métodos de normalización.

### Uso del Algoritmo

#### Evaluación Multidimensional
DRAFT evalúa múltiples aspectos del juego, incluyendo habilidades ofensivas, defensivas, juego aéreo y contribuciones tácticas.

#### Basado en Datos
Las evaluaciones se fundamentan en datos recopilados, limpiados y normalizados de fuentes confiables, asegurando una evaluación objetiva y basada en el rendimiento real del jugador.

### Interpretación de Resultados

#### Escala de 0 a 100
Cada jugador recibe una puntuación en una escala de 0 a 100, donde un puntaje más alto indica un rendimiento superior.

#### Divisiones por Temporadas, Posiciones y Ligas
Los jugadores son evaluados dentro de su contexto específico: por temporadas, posiciones y ligas. Esto permite ver la evolución del rendimiento, reconocer diferentes requisitos por posición y comparar dentro del mismo nivel competitivo.

### Uso Práctico

#### Scouting y Análisis de Talentos
DRAFT es esencial para identificar talentos destacados o subestimados en diferentes ligas y posiciones.

#### Evaluación Estratégica
Permite a directores técnicos y estrategas evaluar fortalezas y debilidades tanto propias como de oponentes.

#### Desarrollo de Jugadores
Facilita a los entrenadores identificar áreas específicas de mejora para sus jugadores.

#### Comparaciones y Benchmarks
Facilita la realización de benchmarks entre jugadores de diferentes ligas o temporadas.

### Consideraciones Finales

DRAFT es una herramienta dinámica y adaptable, capaz de ajustarse y evolucionar con nuevas informaciones y métricas.

### Conclusión

DRAFT ofrece una visión detallada y multifacética del rendimiento de los jugadores, siendo una herramienta indispensable para profesionales del fútbol en todo el mundo.

---

## Discusión sobre el Algoritmo DRAFT

### Los Desafíos y el Futuro de DRAFT

Es importante ser transparente acerca de los posibles problemas y limitaciones del modelo DRAFT, así como de su salida. A continuación, se discuten algunos de estos desafíos, así como las posibles mejoras y desarrollos futuros.

#### Desafíos Actuales

- **Automatización y Actualización de Datos**: Si bien el proceso es ahora automatizado, sigue requiriendo tiempo para recorrer y actualizar los datos en la plataforma Wyscout.
- **Interpretación de las Puntuaciones**: Las puntuaciones, después de ser manipuladas y ponderadas, sirven principalmente para clasificar a los jugadores en sus roles.
- **Comparabilidad de las Puntuaciones**: Las clasificaciones se realizan dentro de un conjunto de datos específico, lo que puede dificultar la comparación entre diferentes conjuntos de datos.
- **Datos Defensivos**: La clasificación de atributos defensivos usando solo datos de eventos es compleja y puede no ser tan confiable como los datos de atributos ofensivos.
- **Atributos Físicos**: Actualmente no es posible clasificar o evaluar atributos físicos.
- **Diferenciación de Roles**: Algunos roles pueden ser difíciles de diferenciar si las diferencias clave no se pueden medir con los datos disponibles.
- **Calidad de los Datos**: La eficacia del modelo DRAFT depende de la calidad de los datos de entrada.

#### Desarrollos Futuros

- **Uso de Promedios de Atributos Posicionales**: Para comparar el rendimiento de los jugadores de manera más confiable y proporcionar un contrapunto a las puntuaciones relacionales.
- **Mejora de la Presentación de Datos**: Trabajar en la interpretación y visualización de los datos para que sean comprensibles para el usuario final.
- **Integración de Scouting Visual**: Desarrollar y combinar formularios de scouting visual con el sistema basado en datos para una visión holística del jugador.
- **Ajuste Fácil de las Puntuaciones Finales**: Permitir que los usuarios finales apliquen diferentes ponderaciones, como aumentar la ponderación de la defensa 1v1 para los laterales.
- **Inclusión de Métricas Avanzadas**: Como la amenaza esperada (xT) para agregar más contexto a algunos atributos clave.
- **Uso de Datos de Posesión y Tilt de Campo**: Para reducir el sesgo del equipo en los datos de los jugadores.
- **Uso de Calificaciones de Ligas y Clubes**: Para comparar de manera más efectiva a través de ligas.

#### Pensamientos Finales y Retroalimentación

Si tienes comentarios o sugerencias sobre el modelo DRAFT, ya sean positivos o negativos, siempre son bienvenidos. Puedes contactarme a través de correo electrónico en nachomolinaruiz@gmail.com.

---

## Proceso Técnico
### 1. Extracción de datos (`01_data_extraction_2018_2022.R / 01_data_extraction_2023.R`)
#### Objetivo
Recopilar datos detallados de jugadores de fútbol.

#### Funcionalidades Clave
- Conexión con API para obtener estadísticas de jugadores.
- Filtrado y selección de ligas y temporadas relevantes.
- Almacenamiento de datos en formato Excel.

#### Bibliotecas de R Utilizadas
- `rjson`
- `readxl`
- `dplyr`
- `stringr`
- `writexl`

#### Proceso
- Obtención del token de acceso para la API.
- Extracción de estadísticas de jugadores de diferentes ligas.
- Limpieza inicial y formateo de los datos.
- Exportación de los datos a un archivo Excel.

### 2. Limpieza de datos (`02_data_cleaning.ipynb`)
### Objetivo
Preparar los datos para el análisis.

#### Funcionalidades Clave
- Lectura de los datos desde archivos Excel.
- Selección y renombrado de columnas específicas.
- Limpieza de valores nulos y transformaciones necesarias.

#### Bibliotecas de Python Utilizadas
- `pandas`

#### Proceso
- Carga de datos de Excel usando `pandas`.
- Renombrado de columnas para mejorar la claridad.
- Tratamiento de valores faltantes o incorrectos.
- Consolidación de datos de diferentes temporadas.

### 3. Normalización de datos (`03_data_normalization.ipynb`)
#### Objetivo
Normalizar las estadísticas de los jugadores.

#### Funcionalidades Clave
- Aplicación de técnicas de normalización a las métricas de los jugadores.
- Asegurar comparabilidad entre jugadores de diferentes ligas y temporadas.

#### Bibliotecas de Python Utilizadas
- `pandas`
- `numpy`

#### Proceso
- Cálculo de umbrales y criterios para la normalización.
- Normalización de estadísticas individuales a una escala común.
- Combinación de los datos normalizados con el conjunto de datos original.

### 4. Performance Analysis (`04_performance_algorithem.ipynb`)
#### Objetivo
Evaluar el rendimiento de los jugadores utilizando métricas ponderadas.

#### Funcionalidades Clave
- Aplicación de un conjunto de pesos a las estadísticas normalizadas.
- Cálculo de una puntuación de rendimiento global para cada jugador.

#### Bibliotecas de Python Utilizadas
- `pandas`
- `numpy`

#### Proceso
- Definición de pesos para diferentes posiciones y métricas.
- Cálculo del rendimiento basado en los pesos asignados.
- Reescalamiento de las puntuaciones para comparación uniforme.
- Exportación de los datos finales para su uso en análisis o visualizaciones.

### Consideraciones Adicionales
- **Integración de Datos**: Asegurar un flujo de datos sin problemas entre las etapas.
- **Actualización y Mantenimiento**: Establecer protocolos para actualizaciones y ajustes.
- **Visualización y Reportes**: Desarrollar herramientas para visualizar y reportar los hallazgos.

## Estructura
Este proyecto incluye varias carpetas y archivos organizados para facilitar el desarrollo y el análisis:

## Directorio de Datos
- `data/`: Carpeta principal para todos los conjuntos de datos.
  - `raw/`: Almacena los datos sin procesar obtenidos de las fuentes.
  - `cleaned/`: Contiene los datos que han sido limpiados y preprocesados.
  - `normalized/`: Datos después de aplicar procesos de normalización.
  - `final/`: Datos finales procesados y listos para el análisis.

## Directorio de Scripts y Notebooks
- `directory/`: Incluye scripts y notebooks del proyecto.
  - `R/`: Scripts de R para la extracción de datos.
    - `01_data_extraction_2018_2022.R`: Extracción de datos de las temporadas 2018 a 2022.
    - `01_data_extraction_2023.R`: Extracción de datos de la temporada 2023.
  - `Python/`: Notebooks de Python para limpieza, normalización y análisis.
    - `02_data_cleaning.ipynb`: Notebook para limpieza de datos.
    - `03_data_normalization.ipynb`: Notebook para normalización de datos.
    - `04_performance_analysis.ipynb`: Notebook para análisis de rendimiento.
  - `READMES/`: READMEs para cada script o notebook.

## Documentación
- `docs/`: Documentación del proyecto, notas adicionales y materiales de referencia.

## README Principal
- `README.md`: Descripción general y detallada del proyecto.

---

## Insipiración
Liam Henshaw - [Henshaw Analysis player ratings — methodology, discussion & examples](https://henshawanalysis.medium.com/henshaw-analysis-player-ratings-methodology-discussion-examples-555351393b9a)

Andy Watson - [AW Role Scouting System: The Launch](https://andywatsonsport.wordpress.com/2022/02/02/aw-role-scouting-system-the-launch/)

Rubén Sánchez-López, Ibon Echeazarra y Julen Castellano Paulis - [Validation of an instrument to qualify football competence via WyScout](https://revista-apunts.com/en/validation-of-an-instrument-to-qualify-football-competence-via-wyscout/)

Anterior trabajo propio - [Proceso de scouting y confección de plantilla R.C.D Espanyol para la temporada 23/24](https://www.linkedin.com/posts/ignaciomruiz_scouting-y-confecci%C3%B3n-de-plantilla-rcd-activity-7091011895117111296-AR6g?utm_source=share&utm_medium=member_desktop)
