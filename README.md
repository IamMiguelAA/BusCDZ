# BusCDZ

Bot de twitter para obtener el tiempo restante para la llegada de un autobús determinado en Cádiz.


### Autores

* **Miguel Ángel Álvarez García** - [GitHub](https://github.com/IamMiguelAA)
* **Ana Gómez González** - [GitHub](https://github.com/angoglez)


### Funcionamiento

Debe instalar antes de iniciar el proceso el programa Anypoint Platform de MuleSoft.

1.Importe en la aplicación una vez iniciada el proyecto:

2. Edite el archivo buscdz.xml:
```
<twitter:config name="Twitter__Configuration" accessKey="" accessSecret="" consumerKey="" consumerSecret="" doc:name="Twitter: Configuration"/>
```
Pueden existir otros apartados en ese mismo archivo que deben ser editados.

3. Ejecutar la aplicación mediante Anypoint.
