# RandTest

A lightweight package for quick and accurate determinations of the randomness of a sequence.

# Overview

Identifying random patterns, and conversely, ordered patterns, is a major tool with applicability to a wide variety of fields, from mathematical analysis to cybersecurity. Random Test looks for randomness in sequences of numbers by searching for patterns which are inherently unpredictable. It uses an exponentially-decaying moment prediction to determine the net deviation between the predicted and actual elements of a sequence. In tests, this led to a net **predictive accuracy of 99.85% for nonrandom sequences and 96.82% for random sequences**. Additionally, this package is able to provide these predictions in under a millisecond for sequences shorter than 10 elements and under 100 milliseconds for sequences shorter than 1000 elements.

## Requirements

RandTest is built for Python 3. It has only one requirement:

    - Numpy

# Installation

To download randtest, use PyPI via pip:

```sh
pip install randtest
```

Alternatively, you can clone this Github repository and build from source:

```sh
git clone https://github.com/sudo-rushil/randtest
cd randtest
python setup.py install
```

Verify your installation by running

```Python
>>> import randtest
>>> randtest.random_score([0, 1, 2, 3])
'False'
```

# Examples

RandTest is extremely simple to use. You only need to input either a list or a 1D Numpy array of numbers. The prediction returns `False` if the sequence is ordered and `True` if the sequence is random.

```Python
import numpy as np
import randtest as rt

ordered_sequence = np.arange(10)
random_sequence = np.random.randint(10, size=10)

print(rt.random_score(ordered_sequence))

print(rt.random_score(random_sequence))
```

> False

> True 

# Documentation

RandTest is a very lightweight package. It has polymorphism support; you can pass either a list or a 1D Numpy array without any effort. It is also extremely fast, returning predictions in under 100 milliseconds, even in extreme cases.

## Algorithm

RandTest identifies randomness by one of its byworded properties - unpredictability. It uses the conformance of a sequence to a continuously generated predicted model as a measure of how unpredictable - how random - that sequence is.

For any sequence of numbers $a_i$, with $i$ ranging from $0$ to $n-1$, where $n$ is the length of the sequence, we can compute the element-wise gradients as a new sequence, $\Delta a_i = a_{i+1} - a_i$, which has length $n-1$. 
From here, we can apply exponential scaling, sum these gradients, and normalize to obtain the predicted gradient, $\hat{\Delta a_n}$.

$$
\hat{\Delta a_n} = \frac{\sum_{i=0}^{n-2}{\gamma^i \cdot \Delta a_i}}{\sum_{i=0}^{n-2}{\gamma^i}}
$$

Then, the predicted value $\hat{a_n}$ is $a_{n-1} + \hat{\Delta a_n}$.

To compute the numerical randomness score of a sequence $a_i$, with $i$ ranging between $0$ and $n$, we take the sum

$$
\sum_{k = 1}^{n}{|\hat{a_k} - a_k|}\mathrm{,}
$$

where the predicted value $\hat{a_k}$ comes from the sliced subsequence of $a$ containing all elements up to $k$.

In the RandTest implementation, this randomness score is converted into a prediction by comparision with an empirically determined threshold, which is chosen to maximize the combined precision and sensitivity of the classifier on both random and ordered sequences.

## API

RandTest contains a single function, `random_score`. This returns `True` if the input sequence *is* random. This means it can be integrated directly into your current control flow.

```Python
import numpy as np
from randtest import random_score

# Ordered sequences
random_score(np.arange(10)) # False
random_score(np.geomspace(1, 27, num=4)) # False
random_score([0, 1, 2, 3, 4, 5]) # False

# Random sequences
random_score(np.random.randint(100, size=10)) # True
random_score([7, 12, 14, 88, 9]) # True
```

This function has an optional input of `raw=True`, which enables you to directly access the randomness metric as defined above. However, we reccomend you do not pass this in production environments, as the function has already been thresholded on over 200,000 examples.