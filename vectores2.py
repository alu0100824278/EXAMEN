#!/usr/bin/python
#! encoding: UTF-8

dimensiones = (2, 3, 4, 5)

for dim in dimensiones:
  print 'Evaluacion para la suma de vectores de dimension %d' % dim
  v1 = [0]*dim
  v2 = [0]*dim
  v3 = [0]*dim

  for i in range (dim):
    v1[i] = int(raw_input("Coordenada %d del vector 1: " % i))

  for i in range (dim):
    v2[i] = int(raw_input("Coordenada %d del vector 2: " % i))
  
  for i in range (dim):
    v3[i] = v1[i] + v2[i]
  
  print 'v1 = ' , v1
  print 'v2 = ' , v2
  print 'v1 + v2 = ', v3