import numpy as np
import matplotlib.pyplot as plt
I=np.linspace(0,10,100)
gamma=np.zeros(100)
gamma1=np.zeros(100)
for i in range(100):
 gamma[i]=-0.51*np.sqrt(I[i])/(1+3.288*0.196*np.sqrt(I[i]))
for i in range(100):
 gamma1[i]=-0.51*np.sqrt(I[i])
plt.plot(np.sqrt(I),gamma,'r')
plt.plot(np.sqrt(I),gamma1,'b--')
plt.ylabel('log$_{10}\gamma_{\pm}$')
plt.xlabel('$\sqrt{I}$ (mol/L)')
plt.savefig('highionic.png')

plt.figure()

I=np.linspace(0,0.1,100)
gamma=np.zeros(100)
gamma1=np.zeros(100)
for i in range(100):
 gamma[i]=-0.51*np.sqrt(I[i])/(1+3.288*0.196*np.sqrt(I[i]))
for i in range(100):
 gamma1[i]=-0.51*np.sqrt(I[i])
plt.plot(np.sqrt(I),gamma,'r')
plt.plot(np.sqrt(I),gamma1,'b--')
plt.ylabel('log$_{10}\gamma_{\pm}$')
plt.xlabel('$\sqrt{I}$ (mol/L)')
plt.savefig('lowionic.png')
