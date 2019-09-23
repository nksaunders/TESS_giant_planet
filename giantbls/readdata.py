import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams["savefig.dpi"] = 300
import scipy.ndimage

import eleanor
import astropy.stats as ass

from utils import get_cvz_targets

def from_eleanor(ticid):
    star = eleanor.Source(tic=ticid, sector=2, tc=True) #note: update to get all Sectors
    print('data found! for: ', ticid)
    data = eleanor.TargetData(star, height=15, width=15, bkg_size=31, do_psf=True, do_pca=True, try_load=True)
    return data

def from_lightkurve(ticid):
    star = lk.search_targetpixelfile('tic{int}'.format(ticid))[0].download()
    
