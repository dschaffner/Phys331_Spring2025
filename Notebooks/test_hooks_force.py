import pytest
import numpy as np
import astropy.units as u
from hooks_force import hooks_force

@pytest.mark.parametrize(
        ("args", "expected"),
        [((0.2*u.m,100*u.N/u.m),-20*u.N),
         ((0.1*u.m,100*u.N/u.m),-10*u.N)])
def test_hooks_force(args,expected) -> None:
    assert np.isclose(hooks_force(*args), expected)