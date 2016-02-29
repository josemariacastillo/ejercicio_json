# -*- coding: utf-8 -*-
#!/usr/bin/env python

#Programa que lea por teclado una cadena y muestre la nacionalidad de la película por la que empieza es cadena y la URL

import json

with open("peliculas.json") as fichero:
	doc=json.load(fichero)

cad=raw_input("Introduzca una cadena texto: ")

for p in doc["peliculas"]["pelicula"]:
	if p["nacionalidad"].startswith(cad):
		print p["url"]
