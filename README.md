# pyniggli

Pyniggli is a python package that uses perform niggli reduction on a
cell of a lattice. The niggli cell is useful because it is unique for
each lattice and extremely useful for [Bravais
lattice](https://en.wikipedia.org/wiki/Bravais_lattice)
identification. Pyniggli performs the
[Krivy-Gruber](http://journals.iucr.org/a/issues/1976/02/00/a12875/a12875.pdf)
algorithm for niggli reduction and provides the user with the
resultant transformation matrix as described by
[Grosse-Kunstleve](https://journals.iucr.org/a/issues/2004/01/00/sh5006/sh5006.pdf).

Full API documentation is available at: [github pages](https://wsmorgan.github.io/pyniggli/).

## Installing the package

To install this python package you can clone this repository then use:

```
python setup.py install
```

## Example

To use pyniggli to get the niggli reduced cell and the transformation
matrix for a lattice defined by the vectors `a = [1,1,1], b = [2,2,2],
c = [3,3,3]' use pyniggli as follows:

```
import numpy as np
from pyniggli import reduced_cell

A = np.transpose([[1,1,1],[2,2,2],[3,3,3]])

B = reduced_cell(A)
#For the niggli reduced cell vectors
print(B.niggli)
#For the transformation matrix
print(B.C)
```

## Issues

If you find a bug in pyniggli or decide to contribute to pyniggli
please see the [contributions](contributing) guidelines.

## Python Packages Used

-numpy
