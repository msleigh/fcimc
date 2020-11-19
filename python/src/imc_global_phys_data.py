"""Global physics data."""

# Physical constants
# ------------------

# Speed of light
c = 3.0e10  # cm.s^-1

# Planck constant
h = 4.1356675e-18  # KeV.s

pi = 3.14159265359

# Derived constants
# -----------------

invc = 1.0 / c
invh = 1.0 / h
invh3 = 1.0 / h ** 3
x15pi4 = 15.0 / pi ** 4

# Stefan-Boltzmann constant
# (with the k^4 missing since this is folded into the temp variable)
sb = 2.0 * pi ** 5 / (15.0 * h ** 3 * c ** 2)  # keV^-3.cm^-2.s^-1 (flux-like)

# Radiation constant
a = 4.0 * sb / c  # keV^-3.cm^-3      (density-like)
