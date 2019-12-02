# RandTest

A light package for quick and accurate determinations of the randomness of a sequence.

# Overview

Identifying random patterns, and conversely, ordered patterns, is a major tool with applicability to a wide variety of fields, from mathematical analysis to cybersecurity. Random Test looks for randomness in sequences of numbers by searching for patterns which are inherently unpredictable. It uses an exponentially-decaying moment prediction to determine the net deviation between the predicted and actual elements of a sequence. In tests, this led to a net **predictive accuracy of 99.85% for nonrandom sequences and 96.82% for random sequences**. Additionally, this package is able to provide these predictions in under a millisecond for sequences shorter than 10 elements and under 100 milliseconds for sequences shorter than 1000 elements.

## Requirements

RandTest is built for Python 3. It has only one requirement:

    - Numpy

# Installation

To download randtest, use PyPI via pip:

```sh
\$ pip install randtest
```

Alternatively, you can clone this Github repository and build from source:

```sh
\$ git clone https://github.com/sudo-rushil/randtest
\$ cd randtest
\$ python setup.py install
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

RandTest is a very light package. It has polymorphism support; you can pass either a list or a 1D Numpy array without any effort. It is also extremely fast, returning predictions in under 100 milliseconds, even in extreme cases.

## Algorithm

RandTest identifies randomness by one of its byworded properties - unpredictability. It uses the conformance of a sequence to a continuously generated predicted model as a measure of how unpredictable - how random - that sequence is.

For any sequence of numbers <img src="/tex/65ed4b231dcf18a70bae40e50d48c9c0.svg?invert_in_darkmode&sanitize=true" align=middle width=13.340053649999989pt height=14.15524440000002pt/>, with <img src="/tex/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/> ranging from <img src="/tex/29632a9bf827ce0200454dd32fc3be82.svg?invert_in_darkmode&sanitize=true" align=middle width=8.219209349999991pt height=21.18721440000001pt/> to <img src="/tex/efcf8d472ecdd2ea56d727b5746100e3.svg?invert_in_darkmode&sanitize=true" align=middle width=38.17727759999999pt height=21.18721440000001pt/>, where <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> is the length of the sequence, we can compute the element-wise gradients as a new sequence, <img src="/tex/3625ab7c1b30dcd3c08e10061c91ce68.svg?invert_in_darkmode&sanitize=true" align=middle width=114.01535969999999pt height=22.465723500000017pt/>, which has length <img src="/tex/efcf8d472ecdd2ea56d727b5746100e3.svg?invert_in_darkmode&sanitize=true" align=middle width=38.17727759999999pt height=21.18721440000001pt/>. 
From here, we can apply exponential scaling, sum these gradients, and normalize to obtain the predicted gradient, <img src="/tex/c88565636040fa245dadbf8378667fc4.svg?invert_in_darkmode&sanitize=true" align=middle width=30.51384929999999pt height=31.141535699999984pt/>.

<p align="center"><img src="/tex/a3b25a0334c90fcf366078c7e4bdaaf5.svg?invert_in_darkmode&sanitize=true" align=middle width=155.72099895pt height=45.82666275pt/></p>

Then, the predicted value <img src="/tex/28d65fd9ccc424e34ec4f277701115a2.svg?invert_in_darkmode&sanitize=true" align=middle width=16.81517804999999pt height=22.831056599999986pt/> is <img src="/tex/5bd075809c77195b473bbb706e536c98.svg?invert_in_darkmode&sanitize=true" align=middle width=85.06867215pt height=31.141535699999984pt/>.

To compute the numerical randomness score of a sequence <img src="/tex/65ed4b231dcf18a70bae40e50d48c9c0.svg?invert_in_darkmode&sanitize=true" align=middle width=13.340053649999989pt height=14.15524440000002pt/>, with <img src="/tex/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/> ranging between <img src="/tex/29632a9bf827ce0200454dd32fc3be82.svg?invert_in_darkmode&sanitize=true" align=middle width=8.219209349999991pt height=21.18721440000001pt/> and <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/>, we take the sum

<p align="center"><img src="/tex/caade0fdcb3a04fd29e36c52651d9451.svg?invert_in_darkmode&sanitize=true" align=middle width=93.9936063pt height=45.2741091pt/></p>

where the predicted value <img src="/tex/b22ec94b5bdaa79af222bfafdd3f2110.svg?invert_in_darkmode&sanitize=true" align=middle width=15.95518319999999pt height=22.831056599999986pt/> comes from the sliced subsequence of <img src="/tex/44bc9d542a92714cac84e01cbbb7fd61.svg?invert_in_darkmode&sanitize=true" align=middle width=8.68915409999999pt height=14.15524440000002pt/> containing all elements up to <img src="/tex/63bb9849783d01d91403bc9a5fea12a2.svg?invert_in_darkmode&sanitize=true" align=middle width=9.075367949999992pt height=22.831056599999986pt/>.

In the RandTest implementation, this randomness score is converted into a prediction by comparision with an empirically determiend threshold, which is chosen to maximize the combined precision and sensitivity of the classifier on both random and ordered sequences.

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