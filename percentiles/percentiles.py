import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    # percentiles of the data 

    x = np.array(x)
    return np.percentile(x,q)