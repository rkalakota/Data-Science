
# TFM: Estimación de parámetros hemodinámicos en Aneurismas abdominales mediante técnicas de Machine Learning.

# What? 
El objetivo de este proyecto es optimizar el cálculo de parámetros hemodinámicos en aneurismas abdominales, para determinar la diferencia de presión en la orta y así determinar la gravedad del paciente.
 
# Why?
En la actualidad estos parámetros hemodinámicos son costosos de calcular computacionalmente hablando, ya que requieren de técnicas de segmentación / mallado y de un motor de simulación para la física de fluidos.

Ese proceso puede llegar a tardar más de 5 horas dependiendo de la "calidad" del mallado.

# How?
La idea es que mediante características geométricas del aneurismas, que se pueden extraer fácilmente de la prueba realizada al paciente, no sea necesaria hacer un proceso de simulación costoso sino encontrar un modelo matemático que de una respuesta mas inmediata.

_**Imprescidible:**_ empezar la lectura del TFM por la 0_Presentacion para una completa compresión del TFM.

# Structure of repository
Este repositorio ha sido creado para el proyecto final de master (TFM) y está estructurado en 3 carpetas ordenadas de forma numérica.

* **0_Presentation:** Incluye la propuesta de proyecto presentada para la realización del master defendida el 15 de Junio.

* **1_DataAdquistion:** Carpeta donde se encuentran todos los datos en RAW, de las simulaciones generadas y donde se encuentra el parser para crear el CSV de trabajo.

* **2_Analysis:** Carpeta donde se encentran diferente _jupyter notebook_ con el análisis de los datos y los diferentes modelos usados.


## Getting Started

1. El primer paso a realizar es descargar el repositorio a nuestra maquina local. Esto se realiza simplemente escribiendo en un navegador la siguiente dirección y automáticamente se descargará un ZIP con todo el repositorio.
 
  ```
  https://github.com/rkalakota/Data-Science/zipball/master/
  ```

2. Generar el Dataset de trabajo a partir del conjunto de archivos de simulación.Previamente se necesita que la maquina disponga de PYTHON.Se abre una consola de ANACONDA PROMPT y se busca donde se ha descargado el repositorio para buscar la carpeta 1_DataAdquistion y ejecutar el SCRIPT de PYTHON.

  ```
  cd 1_DataAdquistion
  python 1.2_GetCSVDataFromSimulation.py
  ```
  Esto genera un archivo CSV llamado salida.csv que contiene los datos para trabajar.
  
  _**Atención!**_ Si hubiera algún problema con el PATH a la hora de ejecutar el SCRIPT, ya que todas las pruebas se han realizado con una maquina Windows en la línea 81 se puede modificar la línea que contiene la carpeta, donde están todas las carpetas de simulación.

3. Con el CSV de datos ya se puden ejecutar los Jupyter Notebook de análisis de datos que se encuentran en la carpeta 2_Analysis

  ```
  2_Analysis \ 0.Analisis_Exploratorio_Datos.ipynb
  2_Analysis \ 1.Modelo.ipynb
  ```
  
## Built With
* [GID] - (https://www.gidhome.com/) - The personal pre and post processor.
* [Kratos] - (https://github.com/KratosMultiphysics/Kratos) - Kratos Multi-Physics.
* [Anaconda] - (https://anaconda.org/anaconda/python) - Una distribución de PYTHON muy completa que incluye Juypyter Notebook.

## Author:
Sergio Valero López

Android developer in Centre Internacional de Mètodes Numèrics a l'Enginyeria (CIMNE).

rkalakota@gmail.com
