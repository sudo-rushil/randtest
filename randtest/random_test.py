'''
Main code for the random_test module.
'''
import numpy as np

def _input(seq):
    if isinstance(seq, list):
        return np.array(seq)

    assert isinstance(seq, np.ndarray), 'Input is not a list or a Numpy array'
    assert len(seq.shape) == 1, 'Input is not a one-dimensional Numpy array'

    return seq

def _geom_vec(seq, gamma=0.2):
    seq_length = seq.shape[0]
    return np.geomspace(1, (gamma**(seq_length-1) + 0.001), num=seq_length)[::-1]

def _seq2grad(seq):
    return seq[1:] - seq[:-1]

def _spread(seq):
    return abs(seq.max() - seq.min())

def _predict(seq):
    grads = _seq2grad(seq)
    geom = _geom_vec(grads)
    return seq[-1] + np.dot(grads, geom)/geom.sum()

def _randscore(seq):
    score = 0
    for i in range(2, seq.shape[0]):
        nxt = _predict(seq[: i])
        score += abs(nxt - seq[i])
    return score/_spread(seq)

def _threshold(seq, threshold=1.955):
    return _randscore(seq) >= threshold

def random_score(seq, raw=False, threshold=1.955):
    seq = _input(seq)
    if raw:
        return _randscore(seq)
    return _threshold(seq, threshold)
