"""
TODO:
- Bayesian distance estimator
- P(pi, pi_t) generator code
"""


#dependencies
import os
import csv
import math
import statistics
import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
from astropy import coordinates as coords
from astroquery.gaia import Gaia

from astroquery.vizier import Vizier
from csv import writer

#data locations; replace with coordinates of LC DAT directory and metadata txt file, respectively
#outputdir = os.path.expanduser(r"~/starplot/BLG_data_processing/PROCESSED")
BLGLCdir = os.path.expanduser(r"/Users/fl4mx/OGLE-IV/BLG/BLG_IV_Photometry/I")
stardata = os.path.expanduser(r"~/OGLE-IV/BLG/BLG_IV_metadata.txt")
lastsortedloc = os.path.expanduser(r"~/OGLE-IV/processed.txt")
distancemagnitudefile = os.path.expanduser(r"~/OGLE-IV/d-m.csv")
#debugloc = os.path.expanduser(r"~/starplot/BLG_data_processing/OGLE-ATLAS-RR-c/debug.txt")
#matrixbuglog = os.path.expanduser(r"~/starplot/BLG_data_processing/OGLE-ATLAS-RR-c/matrixbug.txt")

#get file directory
LCfilelist = sorted(os.listdir((BLGLCdir)))
LCfilelength = len(LCfilelist)


#reading all star data from DAT file (names and periods for wave fitting, RA and dec for Gaia query)
names = np.loadtxt(stardata, dtype=str, skiprows=7, usecols=0)
ibands = np.loadtxt(stardata, dtype=float, skiprows=7, usecols=5)
periods = np.loadtxt(stardata, dtype=float, skiprows=7, usecols=8)
fallbackRA = np.loadtxt(stardata, dtype=str, skiprows = 7, usecols=2)
allRA = np.loadtxt(stardata, dtype=str, skiprows = 7, usecols=3)
alldec = np.loadtxt(stardata, dtype=str, skiprows = 7, usecols=4)

#lastsaved
lastsorted = open(lastsortedloc, "r")
laststar = int(lastsorted.read())
lastsorted.close()




# implementing method of querying Gaia data for the parallax, parallax error of the star
def gaiaquery(starnumber, fallbackRA, allRA, alldec):
    verif = True

    #reading coords of the star
    RA = allRA[starnumber]
    #formatting issue in metadata, where they lose a column and dec is read as RA
    if (float(RA.split(":")[0]) < 0.0):
        print("metadata formatting issue, using fallback RA")
        dec = RA
        RA = fallbackRA[starnumber]
    #formatting issue in metadata, where they lose a column and dec is read as RA
    if (float(RA.split(":")[0]) < 0.0):
        print("metadata formatting issue, using fallback RA")
        dec = RA
        RA = fallbackRA[starnumber]
    else:
        dec = alldec[starnumber]

    #print(RA)
    #print(dec)

    #setting up coords query, height and width search precision
    coord = coords.SkyCoord(ra = RA, dec = dec, unit = (u.hourangle, u.deg), frame = "icrs")
    height = u.Quantity(1, u.arcsec)
    width = u.Quantity(1, u.arcsec)

    #query
    star = Gaia.query_object(coordinate=coord, width=width, height=height, columns=["ref_epoch, parallax, parallax_error"])
    #star is a table
    #print("star:")
    #print(star)

    #print(star["parallax"])
    #print(star["parallax_error"])
    #print(len(star["parallax"]))

    if ((len(star["parallax"]) == 0) or (len(star["parallax_error"]) == 0)):
        verif = False
        print("nothing in parallax array")
        parallax = 0
    elif (star["parallax"][0] == "--"):
        verif = False
        print("array is --")
        parallax = 0

    #print(star["ref_epoch"])


    #print(star["ref_epoch"][0])
    #print(star["ref_epoch"][-1])

    #ref_epoch = star["ref_epoch"][-1]


    else:
        #keep in mind there is problem with ref epoch. parallax is given at different reference epochs.
        parallax = float(star["parallax"][-1])
        parallax_error = float(star["parallax_error"][-1])
        #print(parallax)
        #print(parallax_error)
        #RA = float(star["ra"][0])
        #print(str(RA))
        #print(str(parallax_error))
        #print(str(parallax))
        frac_par_err = parallax_error / parallax
        if ((parallax < 0) | (parallax_error < 0) | (frac_par_err > 0.2)):
            verif = False


    #return coordinates, parallax
    return (RA, dec, parallax, verif)







#driver to iterate through all the stars, starting from where we last left off
#for countLC in range(laststar, LCfilelength, 1):
for countLC in range(laststar, LCfilelength, 1):
    #specifying the LC data file, without iterating through listdir in outer for loop
    file = LCfilelist[countLC]

    # reading LC data from LC files (dates and brightness)
    #trim initial whitespaces in cases where time starts with 3 digit JD, so there is whitespace before time
    #magnitudes = []
    #with open(LCdir + "/" + file, "rt") as f:
    #    read = csv.reader(f, skipinitialspace = True)
    #    for row in read:
    #        magnitude = float(row[0].split()[1])
    #        magnitudes.append(magnitude)

    #magnitudes = np.array(magnitudes)


    #grabbing relevant star data for current star (name, starting time, period) from DAT file
    name = names[countLC]
    mag = ibands[countLC]
    period = periods[countLC]


    #simple progress indicator, tells us which star program is up to
    print("\nnow processing " + name)

    #query Gaia for color
    RA, dec, parallax, verif = gaiaquery(countLC, fallbackRA, allRA, alldec)


    if (verif == True):
        print("good")
        distance = 1 / parallax
        print(str(distance))
        print("\n")
        # temp star stats data to write to CSV later
        tempstatsarray = [name, RA, dec, period, mag, distance]
        # star stats for final processing
        with open(distancemagnitudefile, "a+", newline="") as statsfile:
            csv_writer = writer(statsfile)
            csv_writer.writerow(tempstatsarray)



    # distance calculation
    # bailerjones2015, 1/p is incorrect for frac error > 20%
    # if distance = exp(-())



    # autosaver and resume
    lastsorted = open(lastsortedloc, "w")
    lastsorted.write(str(countLC + 1))
    lastsorted.close()