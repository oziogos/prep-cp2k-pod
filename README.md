# prep-cp2k-pod

A python interface (using a jupyter notebook for evaluation) for generating input files for charge transfer integral calculations by means of the Projector Operator-Based Diabatization (POD) approach via the CP2K code.

Dictionary entries in data/config.py and data/blocks.py control input parameters such as:
- dimer coordinates
- level of theory (basis set, XC functionals etc)

Selected dimer configurations are stored in data/dimers
