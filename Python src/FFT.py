import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

def fastfourier(inp):
    "Intakes data, output is plot on screen of FFT of imported data"
    X = fft(inp)
    
    "inp must be array, can modify based on actual if required"    

    N = len(X)
    n = np.arange(N)
    "Need to determine sampling rate defined as sr here"
    T = N/2000
    freq = n/T
    plt.figure (figsize = (6,6))
    plt.stem(freq, np.abs(X), 'b', markerfmt=" ", basefmt="-b")
    plt.xlabel('Freq (Hz)')
    plt.ylabel('FFT Amplitude')
    plt.show()
    
if __name__ == '__main__':
    fastfourier()