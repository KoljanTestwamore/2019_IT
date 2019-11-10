import math
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

M, N = 5, 3


def get_efficiency_array(mx):
    result = np.ones(len(mx), dtype=bool)
    for i, x0 in enumerate(mx):
        flag = False
        for x1 in np.concatenate((mx[:i], mx[i + 1:])):
            if not np.all(x0 > x1):
                flag = False
                break
        result[i] = flag
    return result


X = np.random.sample((M, N))

efficiency_array = get_efficiency_array(X)
ax = plt.subplot(111, projection="polar")
plt.thetagrids(np.arange(0, 360, 360/N))

for i in range(len(efficiency_array)):
    if efficiency_array[i]:
        ax.plot(np.append(np.arange(0, N, 1), 0) * 2 * math.pi/N, np.append(X[i, :], X[i, 0]), color="r")
    else:
        ax.plot(np.append(np.arange(0, N, 1) * 2 * math.pi/N, 0), np.append(X[i, :], X[i, 0]), color="b")
