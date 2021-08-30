#dependencies
import os
import numpy as np
import math
import matplotlib.pyplot as plt
from csv import writer

#data locations; replace with coordinates of LC DAT directory and metadata txt file, respectively
dmfile = os.path.expanduser(r"~/OGLE-IV/d-m.csv")
cleanfile = os.path.expanduser(r"~/OGLE-IV/d-m_cleaned.csv")
outputdir = os.path.expanduser(r"~/OGLE-IV/Graphs")

#reading all star data from DAT file (names and periods for wave fitting, RA and dec for Gaia query)
names = np.loadtxt(dmfile, delimiter=",", dtype=str, usecols=0)
allRA = np.loadtxt(dmfile, delimiter=",", dtype=str, usecols=1)
alldec = np.loadtxt(dmfile, delimiter=",", dtype=str, usecols=2)
period = np.loadtxt(dmfile, delimiter=",", dtype=float, usecols=3)
apparentmag = np.loadtxt(dmfile, delimiter=",", dtype=float, usecols=4)
distancekpc = np.loadtxt(dmfile, delimiter=",", dtype=str, usecols=5)



def fileclean(names, allRA, alldec, period, apparentmag, distancekpc, cleanfile):
    nan_index = np.where(distancekpc == "nan")
    names = np.delete(names, nan_index)
    allRA = np.delete(allRA, nan_index)
    alldec = np.delete(alldec, nan_index)
    period = np.delete(period, nan_index)
    apparentmag = np.delete(apparentmag, nan_index)
    distancekpc = np.delete(distancekpc, nan_index)
    length = len(names)

    for x in range(0, length, 1):
        temparr = [names[x], allRA[x], alldec[x], period[x], apparentmag[x], distancekpc[x]]
        with open(cleanfile, "a+", newline="") as statsfile:
            csv_writer = writer(statsfile)
            csv_writer.writerow(temparr)



def pMscatter(p, M, plotname):
    fig = plt.figure(figsize=(10, 5))
    fig.suptitle(plotname, fontsize=20, fontweight='bold', y=0.96)
    ax = fig.add_subplot(111)
    fig.subplots_adjust(left=0.1, right=0.98, top=0.87, bottom=0.1)
    ax.set_xlabel("Period")
    ax.set_ylabel("Absolute Magnitude")
    ax.invert_yaxis()
    ax.scatter(p, M, s=0.2, color="#332288")
    #plt.show
    plt.savefig((outputdir + "/" + (plotname) + ".png"), format="png", dpi=1200)



def pl_plot(cleanfile):
    period = np.loadtxt(cleanfile, delimiter=",", dtype=float, usecols=3)
    apparentmag = np.loadtxt(cleanfile, delimiter=",", dtype=float, usecols=4)
    distancekpc = np.loadtxt(cleanfile, delimiter=",", dtype=float, usecols=5)
    length = len(period)
    p = []
    M = []
    for x in range(0, length, 1):
        pe = period[x]
        mi = apparentmag[x]
        d = distancekpc[x] * 1000
        #Mi = mi - (5 * math.log(d)) + 5
        Mi = mi - (5 * math.log(d/10))
        p.append(pe)
        M.append(Mi)


    pMscatter(p, M, "Period vs Absolute Magnitude in BLG")


fileclean(names, allRA, alldec, period, apparentmag, distancekpc, cleanfile)
pl_plot(cleanfile)