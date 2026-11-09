import numpy as np 
import matplotlib.pyplot as plt 

def fourier(x: float, N: int): 
    wave = 0
    for n in range(1, N+1): 
        # wave += np.cos((2*n+1)*x) / (2*n+1)**2
        wave += np.cos(2*np.pi*n*x) / n**2
    return 1/2 + wave

fig, ax = plt.subplots(2, 2, figsize=(8, 4)) 
x = np.linspace(-1.6 , 1.6, 500)
ax[0, 0].plot(x, fourier(x, 1), color='tab:blue') 
ax[0, 0].text(0.82, 0.85, 'N=1', transform=ax[0, 0].transAxes)
ax[0, 0].set_ylim([-0.6, 2.4])
ax[0, 1].plot(x, fourier(x, 3), color='tab:blue') 
ax[0, 1].text(0.82, 0.85, 'N=3', transform=ax[0, 1].transAxes)
ax[0, 1].set_ylim([-0.6, 2.4])
ax[1, 0].plot(x, fourier(x, 10), color='tab:blue') 
ax[1, 0].text(0.82, 0.85, 'N=10', transform=ax[1, 0].transAxes)
ax[1, 0].set_ylim([-0.6, 2.4])
ax[1, 1].plot(x, fourier(x, 100), color='tab:blue') 
ax[1, 1].text(0.82, 0.85, 'N=100', transform=ax[1, 1].transAxes)
ax[1, 1].set_ylim([-0.6, 2.4])
plt.savefig('fourier_expansion.png')
plt.show()