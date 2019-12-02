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
$ pip install randtest
```

Alternatively, you can clone this Github repository and build from source:

```sh
$ git clone https://github.com/sudo-rushil/randtest
$ cd randtest
$ python setup.py install
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
