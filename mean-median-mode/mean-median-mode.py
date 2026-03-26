import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.array(x)
    mean = np.mean(x)
    median = np.median(x)
    counts = Counter(x)
    mode = max(counts, key=counts.get)

    t = (mean,median,mode)
    return t
    