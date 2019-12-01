import numpy as np

def _input(seq):
    if type(seq) == list:
        return np.array(seq)

    assert type(seq) == np.ndarray, 'Input is not a list or a Numpy array'
    assert len(seq.shape) == 1, 'Input is not a one-dimensional Numpy array'

    return seq

def _geom_vec(seq, gamma=0.2):
    n = seq.shape[0]
    return np.geomspace(1, (gamma**(n-1) + 0.001), num=n)[::-1]

def _seq2grad(seq):
    return seq[1:] - seq[:-1]

def _spread(seq):
    return abs(seq.max() - seq.min())

def _predict(seq):
    grads = _seq2grad(seq)
    geom = _geom_vec(moments)
    return seq[-1] + np.dot(grads, geom)/geom.sum()

def _randscore(seq):
    score = 0
    for i in range(2, seq.shape[0]):
        nxt = _predict(seq[: i])
        score += abs(nxt - seq[i])
    return score/_spread(seq)

def _threshold(seq, T=1.955):
    return _randscore(seq) >= T

def random_score(seq, raw=False, T=1.955):
    seq = _input(seq)
    if raw:
        return _randscore(seq)
    else:
        return _threshold(seq, T)