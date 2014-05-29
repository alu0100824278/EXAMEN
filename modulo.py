#!/usr/bin/python
#! encoding: UTF-8

def suma(p1,p2):
  #Grados
  grado = (0,1,2,3)
  #Coeficientes
  p1 = [1,0,1,0]
  p2 = [0,1,0,1]
  p3 = []
  #Suma
  for i in range (grado):
    p3[i] = p1[i] + p2[i]

  print p3  
  return p3
