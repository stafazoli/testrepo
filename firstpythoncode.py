import numpy as np
x = np.linspace(0, 10, 5)
print(x)

lenx = len(x)
print("the length of the vector is {0}".format(lenx))

for i in range(0,lenx):
    print("the %d-th element is %.1f." % (i+1, x[i]))
