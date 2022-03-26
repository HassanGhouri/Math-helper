from equations import *

def testsolve_eqnD():

    assert solve_eqnD("5x + 2 = 1") == (-1, 5)

    assert solve_eqnD("-12x - 6 = -4") == (-1, 6)

    assert solve_eqnD("4x + 2 = 10") == (2,1)

    # edge cases

    assert solve_eqnD("0x + 0 = 0") == (0, 0)

    assert solve_eqnD("7x + 9 = 9") == (0,1)

    assert solve_eqnD("6x + 0 = 0") == (0, 1)

    assert solve_eqnD("0x + 6 = 0") == ("No Solution")

    assert solve_eqnD("0x + 0 = 7") == ("No Solution")


if __name__ == "__main__":
 testsolve_eqnD()
