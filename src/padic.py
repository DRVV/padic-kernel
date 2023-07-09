import numpy as np

def valuation(n, p=2):
    """
    calculate p-adic valuation
    """
    assert n >= 0

    if n == 0:
        return np.infty
    else:
        reminder = 0
        division_count = -1
        division_target = n
        while reminder == 0:
            # update reminder
            reminder = division_target % p
            # update target
            division_target = division_target // p

            division_count += 1

        return division_count