import matplotlib.pyplot as plt

def plot_fft(f, spectrum, filename=None):
    plt.figure(figsize=(8,4))
    plt.plot(f, spectrum)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.title("FFT Spectrum")
    plt.grid(True)
    if filename:
        plt.savefig(filename)
    plt.show()

def plot_transfer_function(mod_depth, phase, filename=None):
    plt.figure(figsize=(8,4))
    plt.plot(mod_depth, label="Modulation Depth")
    plt.plot(phase, label="Phase Shift")
    plt.xlabel("Frequency Index")
    plt.ylabel("Value")
    plt.legend()
    plt.title("Transfer Function")
    plt.grid(True)
    if filename:
        plt.savefig(filename)
    plt.show()
