#dependencies
import os
import csv
import math
import statistics
import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
from astropy import coordinates as coord
from astroquery.vizier import Vizier
from csv import writer


#data locations; replace with coordinates of LC DAT directory and metadata txt file, respectively
#outputdir = os.path.expanduser(r"~/starplot/BLG_data_processing/PROCESSED")
BLGLCdir = os.path.expanduser(r"/Users/fl4mx/OGLE-IV/BLG/BLG_IV_Photometry/I")
stardata = os.path.expanduser(r"~/OGLE-IV/BLG/BLG_IV_metadata.txt")
lastsortedloc = os.path.expanduser(r"~/OGLE-IV/processed.txt")
distancemagnitudefile = os.path.expanduser(r"~/OGLE-IV/bailerjones.csv")


#get file directory
#LCfilelist = sorted(os.listdir((BLGLCdir)))



#reading all star data from DAT file (names and periods for wave fitting, RA and dec for Gaia query)
names = np.loadtxt(stardata, dtype=str, skiprows=7, usecols=0)
ibands = np.loadtxt(stardata, dtype=float, skiprows=7, usecols=5)
periods = np.loadtxt(stardata, dtype=float, skiprows=7, usecols=8)
fallbackRA = np.loadtxt(stardata, dtype=str, skiprows = 7, usecols=2)
allRA = np.loadtxt(stardata, dtype=str, skiprows = 7, usecols=3)
alldec = np.loadtxt(stardata, dtype=str, skiprows = 7, usecols=4)

LCfilelength = len(names)

#lastsaved
lastsorted = open(lastsortedloc, "r")
laststar = int(lastsorted.read())
lastsorted.close()






def gaiaquery(starnumber, fallbackRA, allRA, alldec):
    RA = allRA[starnumber]
    if (float(RA.split(":")[0]) < 0.0):
        print("metadata formatting issue, using fallback RA")
        dec = RA
        RA = fallbackRA[starnumber]
    if (float(RA.split(":")[0]) < 0.0):
        print("metadata formatting issue, using fallback RA")
        dec = RA
        RA = fallbackRA[starnumber]
    else:
        dec = alldec[starnumber]

    column_filters = {}
    row_limit = 9999999
    catalog = 'I/352/gedr3dis'
    v = Vizier(columns=["rgeo"],
               column_filters=column_filters,
               row_limit=row_limit)
    result = v.query_region(coord.SkyCoord(ra=RA, dec=dec,
                                           unit=(u.hourangle, u.deg),
                                           frame='icrs'),
                            radius=0.5 * u.arcsec, catalog=catalog)


    if (len(result) == 0):
        distance = 0
    else:
        distance = result[0]["rgeo"][0]

    print(distance)

    return (RA, dec, distance)






for countLC in range(laststar, LCfilelength, 1):
    #file = LCfilelist[countLC]
    name = names[countLC]
    mag = ibands[countLC]
    period = periods[countLC]

    print("\nnow processing " + name)

    gaiaquery(countLC, fallbackRA, allRA, alldec)
    RA, dec, distance = gaiaquery(countLC, fallbackRA, allRA, alldec)

    tempstatsarray = [name, RA, dec, period, mag, distance]
    with open(distancemagnitudefile, "a+", newline="") as statsfile:
        csv_writer = writer(statsfile)
        csv_writer.writerow(tempstatsarray)

    lastsorted = open(lastsortedloc, "w")
    lastsorted.write(str(countLC + 1))
    lastsorted.close()