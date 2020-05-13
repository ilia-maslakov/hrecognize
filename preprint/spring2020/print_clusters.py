import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


np.random.seed(440)

x1 = np.random.randint(low=500, high=1000, size=50) + 300
y1 = np.random.randint(np.sin(x1), high=1000, size=50) + 300

x1p = np.random.randint(low=1, high=1100, size=10)
y1p = np.random.randint(low=100, high=1500, size=10)

x1 = x1**1 

x1 = np.append(x1, x1p)
y1 = np.append(y1, y1p)


np.random.seed(1440)

x2 = np.random.randint(low=500, high=1000, size=50) - 300
y2 = np.random.randint(np.tanh(x2), high=1000, size=50) - 300

x2p = np.random.randint(low=1, high=1100, size=10)
y2p = np.random.randint(low=100, high=1500, size=10)

x2 = np.append(x2, x2p)
y2 = np.append(y2, y2p)


#data = np.column_stack((x1, y1))
 
fig, (ax1, ax2) = plt.subplots(
    nrows=1, ncols=2,
    figsize=(8, 4)
)
 
ax1.scatter(x=x1, y=y1, marker='o', c='k', edgecolor='w')
ax1.set_title('Class A')
ax1.set_xlim(0, 1500)
ax1.set_ylim(0, 1500)
rect1 = patches.Rectangle((670,260), 690,1070,linewidth=1, edgecolor='r', facecolor='none')
ax1.add_patch(rect1)


ax2.scatter(x=x2, y=y2, marker='X', c='w', edgecolor='k')
ax2.set_title('Class B')
ax2.set_xlim(0, 1500)
ax2.set_ylim(0, 1500)
rect1 = patches.Rectangle((130,0), 630,750,linewidth=1, edgecolor='r', facecolor='none')
ax2.add_patch(rect1)

#ax1.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=15))

plt.show()

#plt.savefig('1.png')
