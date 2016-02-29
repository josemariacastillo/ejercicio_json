# -*- coding: utf-8 -*-
#!/usr/bin/env python

#Programa que lea por teclado la nacionalidad de la película y cuente las películas hechas en ese país.

import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

with open("peliculas.json") as fichero:
	doc=json.load(fichero)
nac=unicode(raw_input("Introduzca nacionalidad: "),'utf-8')

encontrado=False
contador=0

for p in doc["peliculas"]["pelicula"]:
	if nac==p["nacionalidad"]:
		if p["titulo"]:
			encontrado=True
		if encontrado==True:
			contador=contador+1
print contador