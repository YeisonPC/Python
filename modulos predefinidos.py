Módulos Predefinidos

Además de las funciones predefinidas, Python provee un conjunto de módulos que soportan
características muy útiles al momento de resolver problemas con Python. Un módulo contiene
definiciones de funciones y opcionalmente puede contener instrucciones para inicializar el módulo.
Un módulo es guardado como un archivo nombre_modulo.py. Dentro del módulo se puede utilizar el
nombre del módulo consultando el valor de la variable __name__.

Módulos	Utilidad

os, shutil, glob, sys	Interfaz con el sistema operativo y el sistema de archivos
re	Manejo de expresiones regulares
math	Funciones matemáticas. Es importante destacar que este módulo siempre está disponible, por lo cual para usarlo solo hay que usar import math.
urllib, smtplib, poplib, email	Módulos para funcionalidades de diversos protocolos de internet
datetime, timeit	Manejo de fecha y hora
zipfile, tarfile	Compresión de datos
doctest	Módulo para ejecución de pruebas unitarias provistas en la documentación del código
xmlrpc	Manejo de llamadas a procedimientos remotos
json, csv, xml	Manejo de formatos de intercambio de datos
gettext, locale, codecs	Internacionalización
sqlite, dbm	Manejo de bases de datos
reprlib, pprint, textwrap	Formateo de salida
threading	Soporte de multi-threading
logging	Soporte de logs (bitácoras)
