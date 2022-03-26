from equations import *

def testsolve_eqnC():

    assert solve_eqnC("x/5 = 10") == (50,1)
    
    assert solve_eqnC("x/-4 = -5") == (20, 1)

    assert solve_eqnC("x/4 = -2") == (-8, 1)

    assert solve_eqnC("x/-18 = 2") == (-36, 1)

    #edge Cases

    assert solve_eqnC("x/0  = 0") == (0,0)

    assert solve_eqnC("x/0 = 1") == (0,0)
    
    assert solve_eqnC("x/3 = 0") == (0,0)


if __name__ == "__main__":
 testsolve_eqnC()

