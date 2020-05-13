import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import scipy.special



np.random.seed(440)

x1 = np.linspace(-5, 5, 100)

mu = 0
sigma2 = 1
y1 = (1/(sigma2**0.5*(2*np.pi)**0.5)*(np.exp((-(x1-mu)**2)/(2*sigma2))))

r1 = 0.5 * (1 + scipy.special.erf((x1 - mu)/(2*sigma2)**0.5))

sigma2 = 5
y2 = (1/(sigma2**0.5*(2*np.pi)**0.5)*(np.exp((-(x1-mu)**2)/(2*sigma2))))
r2 = 0.5 * (1 + scipy.special.erf((x1 - mu)/(2*sigma2)**0.5))

sigma2 = 0.4
y3 = (1/(sigma2**0.5*(2*np.pi)**0.5)*(np.exp((-(x1-mu)**2)/(2*sigma2))))
r3 = 0.5 * (1 + scipy.special.erf((x1 - mu)/(2*sigma2)**0.5))

#data = np.column_stack((x1, y1))
 
fig, (ax1, ax2) = plt.subplots(
    nrows=1, ncols=2,
    figsize=(8, 4)
)
 
#ax1.scatter(x=x1, y=y1, marker='o', c='k', edgecolor='w')
ax1.plot(x1, y1, label=r"$\sigma^{2}$=1")
ax1.plot(x1, y2, label=r"$\sigma^{2}$=5")
ax1.plot(x1, y3, label=r"$\sigma^{2}$=0.4")
ax1.set_xlim(-5, 5)
ax1.set_ylim(0, 1)
ax1.legend()

ax2.plot(x1, r1, label=r"$\sigma^{2}$=1")
ax2.plot(x1, r2, label=r"$\sigma^{2}$=5")
ax2.plot(x1, r3, label=r"$\sigma^{2}$=0.4")
ax2.set_xlim(-5, 5)
ax2.set_ylim(0, 1)
ax2.legend()

#ax1.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=15))

plt.show()

#plt.savefig('1.png')
