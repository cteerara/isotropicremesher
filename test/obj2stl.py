import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import copy
import time

# ------------------------------------------------------- #

import meshio


mesh = meshio.read(sys.argv[1])

mesh.write(sys.argv[1].split('.')[0]+'.stl')
