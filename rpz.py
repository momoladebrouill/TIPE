# plot linear function using matplotlib

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100000)
pos = lambda x : x if x < 5 else 5
vit = lambda x : 1 if x < 5 else 0
def acc(x):
    if abs(x-5) < 0.01:
        return -1
    if x==0:
        return 1
    return 0 

def apply(f, x):
    return [f(i) for i in x]
plt.style.use('Solarize_Light2')
plt.plot(x, apply(pos, x), label='Position')
# change graph
plt.xlabel('Temps')
plt.ylabel('Position')
plt.legend()
plt.savefig('position.png')
plt.figure()

plt.plot(x, apply(vit, x), label='Vitesse')
plt.xlabel('Temps')
plt.ylabel('Vitesse')
plt.legend()
plt.savefig('vitesse.png')
plt.figure()

plt.plot(x, apply(acc, x), label='Acceleration')
plt.xlabel('Temps')
plt.ylabel('Acceleration')
plt.legend()
plt.savefig('acceleration.png')
