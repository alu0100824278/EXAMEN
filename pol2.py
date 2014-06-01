#!/usr/bin/python
#! encoding: UTF-8

import modulo

grados = (2,3,4,5)

for n in grados:
  print 'Evaluacion suma de polinomios de grado %d' % n
  p1 = [0]*(n+1)
  p2 = [0]*(n+1)
  
  for i in range(n+1):
    p1[i] = int(raw_input('Coeficiente de grado (%d) (polinomio 1): ' % (i))) 

  for j in range(n+1):
    p2[j] = int(raw_input('Coeficiente de grado (%d) (polinomio 2): ' % (j))) 

  modulo.suma(p1,p2)