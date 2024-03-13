import numpy as np
from pylab import * 
import matplotlib.pyplot as plt

Ndata = 31 

kx = np.linspace(-np.pi,np.pi,Ndata) 
ky = np.linspace(-np.pi,np.pi,Ndata) 
d  = np.zeros((Ndata,Ndata)) 

X,Y = np.meshgrid(kx,ky) 

m = 1.0            

for i in range(Ndata):
    for j in range(Ndata):
        d[i,j] = np.sin(kx[i])**2 + np.sin(ky[j])**2 + (-2+m+np.cos(kx[i])+np.cos(ky[j]))**2
        d[i,j] = np.sqrt(d[i,j]) 

fig = plt.figure() 
ax = fig.add_subplot(projection='3d') 
ax.plot_surface(X/np.pi,Y/np.pi,d)
ax.plot_surface(X/np.pi,Y/np.pi,-d) 
ax.set_xticks(np.arange(-1,1.5,0.5),fontsize=12)
ax.set_yticks(np.arange(-1,1.5,0.5),fontsize=12) 
ax.set_xlabel(r'$k_x (\pi)$',fontsize=12) 
ax.set_ylabel(r'$k_y (\pi)$',fontsize=12)
ax.set_zlabel(r'$E$',fontsize=12) 
ax.set_title('m = '+str(m),fontsize=12) 
plt.show() 
