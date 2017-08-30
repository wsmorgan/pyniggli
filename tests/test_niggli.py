import numpy as np
import pytest

from pyniggli.niggli import reduced_cell


def test_reduction():
    """Tests the niggli reduction of some basic cells."""

    A = np.transpose([[1,0,0],[0,1,0],[0,0,2]])
    B = reduced_cell(A)
    assert np.allclose(B.C,np.array([[1,0,0],[0,1,0],[0,0,1]]))
    assert np.allclose(B.niggli,A)
    assert np.allclose(B.niggli,np.dot(A,B.C))

    A = np.transpose([[0.5,0,0.5],[0,3,0],[0.5,0,-0.5]])
    B = reduced_cell(A)
    assert np.allclose(B.niggli,np.transpose([[-0.5,0,-0.5],[-0.5,0,0.5],[0,-3,0]]))
    assert np.allclose(B.niggli,np.dot(A,B.C))

    with pytest.raises(ValueError):
        reduced_cell([[0,0,0],[0,0,0],[0,0,0]])
        reduced_cell([0,0,0])
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

    B = reduced_cell(A)

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
    
