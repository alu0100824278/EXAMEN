#!/usr/bin/python
#! encoding: UTF-8

#Grados
grado = [0,1,2,3]
#Coeficientes
p1 = [1,0,1,0]
p2 = [0,1,0,1]
p3 = []
p3.append([0]*3)
#Suma
for i in range (3):
  p3[i] = p1[i] + p2[i]
print p3