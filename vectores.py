#!/usr/bin/python
#! encoding: UTF-8

v1 = [0]*2
v2 = [0]*2
v3 = [0]*2

for i in range (2):
  v1[i] = int(raw_input("Coordenada %d del vector 1: " % i))

for i in range (2):
  v2[i] = int(raw_input("Coordenada %d del vector 2: " % i))
  
for i in range (2):
  v3[i] = v1[i] + v2[i]
  
print 'v1 = ' , v1
print 'v2 = ' , v2
print 'v1 + v2 = ', v3