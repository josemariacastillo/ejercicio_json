# -*- coding: utf-8 -*-
#!/usr/bin/env python

#Listar el titulo de las películas y la productora

import json

with open("peliculas.json") as fichero:
	doc=json.load(fichero)

for l in doc["peliculas"]["pelicula"]:
	print "\nTitulo: ",l["titulo"]
	print "Sinopsis: \n",l["sinopsis"]