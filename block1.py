#!/usr/bin/python

import numpy as np
from astropy.io import fits

fits = fits.open('/Users/Brian/Work/scicoder/ssppOut-dr9.fits', memmap=True)
header = fits[1].header
data = fits[1].data

#columns we want  TEFF_ADOP, LOGG_ADOP, FEH_APOD

teff = data.field('TEFF_ADOP')
logg = data.field('LOGG_ADOP')
feh = data.field('FEH_ADOP')

good,=np.where((teff != -9999) & (logg != -9999 ) & (feh != -9999))

teff_good = teff[good]
logg_good = logg[good]
feh_good = feh[good]

#SPECTYPE

st_hammer = data.field('SPECTYPE_HAMMER')[good]
st_subclass = data.field('SPECTYPE_SUBCLASS')[good]






