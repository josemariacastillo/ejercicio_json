# -*- coding: utf-8 -*-
#!/usr/bin/env python

#Programa que lea por teclado una cadena y muestre la nacionalidad de la película por la que empieza esa cadena y la URL

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import json

with open("peliculas.json") as fichero:
	doc=json.load(fichero)

cad=unicode(raw_input("Introduzca una cadena texto: "),'utf-8')
encotrado=False
try:
	for p in doc["peliculas"]["pelicula"]:
		if p["nacionalidad"].startswith(cad):
			print "\nNacionalidad: ",p["nacionalidad"]
			print "URL: ",p["url"]
			encotrado=True
			
except AttributeError:
	print "" #Quitar error molesto de atributo al finalizar la búsqueda

   

if encotrado==False:
	print "La cadena introducida no coincide con el comienzo de ninguna nacionalidad."
