#!/usr/bin/python
#! encoding: UTF-8

from sympy import *

def suma(p1,p2):
  g1 = len(p1)
  g2 = len(p2)
  
  if (g1 > g2):
    p3 = [0]*g1
    for i in range(g2):
      p3[i] = p1[i] + p2[i]
      
    for j in range (g2, g1):
      p3[j] = p3[j] + p1[j]  
      
    print 'p1 = ' , p1
    print 'p2 = ' , p2
    print 'p1 + p2 = ' , p3
    
  else:
    p3 = [0]*g2
    for i in range(g1):
      p3[i] = p1[i] + p2[i]
    
    for j in range (g1, g2):
      p3[j] = p3[j] + p2[j]
        
    print 'p1 = ' , p1
    print 'p2 = ' , p2
    print 'p1 + p2 = ' , p3
    