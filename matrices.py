#!/usr/bin/python
#! encoding: UTF-8

fyc = (2,3,4)

for i in fyc:
  M=[]
  N=[]
  C=[]
  print 'Evaluacion suma matrices de orden %dx%d' % (i,i)
  for j in range (i):
    M.append([0]*i)
    N.append([0]*i)
    C.append([0]*i)
  
  for x in range(i):
    for y in range(i):
      M[x][y]=int(raw_input('Cordenada (%d,%d) dela matriz M: ' % (x,y)))
      N[x][y]=int(raw_input('Cordenada (%d,%d) dela matriz N: ' % (x,y)))
      C[x][y]=M[x][y]+N[x][y] 
      
  print 'Matriz M: ' , M
  print 'Matriz N: ' , N
  print 'M + N = ' , C