from equations import *

def testsolve_eqnE():

    assert solve_eqnE("x/6 + 1 = 7") == (36, 1)

    assert solve_eqnE("x/-2 - 8 = -10") == (4,1)

    assert solve_eqnE("x/9 - 6 = -3") == (27, 1)

    assert solve_eqnE("x/5 - 1 = 4") == (25, 1)

    assert solve_eqnE("x/-5 - 1 = 4") == (-25, 1)

    

    

    # edge cases

    assert solve_eqnE("x/0 + 0 = 0") == (0, 0)

    assert solve_eqnE("x/7 + 9 = 9") == (0, 0)

    assert solve_eqnE("x/6 + 0 = 0") == (0, 1)

    assert solve_eqnE("x/0 + 6 = 0") == (0, 0)

    assert solve_eqnE("x/0 + 0 = 7") == (0, 0)


if __name__ == "__main__":
 testsolve_eqnE()
