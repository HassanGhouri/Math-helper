from equations import *

def testsolve_eqnB():

    assert solve_eqnB("5x = 10") == (2,1)

    assert solve_eqnB("-4x = -5") == (5, 4)

    assert solve_eqnB("4x = -2") == (-1, 2)

    assert solve_eqnB("-9x = 1") == (-1,9)

    #edge Cases

    assert solve_eqnB("0x  = 0") == (0,0)

    assert solve_eqnB("0x = 1") == ("No Solution")
    
    assert solve_eqnB("3x = 0") == (0,1)


if __name__ == "__main__":
 testsolve_eqnB()
