import pytest
import sys
sys.path.append('../src/')

import numpy as np
from padic import valuation


def test_valuation_of_zero():
    assert valuation(0) == np.inf
    assert valuation(0, 7) == np.inf


def test_valuation_of_prime():
    assert valuation(3) == 0
    assert valuation(5) == 0
    assert valuation(7) == 0
    assert valuation(11) == 0

    assert valuation(89) == 0
    assert valuation(97) == 0


def test_valuation_of_factor():
    assert valuation(2) == 1
    assert valuation(3, 3) == 1
    assert valuation(5, 5) == 1


def test_valuation():
    assert valuation(6) == 1
    assert valuation(8) == 3
    assert valuation(12) == 2


def test_only_allows_integer():
    with pytest.raises(TypeError) as exc_info:
        ret = valuation(1.5)

    if exc_info.type is None:
        pytest.fail(f'returned value is {ret}, but the value should not be expected')