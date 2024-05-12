import numpy as np
dpmFile = np.loadtxt("plane-11=4.5-test.dpm", usecols=range(1, 13), skiprows=2)

print (dpmFile)