import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import rc
import matplotlib.pyplot as plt
x = np.linspace(1, 100, 100)
y = np.log10(x)
plt.clf()  # Ensures a clean plotting canvas.
plt.rc('text', usetex=True)
plt.rc('figure', figsize=(1920, 1080))
plt.rc('font', family='serif', serif=['Computer Modern Roman'], size=14)
# plt.title("Sorting Improvised with Interpolation Search")
plt.ylabel("$\pi(\delta)$")
plt.xlabel("$\delta$")
plt.plot(x, y, "k--")
plt.legend(loc='upper left', frameon=False, handlelength=3)
plt.savefig('1.pdf', format="pdf")