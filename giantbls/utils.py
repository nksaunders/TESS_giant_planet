import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams["savefig.dpi"] = 300
import scipy.ndimage

def get_cvz_targets():
    path = os.path.abspath(os.path.join('data', 'TICgiants_CVZ.csv'))
    return pd.read_csv(path, skiprows=4)
