import numpy as np

def fft_analysis(data, fs):
    N = len(data)
    f = np.fft.rfftfreq(N, d=1/fs)
    spectrum = np.abs(np.fft.rfft(data))
    return f, spectrum

def thd_calc(data, fs, f0=1000, num_harmonics=5):
    N = len(data)
    f = np.fft.rfftfreq(N, d=1/fs)
    spectrum = np.abs(np.fft.rfft(data))
    idx_f0 = np.argmin(np.abs(f - f0))
    harmonics = [np.argmin(np.abs(f - (n+1)*f0)) for n in range(num_harmonics)]
    fundamental = spectrum[idx_f0]
    harmonic_power = np.sum([spectrum[h]**2 for h in harmonics])
    thd = np.sqrt(harmonic_power) / fundamental
    return thd

def modulation_transfer(data, fs):
    # Dummy implementation: for real use, provide modulated data and implement extraction
    mod_depth = np.array([1])  # Placeholder
    phase = np.array([0])      # Placeholder
    return mod_depth, phase
