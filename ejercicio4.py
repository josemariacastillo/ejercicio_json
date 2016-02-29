# -*- coding: utf-8 -*-
#!/usr/bin/env python

#Programa que lea por teclado el identificador de la película y muestre el titulo y nacionalidad

import json

with open("peliculas.json") as fichero:
	doc=json.load(fichero)

iden=int(raw_input("Introduzca el identificador de la pelicula: "))

for p in doc["peliculas"]["pelicula"]:
	if iden==p["identificador"]:
		print p["titulo"]
		print p["nacionalidad"]