# -*- coding: latin-1 -*- 
#AA - script para ler e visualizar imagens
import matplotlib.pyplot as plt
fName="C:/Users/diogo/Desktop/LEIM/5sem/AA/lab0/figs/lena.tif"   #necess�rio estar na mesma dir. que c�digo
I=plt.imread(fName)#ler imagens (I-> numpy array uint8)
plt.subplot(1,2,1) #1x2 figuras (3� valor = �ndice da figura 1 ou 2)
plt.imshow(I) #origem no canto inferior esquerdo
#tirar eixos - plt.axis('off') tb d�
plt.xticks([]),plt.yticks([]),plt.box(True) 
#aten��o que pixeis est�o em  uint8 
#s� � poss�vel representar valores entre 0-255
plt.subplot(1,2,2)
plt.imshow(I*2)
plt.xticks([]),plt.yticks([]),plt.box(True)
#guarda figura 
#plt.savefig('../figs/L0AAex005.png', transparent=True, bbox_inches='tight', pad_inches=0)
plt.show() #n�o � necess�rio em     #guardar  em ficheiro ".png"
           #iPython usar show()     #(na directoria "../figs/")
                                    #(d� erro se n�o existir)

