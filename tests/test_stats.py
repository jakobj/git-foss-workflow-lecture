import pytest

import meaningful


def test_mean():
    l = [1.0, 2.0, 3.0]
    result = meaningful.stats.mean(l)
    expected = 2.0
    assert result == pytest.approx(expected)


def test_var():
    l = [1.0, 2.0, 3.0]
    result = meaningful.stats.var(l)
    expected = 0.6666666666666666
    assert result == pytest.approx(expected)
