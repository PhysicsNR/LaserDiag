import numpy as np
import pandas as pd

def load_csv(filename):
    """Load time-domain data from a CSV file."""
    data = pd.read_csv(filename)
    return data.values[:, 0], 1.0  # Replace 1.0 with the actual sample rate if available

def load_tdms(filename):
    """Load data from a TDMS file using nptdms."""
    try:
        from nptdms import TdmsFile
    except ImportError:
        raise ImportError("Install nptdms via pip: pip install nptdms")
    tdms_file = TdmsFile.read(filename)
    group = tdms_file.groups()[0]
    channel = group.channels()[0]
    data = channel[:]
    # Replace the following two lines with actual sample rate extraction
    wf_samples = channel.property('wf_samples') if 'wf_samples' in channel.properties else len(data)
    wf_duration = channel.property('wf_duration') if 'wf_duration' in channel.properties else 1
    fs = wf_samples / wf_duration
    return data, fs
