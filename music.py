import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as sci_wav

def note(freq, len):
    t = np.linspace(0, len, len*44100)
    data = np.sin(2 * np.pi * freq * t) * 10000
    return data.astype(int16)

if __name__ == "__main__":
    u = np.load("u.npy")
    u = u * 12
    u = np.ceil(u)
    for i in len(u):
        note(440 *

    sci_wav.write("u.wav", 44100, u)
