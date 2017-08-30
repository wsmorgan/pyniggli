Examples
========

Pyniggli is well documented but we'll provide some basic usage
examples here. To use pyniggli to get the niggli reduced cell and the
transformation matrix for a lattice defined by the vectors `a =
[1,1,1], b = [2,2,2], c = [3,3,3]' use pyniggli as follows.
::
  >>> import numpy as np
  >>> from pyniggli import reduced_cell

  >>> A = np.transpose([[1,1,1],[2,2,2],[3,3,3]])

  >>> B = reduced_cell(A)
  >>> #For the niggli reduced cell vectors
  >>> print(B.niggli)
  >>> #For the transformation matrix
  >>> print(B.C)

