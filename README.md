# LaserDiag

**LaserDiag** is an open-source Python toolkit for advanced analysis and diagnostics of laser systems. It supports time-domain and frequency-domain analysis (FFT, SNR, THD, modulation transfer, phase shift), batch processing, and hardware integration (TiePie, BK Precision, etc).

## ✨ Features

- Load laser data from CSV, TDMS, or binary files
- Compute transfer function, modulation depth, phase shift vs. frequency
- FFT analysis, noise spectrum, SNR, and THD
- Batch file processing and statistical summaries
- Ready-to-use demo notebooks and real example plots
- Extensible for custom laser or sensor setups

## 🚀 Example Workflow

```python
from core.io import load_csv
from core.analysis import fft_analysis, thd_calc
from core.plot import plot_fft

data, fs = load_csv('data.csv')
f, spectrum = fft_analysis(data, fs)
plot_fft(f, spectrum)
thd = thd_calc(data, fs)
print("Total Harmonic Distortion:", thd)
