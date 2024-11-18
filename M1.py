import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import random

t = np.linspace(0, 3, 12 * 1024)
n_samples = len(t)

N = 4

ti = [0, 0.5, 1.5, 2.25] #(start time)
Ti = [0.5, 1, 0.75, 0.75] #(duration)

def getF(i):
    F = 0
    if i == 1:
        F = 130.81
    elif i == 2:
        F = 146.83
    elif i == 3:
        F = 164.81
    elif i == 4:
        F = 174.61
    elif i == 5:
        F = 196
    elif i == 6:
        F = 220
    elif i == 7:
        F = 246.93
    return F


def getf(i):
    f = 0
    if i == 1:
        f = 261.63
    elif i == 2:
        f = 293.66
    elif i == 3:
        f = 329.63
    elif i == 4:
        f = 349.23
    elif i == 5:
        f = 392
    elif i == 6:
        f = 440
    elif i == 7:
        f = 493.88
    return f


x = np.zeros(n_samples)
for i in range(N):
    F = getF(random.randint(0,7))
    f = getf(random.randint(0,7))
    x += (np.sin(2*np.pi*F*t) + np.sin(2*np.pi*f*t)) * (np.heaviside(t-ti[i], 0) - np.heaviside(t-ti[i]-Ti[i], 0))

#plt.plot(t, x)
#plt.xlabel('t')
#plt.ylabel('x(t)')
#plt.show()

sd.play(x, 3 * 1024)
sd.wait()
