from warnings import warn
import scipy.integrate as sp
from typing import Tuple
import numpy as np


import astropy.units as u
from plasmapy.utils.decorators import validate_quantities
from typing import Tuple

@validate_quantities
def hooks_force(displacement: u.Quantity[u.m], spring_constant: u.Quantity[u.N/u.m]) -> u.Quantity[u.N]:
    return -displacement*spring_constant