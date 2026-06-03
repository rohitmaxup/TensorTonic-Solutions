import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    X = np.asarray(X, dtype=float)

    mn = np.min(X, axis=axis, keepdims=True)
    mx = np.max(X, axis=axis, keepdims=True)

    return (X - mn) / np.maximum(mx - mn, eps)