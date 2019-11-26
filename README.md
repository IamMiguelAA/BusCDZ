# BusCDZ

Bot de twitter para obtener el tiempo restante para la llegada de un autobús determinado en Cádiz.


### Autores

* **Miguel Ángel Álvarez García** - [GitHub](https://github.com/IamMiguelAA)
* **Ana Gómez González** - [GitHub](https://github.com/angoglez)

### Tecnologías utilizadas

* [Flask](http://flask.pocoo.org/) - Microframework para aplicaciones web en Python
* [Celery](http://www.celeryproject.org/) - Gestor de tareas asíncronas con RabbitMQ como broker
* [Tweepy](http://www.tweepy.org/) - Librería para el manejo de Twitter en Python
* [Dropbox API](https://www.dropbox.com/developers/documentation/python#overview) - API propia de Dropbox para Python
* [MeaningCloud API](https://www.meaningcloud.com/es/) - API para análisis de sentimiento
* [Pandas](https://pandas.pydata.org/) - Librería para el análisis de datos en Python
* [PlotLy API](https://plot.ly/python/) - API para la visualización de los datos


### Funcionamiento

Debe instalar antes de iniciar el proceso el programa Anypoint Platform de MuleSoft.

1.Importe en la aplicación una vez iniciada el proyecto:

2.Edite el archivo buscdz.xml:
```
<twitter:config name="Twitter__Configuration" accessKey="" accessSecret="" consumerKey="" consumerSecret="" doc:name="Twitter: Configuration"/>
```
  Pueden existir otros apartados en ese mismo archivo que deben ser editados.

3.Ejecutar la aplicación mediante Anypoint.
