#! /usr/bin/env python3
#shebang required for executing a file directly from a terminal using only ./filename.py instead of python3 filename.py

# Remember to change directory (CD) to the folder where this file is stored before running.

from sys import path
path.append('../packages/Extrapack ZIP file.zip') # Navigates back up to the 'Module 1' folder, then into packages.

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import FunI
from extra.good.beta import FunB

print(sig.FunS())
print(alp.FunA())
print(FunI())
print(FunB())
