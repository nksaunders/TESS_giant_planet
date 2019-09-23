import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams["savefig.dpi"] = 300
import scipy.ndimage

import eleanor
import astropy.stats as ass

from utils import get_cvz_targets
from readdata import from_eleanor

cvz = get_cvz_targets()
brightcvz = cvz.GAIAmag < 6.5

print(f'Using the brightest {len(cvz[brightcvz])} targets.')

def perday_to_uHz(freq_perday):
    return freq_perday/24/3600 * 1e6

def uHz_to_perday(freq_uHz):
    return (freq_uHz * 1e-6)*24*3600

freq = np.linspace(1./15, 1./.01, 100000)
ps = 1./freq

data = []

i = 3
from_eleanor(ticid=cvz[brightcvz].ID.values[i])
from_lightkurve(ticid=cvz[brightcvz].ID.values[i])
