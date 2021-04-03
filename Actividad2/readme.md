# Actividad Integradora 2
## Equipo 1
- David Alonso Cantú Martínez   A00822455

- Jesús Omar Cuenca Espino      A01378844

- Nadia Corina García Orozco    A01242428

- Luis Cossío Ramírez           A011876634

- Fernando Carrillo Mora        A01194204

## Instrucciones

- Tener instalado paqueterias descritas en el *requirements.txt* del repo
- Tener instalado Chrome
- Tener en el mismo directorio un archivo *pathFile.txt* que en la primera linea contenga el PATH que lleva al WebDriver de Selenium (Chrome)
- El programa se corre de la siguiente forma:

> python3 imgScrapperUnsplash.py < Keyword to search > < Number of images to Download ? Defaults to 100 >

---

## ¿Qué hace este proyecto? / What does this project do?
Explorando la técnica de **Web Data Scraping** con la ayuda de la herramienta *Selenium* para recopilar imagenes de una base de datos en línea, se solicita al usuario un término de búsqueda, para después efectuar una consulta en Unsplash. El programa descarga las imágenes arrojadas por la base de datos, donde guarda el 80% de las mismas en la carpeta 
```
./train/<término_de_búsqueda>
``` 
y el 20% restante en la carpeta 
```
./test/<término_de_búsqueda>. 
```
Por ejemplo,  si el usuario ingresa el término de búsqueda “dog”, se deben descargar el 80% de las imágenes que arrojó Unsplash en *./train/dog* y el otro 20% en *./test/dog*.

Explroing the **Web Data Scraping Tecnique** with *Selenium* as our helping tool to gather images from an online data base, the user is prompted to type a search term for the program to then perform the query with the keyword on Unsplash. The program then downloads the images returned from the data base saving 80% of the results on the folder
```
./train/<search_term>
``` 
and the remaining 20% on 
```
./test/<search term>. 
```

For example, if the user were to type *dog* as a search term, 80% of the images returned from Unsplash would be saved on *./train/dog* and the other 20% on *./test/dog*.

## ¿Por qué es útil este proyecto? / Why is this project useful?
Este proyecto es util para poder empezar a crear nuestro set de datos para aplicaciones de Visión por Computadora que esperamos continuar aprendiendo a lo largo del curso, haciendo uso de recursos gratuitos en la web.

This project is useful for us to begin creating a base data set for future Computer Vision applications we hope to continue learning throughout the next weeks in the course, using free online resources.

## ¿Cómo inicializar el proyecto? / How to get started with this project?
Asegurese de contar con los paquetes de **requests, selenium** y **fileManager** instalados en su ambiente de desarrollo de Python.

Todas las dependencias vienen adjuntas en el **requirements.txt**.

Recomendamos tener un *venv* para instalar las dependencias de forma independiente.


Make sure to have **requests, selenium** and **fileManager** packages installed in your Python environment.

All dependencies are attached in the **requirements.txt**.

We do recommend to create a *venv* for this particular proyect in order not to mix dependencies.

`$ pip install -r requirements.txt`

`$ jupiter notebook`

---

### Recursos / Resources
- [Webscraping Tutorial](https://realpython.com/beautiful-soup-web-scraper-python/)

