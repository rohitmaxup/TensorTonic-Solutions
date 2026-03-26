import numpy as np

def sample_var_std(x):
    x = np.array(x)
    
    t = (np.var(x, ddof=1), np.std(x, ddof=1))
    
    return t