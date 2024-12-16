# -*- coding: latin-1- -*-
#1� linha para poder usar acentos
import numpy as np
a=np.array([1,3,5,2,4,6],int) 
print(a.dtype)        #cuidado com o tipo dos dados
print('a=',a)
print('a-5=',a-5)
a=np.array([1,3,5,2,4,6],float)
print(a.dtype)
print(a.shape)
a=a.reshape((3,2))    #modificar dimens�es 
print(a.shape)
print(a[0,:])         #1� linha
print(a[:,0])         #1� coluna
b=a
a[0,0:2]=0            #2 primeiros elementos da 1� linha = 0 
print('b=',b)          # modificar um, modifica o outro
b=a.copy()            # para copiar usar .copy()
a[1,0:2]=-1
print('a=',a)
print('b=',b)
