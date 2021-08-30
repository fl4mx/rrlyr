#dependencies
import os
import numpy as np
import math
import matplotlib.pyplot as plt
from csv import writer
from csv import reader

#data locations; replace with coordinates of LC DAT directory and metadata txt file, respectively
bailerjones = os.path.expanduser(r"~/OGLE-IV/bailerjones.csv")
bailerjonesdupfile = os.path.expanduser(r"~/OGLE-IV/bailerjonesdedup.csv")

meta = os.path.expanduser(r"~/OGLE-IV/LMC/LMC_IV_metadata.txt")
cleanfile = os.path.expanduser(r"~/OGLE-IV/SMC/cleanfile.csv")

metatype = os.path.expanduser(r"~/OGLE-IV/LMC/LMC_IV_metadata.txt")

typefile = os.path.expanduser(r"~/OGLE-IV/SMC/types.txt")
#types = np.loadtxt(typefile, dtype = "str", delimiter = ",", usecols = 1)
#mergefile = cleanfile
mergefile = os.path.expanduser(r"~/OGLE-IV/SMC/cleanfiletypemerge.csv")
abfile = os.path.expanduser(r"~/OGLE-IV/SMC/RRab_dist.csv")
cfile = os.path.expanduser(r"~/OGLE-IV/SMC/RRc_dist.csv")
dfile = os.path.expanduser(r"~/OGLE-IV/SMC/RRd_dist.csv")

#reading all star data from DAT file (names and periods for wave fitting, RA and dec for Gaia query)
names = np.loadtxt(meta, dtype="str", skiprows=7, usecols=0)
periods = np.loadtxt(meta, skiprows=7, usecols=8)
allRA = np.loadtxt(meta, dtype = "str", skiprows = 7, usecols = 3)
alldec = np.loadtxt(meta, dtype = "str", skiprows = 7, usecols = 4)
imag = np.loadtxt(meta, dtype = "str", skiprows = 7, usecols = 5)



def fileclean(names, allRA, alldec, periods, imag, cleanfile):
    length = len(names)
    for x in range(0, length, 1):
        temparr = [names[x], allRA[x], alldec[x], periods[x], imag[x]]
        with open(cleanfile, "a+", newline="") as statsfile:
            csv_writer = writer(statsfile)
            csv_writer.writerow(temparr)

def typeextract(metatype, typefile):
    names = np.loadtxt(metatype, dtype="str", skiprows=7, usecols=0)
    types = np.loadtxt(metatype, dtype="str", skiprows=7, usecols=2)
    length = len(names)
    for x in range(0, length, 1):
        temparr = [names[x], types[x]]
        with open(typefile, "a+", newline="") as statsfile:
            csv_writer = writer(statsfile)
            csv_writer.writerow(temparr)

def mergededup(mergefile):
    rows = open(mergefile).read().split('\n')
    newrows = []
    for row in rows:
        rowsplit = row.split(",")
        if rowsplit[0] not in [items[0] for items in newrows]:
            newrows.append(row)
    f = open(mergefile, 'w')
    f.write('\n'.join(newrows))
    f.close()

def bailerjonesdedup(bailerjones, bailerjonesdupfile):
    rows = open(bailerjones).read().split('\n')
    newrows = []
    for row in rows:
        if row not in newrows:
            newrows.append(row)
    f = open(bailerjonesdupfile, 'w')
    f.write('\n'.join(newrows))
    f.close()

def mergetypesplit(mergefile, abfile, cfile, dfile):
    with open(mergefile, 'r') as read:
        csv_reader = reader(read)
        for row in csv_reader:
            if (row[-1] == "RRab"):
                with open(abfile, "a+", newline="") as writefile:
                    csv_writer = writer(writefile)
                    csv_writer.writerow(row)
            if (row[-1] == "RRc"):
                with open(cfile, "a+", newline="") as writefile:
                    csv_writer = writer(writefile)
                    csv_writer.writerow(row)
            if (row[-1] == "RRd"):
                with open(dfile, "a+", newline="") as writefile:
                    csv_writer = writer(writefile)
                    csv_writer.writerow(row)

def typemerge(cleanfile, typefile, mergefile):
    types = np.loadtxt(typefile, dtype="str", delimiter = ",", usecols=1)
    with open(cleanfile, 'r') as fileread:
        csv_reader = reader(fileread)
        for x, row in enumerate(csv_reader):
            row.append(types[x])
            with open(mergefile, "a+", newline="") as writefile:
                csv_writer = writer(writefile)
                csv_writer.writerow(row)


#choose which functions to run

#fileclean(names, allRA, alldec, periods, imag, cleanfile)
#mergededup(mergefile)
#bailerjonesdedup(bailerjones, bailerjonesdupfile)
mergetypesplit(mergefile, abfile, cfile, dfile)
#typeextract(metatype, typefile)
#typemerge(cleanfile, typefile, mergefile)
