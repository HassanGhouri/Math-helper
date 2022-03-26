from equations import *
    
def testsolve_eqnA():

    assert solve_eqnA("x + 4 = 1") == (-3,1)

    assert solve_eqnA("x - 6 = -7") == (-1,1)

    assert solve_eqnA("x + 9 = -3") == (-12,1)

    assert solve_eqnA("x - 8 = 2") == (10,1)

    #edge Cases

    assert solve_eqnA("x + 0 = 0") == (0,1)

    assert solve_eqnA("x + 0 = 7") == (7,1)
    
    assert solve_eqnA("x + 7 = 0") == (-7,1)


if __name__ == "__main__":
 testsolve_eqnA()
