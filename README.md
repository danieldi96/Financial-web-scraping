# Práctica 1. Información bursátil de una compañía cotizada en el IBEX35

## Descripción
Esta es la primera práctica de la asignatura _Tipología y ciclo de vida de los datos_, impartida en el Máster de Ciencia de Datos de la Universitat Oberta de Catalunya. Se emplean técnicas de _Web Scraping_ mediante el lenguaje de programción _Python_, además de sus librerías _BeautifulSoup_ y _lxml_. La información se ha extraído de _www.bolsamadrid.es_ y el conjunto de datos hace referencia a cualquier empresa del IBEX35.


## Miembros del equipo

Esta práctica ha sido realizada por **Daniel Díaz Fernández**

## Parámetros

* **src/main.py**: En este archivo debemos definir la variable global _Company_ que corresponde al nombre de la compañía de la que se quiere recopilar los datos.

## Ficheros del código fuente

* **src/main.py**: Código principal del programa.
* **src/scraper.py**: Contiene el código implementado para la recolección y extracción de los datos. Recoge el recurso HTML de la página web y extrae su información para guardarla en un archivo CSV.
* **doc/[P1] Daniel Díaz**: Documentación de la práctica.
* **results/<nombre_escogido>.csv**: Archivo con los datos obtenidos de la compañía obtenida en formato CSV.
* **results/stocks_<nombre_escogido>.csv**: Archivo con los datos históricos obtenidos de la compañía obtenida en formato CSV.

## Zenodo [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4265402.svg)](https://doi.org/10.5281/zenodo.4265402)
El link obtenido para el acceso a los CSV publicados en Zenodo es: https://zenodo.org/record/4265402

## Recursos

1. Subirats, L. Calvo, _Web Scraping_, UOC (2018).
2. Masip, D., _El lenguaje Python_, UOC.
3. _Licencias de uso asociadas a las iniciativas de datos abiertos en España_. Ver en: https://datos.gob.es/es/noticia/licencias-de-uso-asociadas-las-iniciativas-de-datos-abiertos-en-espana
