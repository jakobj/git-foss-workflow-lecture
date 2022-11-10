import pytest

import meaningful

import numpy as np

def test_mean():
    l = [1.0, 2.0, 3.0]
    result = meaningful.stats.mean(l)
    expected = 2.0
    assert result == pytest.approx(expected)

def test_variance():
    l = [1.0, 2.0, 3.0]
    result = meaningful.stats.variance(l)
    expected = np.var(l)
    assert result == pytest.approx(expected)