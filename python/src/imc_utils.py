"""Utility functions for IMC."""

import math
import random as ran

import imc_global_phys_data as phys


def sample_planck_spectrum():
    """Create samples from the Planck spectrum."""
    nnn = 1.0
    rn1 = ran.random()
    tmpsum = 1.0
    while True:
        if rn1 <= 90.0 * tmpsum / phys.pi ** 4:
            rn1 = ran.random()
            rn2 = ran.random()
            rn3 = ran.random()
            rn4 = ran.random()
            xxx = -math.log(rn1 * rn2 * rn3 * rn4) / nnn
            break
        nnn += 1.0
        tmpsum += 1.0 / nnn ** 4

    return xxx
