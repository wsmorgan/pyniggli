import numpy as np
import pytest

from pyniggli.niggli import reduced_cell


def test_reduction():
    """Tests the niggli reduction of some basic cells."""

    #1
    A = np.transpose([[1,0,0],[0,1,0],[0,0,2]])
    B = reduced_cell(A)
    assert np.allclose(B.C,np.array([[1,0,0],[0,1,0],[0,0,1]]))
    assert np.allclose(B.niggli,A)
    assert np.allclose(B.niggli,np.dot(A,B.C))

    #2
    A = np.transpose([[0.5,0,0.5],[0,3,0],[0.5,0,-0.5]])
    B = reduced_cell(A)
    assert np.allclose(B.niggli,np.transpose([[-0.5,0,-0.5],[-0.5,0,0.5],[0,-3,0]]))
    assert np.allclose(B.niggli,np.dot(A,B.C))

    #3
    A = np.transpose([[1.00000000,0.00000000,0.00000000],[-0.50000000,0.86602540,1.63299320],[0.00000000,-1.73205080,1.63299320]])
    B = reduced_cell(A)
    assert np.allclose(B.niggli,[[-1.       ,  0.5      ,  0.       ],
       [ 0.       , -0.8660254, -1.7320508],
       [ 0.       , -1.6329932,  1.6329932]])

    #4
    A = np.transpose([[1.00000000, 0.00000000, 0.00000000],
                      [-0.50000000, 0.86602540, 0.00000000],
                      [0.00000000, 0.00000000, 3.26598640]])
    B = reduced_cell(A)
    assert np.allclose(B.niggli, np.transpose([[ 1., 0., 0.],
                                               [-0.5, 0.8660254, 0.],
                                               [ 0., 0., 3.2659864]]))

    #5
    A = np.transpose([[1.00000000, 0.00000000, 0.00000000],
                      [-0.50000000, 0.86602540, 1.63299320],
                      [0.00000000, -1.73205080, 1.63299320]])
    B = reduced_cell(A)
    assert np.allclose(B.niggli, np.transpose([[-1., 0., 0.],
                                               [0.5, -0.8660254, -1.6329932],
                                               [0., -1.7320508, 1.6329932]]))

    #6
    A = np.transpose([[1.00000000, 0.00000000, 0.00000000],
                      [0.50000000, -0.86602540, 3.26598640],
                      [0.00000000, -1.73205080, 0.00000000]])
    B = reduced_cell(A)
    assert np.allclose(B.niggli, np.transpose([[1., 0., 0.],
                                               [0., -1.7320508, 0.],
                                               [-0.5, 0.8660254, -3.2659864]]))

    #7
    A = np.transpose([[1.00000000, 0.00000000, 0.00000000],
                      [0.50000000, 4.33012700, 0.00000000],
                      [0.00000000, 0.00000000, 1.63299320]])
    B = reduced_cell(A)
    assert np.allclose(B.niggli, np.transpose([[-1., 0., 0.],
                                               [0., 0., 1.6329932],
                                               [0.5, 4.330127, 0.]]))

    #8
    A = np.transpose([[1.00000000, 0.00000000, 0.00000000],
                      [0.50000000, -0.86602540, 4.89897960],
                      [0.00000000, -1.73205080, 0.00000000]])
    B = reduced_cell(A)
    assert np.allclose(B.niggli, np.transpose([[1., 0., 0.],
                                               [0., -1.7320508, 0.],
                                               [-0.5, 0.8660254, -4.8989796]]))

    #9
    A = np.transpose([[0.00000000, -1.73205080, 1.63299320],
                      [0.50000000, 2.59807620, 3.26598640],
                      [1.00000000, 0.00000000, 0.00000000]])
    B = reduced_cell(A)
    assert np.allclose(B.niggli, np.transpose([[-1., 0., 0.],
                                               [0., 1.7320508, -1.6329932],
                                               [0.5, 2.5980762, 3.2659864]]))

    #10
    A = np.transpose([[0.5, 0.5, -0.5],
                      [-0.5, 0.5, 0.5],
                      [1.0, 0.0, 1.0]])
    B = reduced_cell(A)
    assert np.allclose(B.niggli, np.transpose([[0.5, 0.5, -0.5],
                                               [-0.5, 0.5, 0.5],
                                               [1., 0., 1.]]))

    #11
    A = np.transpose([[1.00000000, 0.00000000, 0.00000000],
                      [0.00000000, 0.00000000, 1.00000000],
                      [0.50000000, -1.50000000, 0.50000000]])
    B = reduced_cell(A)
    assert np.allclose(B.niggli, np.transpose([[-1., 0., 0.],
                                               [0., 0., -1.],
                                               [0.5, -1.5, 0.5]]))

    #12
    A = np.transpose([[.05, 2.7, 3.3],
                      [0.1, 0.7, 4.5],
                      [.99, .3, 5.4]])
    B = reduced_cell(A)
    assert np.allclose(B.niggli, np.transpose([[-0.89,  0.4 , -0.9 ],
                                               [-0.84, -1.6 ,  0.3 ],
                                               [-1.68,  1.5 ,  2.7 ]]))

    #13
    A = np.transpose([[1, -.1, 0],
                      [-0.3, 1, .3],
                      [-.3, -0.1, -1.5 ]])
    B = reduced_cell(A)
    assert np.allclose(B.niggli, np.transpose([[-1., 0.1, 0.],
                                               [0.3, -1., -0.3],
                                               [0.4, 0.8, -1.2]]))
    
    with pytest.raises(ValueError):
        reduced_cell([[0,0,0],[0,0,0],[0,0,0]])
    with pytest.raises(ValueError):
        reduced_cell([0,0,0])
    with pytest.raises(ValueError):
        reduced_cell([[2,2,2],[1,1,1]])

def test_swap():

    A = np.array([[1,0,0],[0,1,0],[0,0,1]])

    B = reduced_cell(A)

    a1 = 10
    a2 = 20

    b1, b2 = B._swap(a1,a2)
    assert b1==a2
    assert b2==a1

def test_findC3():
    
    A = np.array([[1,0,0],[0,1,0],[0,0,1]])

    B = reduced_cell(A,eps=1E-7)

    C = B._find_C3(-1,-1,-1)
    assert np.allclose(C,np.array([[-1,0,0],[0,-1,0],[0,0,-1]]))

    C = B._find_C3(1,1,1)
    assert np.allclose(C,np.array([[1,0,0],[0,1,0],[0,0,1]]))

def test_findC4():
    
    A = np.array([[1,0,0],[0,1,0],[0,0,1]])

    B = reduced_cell(A)

    C = B._find_C4(-1,-1,-1)
    assert np.allclose(C,np.array([[1,0,0],[0,1,0],[0,0,1]]))

    C = B._find_C4(0,0,1)
    assert np.allclose(C,np.array([[1,0,0],[0,-1,0],[0,0,-1]]))
    
    C = B._find_C4(1,-1,0)
    assert np.allclose(C,np.array([[-1,0,0],[0,1,0],[0,0,-1]]))
    
    C = B._find_C4(0,1,-1)
    assert np.allclose(C,np.array([[-1,0,0],[0,-1,0],[0,0,1]]))
