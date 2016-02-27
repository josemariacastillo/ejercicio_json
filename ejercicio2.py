# -*- coding: utf-8 -*-
#!/usr/bin/env python

#Cuenta el total de películas del festival de cine.

import json

with open("peliculas.json") as fichero:
	doc=json.load(fichero)


print len(doc["peliculas"]["pelicula"])