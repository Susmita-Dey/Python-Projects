# install matplotlib

import matplotlib.pyplot as plt

x1 = [2, 4, 5, 6]
y1 = [2, 3, 6, 7]

plt.plot(x1, y1, label='Line 1')

x2 = [1, 2, 3, 4, 5]
y2 = [1, 2, 3, 4, 4]

plt.plot(x2, y2, label='Line 2')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Demo Graph - Two Lines')

plt.legend()

plt.show()
