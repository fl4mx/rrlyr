# dependencies
import os
import numpy as np
import matplotlib.pyplot as plt
# data locations
All_metadata = os.path.expanduser(r"~/OGLE-IV/All/IV_metadata.txt")
All_I_LCdir = os.path.expanduser(r"~/OGLE-IV/All/IV_Photometry/I")
All_V_LCdir = os.path.expanduser(r"~/OGLE-IV/All/IV_Photometry/V")
BLG_metadata = os.path.expanduser(r"~/OGLE-IV/BLG/BLG_IV_metadata.txt")
BLG_I_LCdir = os.path.expanduser(r"~/OGLE-IV/BLG/BLG_IV_Photometry/I")
BLG_V_LCdir = os.path.expanduser(r"~/OGLE-IV/BLG/BLG_IV_Photometry/V")
LMC_metadata = os.path.expanduser(r"~/OGLE-IV/LMC/LMC_IV_metadata.txt")
LMC_I_LCdir = os.path.expanduser(r"~/OGLE-IV/LMC/LMC_IV_Photometry/I")
LMC_V_LCdir = os.path.expanduser(r"~/OGLE-IV/LMC/LMC_IV_Photometry/V")
SMC_metadata = os.path.expanduser(r"~/OGLE-IV/SMC/SMC_IV_metadata.txt")
SMC_I_LCdir = os.path.expanduser(r"~/OGLE-IV/SMC/SMC_IV_Photometry/I")
SMC_V_LCdir = os.path.expanduser(r"~/OGLE-IV/SMC/SMC_IV_Photometry/V")
outputdir = os.path.expanduser(r"~/OGLE-IV/Graphs/")



# big mess
def rrlyr_PL(BLG_metadata, LMC_metadata, SMC_metadata):
    # plotter for RRab, RRc, RRd, across different regions
    def typescatterplot(iv, type, xtitle, ytitle, plotname, size):
        fig = plt.figure(figsize=(10, 5))
        fig.suptitle(str(plotname), fontsize=20, fontweight='bold', y=0.96)
        ax = fig.add_subplot(111)
        fig.subplots_adjust(left=0.1, right=0.98, top=0.87, bottom=0.1)
        ax.set_xlabel(xtitle)
        ax.set_ylabel(ytitle)
        ax.invert_yaxis()
        # plot
        if iv == "i":
            if type == "RRab":
                ax.scatter(BLG_RRab[0], BLG_RRab[1], s=size, color="#332288")
                ax.scatter(LMC_RRab[0], LMC_RRab[1], s=size, color="#88CCEE")
                ax.scatter(SMC_RRab[0], SMC_RRab[1], s=size, color="#44AA99")
            if type == "RRc":
                ax.scatter(BLG_RRc[0], BLG_RRc[1], s=size, color="#332288")
                ax.scatter(LMC_RRc[0], LMC_RRc[1], s=size, color="#88CCEE")
                ax.scatter(SMC_RRc[0], SMC_RRc[1], s=size, color="#44AA99")
            if type == "RRd":
                ax.scatter(BLG_RRd[0], BLG_RRd[1], s=size, color="#332288")
                ax.scatter(LMC_RRd[0], LMC_RRd[1], s=size, color="#88CCEE")
                ax.scatter(SMC_RRd[0], SMC_RRd[1], s=size, color="#44AA99")
        elif iv == "v":
            if type == "RRab":
                ax.scatter(BLG_RRab[0], BLG_RRab[2], s=size, color="#332288")
                ax.scatter(LMC_RRab[0], LMC_RRab[2], s=size, color="#88CCEE")
                ax.scatter(SMC_RRab[0], SMC_RRab[2], s=size, color="#44AA99")
            if type == "RRc":
                ax.scatter(BLG_RRc[0], BLG_RRc[2], s=size, color="#332288")
                ax.scatter(LMC_RRc[0], LMC_RRc[2], s=size, color="#88CCEE")
                ax.scatter(SMC_RRc[0], SMC_RRc[2], s=size, color="#44AA99")
            if type == "RRd":
                ax.scatter(BLG_RRd[0], BLG_RRd[2], s=size, color="#332288")
                ax.scatter(LMC_RRd[0], LMC_RRd[2], s=size, color="#88CCEE")
                ax.scatter(SMC_RRd[0], SMC_RRd[2], s=size, color="#44AA99")
        ax.legend(["BLG", "LMC", "SMC"], markerscale=8)
        plt.show
        plt.savefig((outputdir + "/" + (plotname) + ".png"), format="png", dpi=1200)

    # plotter for BLG, LMC, SMC
    def regionscatterplot(iv, region, xtitle, ytitle, plotname, size):
        fig = plt.figure(figsize=(10, 5))
        fig.suptitle(str(plotname), fontsize=20, fontweight='bold', y=0.96)
        ax = fig.add_subplot(111)
        fig.subplots_adjust(left=0.1, right=0.98, top=0.87, bottom=0.1)
        ax.set_xlabel(xtitle)
        ax.set_ylabel(ytitle)
        ax.invert_yaxis()
        # plot
        if iv == "i":
            if region == "BLG":
                ax.scatter(BLG_RRab[0], BLG_RRab[1], s=size, color="#332288")
                ax.scatter(BLG_RRc[0], BLG_RRc[1], s=size, color="#88CCEE")
                ax.scatter(BLG_RRd[0], BLG_RRd[1], s=size, color="#44AA99")
            if region == "LMC":
                ax.scatter(LMC_RRab[0], LMC_RRab[1], s=size, color="#332288")
                ax.scatter(LMC_RRc[0], LMC_RRc[1], s=size, color="#88CCEE")
                ax.scatter(LMC_RRd[0], LMC_RRd[1], s=size, color="#44AA99")
            if region == "SMC":
                ax.scatter(SMC_RRab[0], SMC_RRab[1], s=size, color="#332288")
                ax.scatter(SMC_RRc[0], SMC_RRc[1], s=size, color="#88CCEE")
                ax.scatter(SMC_RRd[0], SMC_RRd[1], s=size, color="#44AA99")
        elif iv == "v":
            if region == "BLG":
                ax.scatter(BLG_RRab[0], BLG_RRab[2], s=size, color="#332288")
                ax.scatter(BLG_RRc[0], BLG_RRc[2], s=size, color="#88CCEE")
                ax.scatter(BLG_RRd[0], BLG_RRd[2], s=size, color="#44AA99")
            if region == "LMC":
                ax.scatter(LMC_RRab[0], LMC_RRab[2], s=size, color="#332288")
                ax.scatter(LMC_RRc[0], LMC_RRc[2], s=size, color="#88CCEE")
                ax.scatter(LMC_RRd[0], LMC_RRd[2], s=size, color="#44AA99")
            if region == "SMC":
                ax.scatter(SMC_RRab[0], SMC_RRab[2], s=size, color="#332288")
                ax.scatter(SMC_RRc[0], SMC_RRc[2], s=size, color="#88CCEE")
                ax.scatter(SMC_RRd[0], SMC_RRd[2], s=size, color="#44AA99")
        ax.legend(["RRab", "RRc", "RRd"], markerscale=8)
        plt.show
        plt.savefig((outputdir + "/" + (plotname) + ".png"), format="png", dpi=1200)

    # plotter for all 9 types
    def allscatterplot(iv, xtitle, ytitle, plotname, size):
        fig = plt.figure(figsize=(10, 5))
        fig.suptitle(str(plotname), fontsize=20, fontweight='bold', y=0.96)
        ax = fig.add_subplot(111)
        fig.subplots_adjust(left=0.1, right=0.98, top=0.87, bottom=0.1)
        ax.set_xlabel(xtitle)
        ax.set_ylabel(ytitle)
        ax.invert_yaxis()
        # plot
        if iv == "i":
            ax.scatter(BLG_RRab[0], BLG_RRab[1], s=size, color="#332288")
            ax.scatter(LMC_RRab[0], LMC_RRab[1], s=size, color="#88CCEE")
            ax.scatter(SMC_RRab[0], SMC_RRab[1], s=size, color="#44AA99")
            ax.scatter(BLG_RRc[0], BLG_RRc[1], s=size, color="#117733")
            ax.scatter(LMC_RRc[0], LMC_RRc[1], s=size, color="#999933")
            ax.scatter(SMC_RRc[0], SMC_RRc[1], s=size, color="#DDCC77")
            ax.scatter(BLG_RRd[0], BLG_RRd[1], s=size, color="#CC6677")
            ax.scatter(LMC_RRd[0], LMC_RRd[1], s=size, color="#882255")
            ax.scatter(SMC_RRd[0], SMC_RRd[1], s=size, color="#AA4499")
        if iv == "v":
            ax.scatter(BLG_RRab[0], BLG_RRab[2], s=size, color="#332288")
            ax.scatter(LMC_RRab[0], LMC_RRab[2], s=size, color="#88CCEE")
            ax.scatter(SMC_RRab[0], SMC_RRab[2], s=size, color="#44AA99")
            ax.scatter(BLG_RRc[0], BLG_RRc[2], s=size, color="#117733")
            ax.scatter(LMC_RRc[0], LMC_RRc[2], s=size, color="#999933")
            ax.scatter(SMC_RRc[0], SMC_RRc[2], s=size, color="#DDCC77")
            ax.scatter(BLG_RRd[0], BLG_RRd[2], s=size, color="#CC6677")
            ax.scatter(LMC_RRd[0], LMC_RRd[2], s=size, color="#882255")
            ax.scatter(SMC_RRd[0], SMC_RRd[2], s=size, color="#AA4499")
        ax.legend(["BLGRRab", "LMCRRab", "SMCRRab", "BLGRRc", "LMCRRc", "SMCRRc", "BLGRRd", "LMCRRd", "SMCRRd"], markerscale=8)
        plt.show
        plt.savefig((outputdir + "/" + (plotname) + ".png"), format="png", dpi=1200)



    # reading columns of BLG, LMC, SMC
    BLG_subtypes = np.loadtxt(BLG_metadata, usecols=(2), skiprows=7, dtype=str)
    BLG_ibands = np.loadtxt(BLG_metadata, usecols=(5), skiprows=7, dtype=float)
    BLG_vbands = np.loadtxt(BLG_metadata, usecols=(6), skiprows=7, dtype=float)
    BLG_vbands = np.ma.masked_equal(BLG_vbands, -99.99)
    BLG_periods = np.loadtxt(BLG_metadata, usecols=(8), skiprows=7, dtype=float)
    LMC_subtypes = np.loadtxt(LMC_metadata, usecols=(2), skiprows=7, dtype=str)
    LMC_ibands = np.loadtxt(LMC_metadata, usecols=(5), skiprows=7, dtype=float)
    LMC_vbands = np.loadtxt(LMC_metadata, usecols=(6), skiprows=7, dtype=float)
    LMC_vbands = np.ma.masked_equal(LMC_vbands, -99.99)
    LMC_periods = np.loadtxt(LMC_metadata, usecols=(8), skiprows=7, dtype=float)
    SMC_subtypes = np.loadtxt(SMC_metadata, usecols=(2), skiprows=7, dtype=str)
    SMC_ibands = np.loadtxt(SMC_metadata, usecols=(5), skiprows=7, dtype=float)
    SMC_vbands = np.loadtxt(SMC_metadata, usecols=(6), skiprows=7, dtype=float)
    SMC_vbands = np.ma.masked_equal(SMC_vbands, -99.99)
    SMC_periods = np.loadtxt(SMC_metadata, usecols=(8), skiprows=7, dtype=float)

    # [[periods], [imag], [vmag]]
    BLG_RRab = [[], [], []]
    BLG_RRc = [[], [], []]
    BLG_RRd = [[], [], []]
    LMC_RRab = [[], [], []]
    LMC_RRc = [[], [], []]
    LMC_RRd = [[], [], []]
    SMC_RRab = [[], [], []]
    SMC_RRc = [[], [], []]
    SMC_RRd = [[], [], []]

    # potentially can put into [[blg], [lmc], [smc]] where each region has [[periods], [imag], [vmag]]
    # RRab = [[[], [], []], [[], [], []], [[], [], []]]
    # RRc = [[[], [], []], [[], [], []], [[], [], []]]
    # RRd = [[[], [], []], [[], [], []], [[], [], []]]

    # dumb workaround without using 3d array
    for count, subtype in enumerate(BLG_subtypes):
        startemp = [[BLG_periods[count]], [BLG_ibands[count]], [BLG_vbands[count]]]
        # count from 0
        if subtype == "RRab":
            BLG_RRab = np.append(BLG_RRab, startemp, axis=1)
        elif subtype == "RRc":
            BLG_RRc = np.append(BLG_RRc, startemp, axis=1)
        elif subtype == "RRd":
            BLG_RRd = np.append(BLG_RRd, startemp, axis=1)
    for count, subtype in enumerate(LMC_subtypes):
        startemp = [[LMC_periods[count]], [LMC_ibands[count]], [LMC_vbands[count]]]
        # count from 0
        if subtype == "RRab":
            LMC_RRab = np.append(LMC_RRab, startemp, axis=1)
        elif subtype == "RRc":
            LMC_RRc = np.append(LMC_RRc, startemp, axis=1)
        elif subtype == "RRd":
            LMC_RRd = np.append(LMC_RRd, startemp, axis=1)
    for count, subtype in enumerate(SMC_subtypes):
        startemp = [[SMC_periods[count]], [SMC_ibands[count]], [SMC_vbands[count]]]
        # count from 0
        if subtype == "RRab":
            SMC_RRab = np.append(SMC_RRab, startemp, axis=1)
        elif subtype == "RRc":
            SMC_RRc = np.append(SMC_RRc, startemp, axis=1)
        elif subtype == "RRd":
            SMC_RRd = np.append(SMC_RRd, startemp, axis=1)

    # np.ma.MaskedArray(RRab, mask=(np.ones_like(RRab) * (RRab[2, :] == -99.99)).T)
    # np.ma.MaskedArray(RRc, mask=(np.ones_like(RRc) * (RRc[2, :] == -99.99)).T)
    # np.ma.MaskedArray(RRd, mask=(np.ones_like(RRd) * (RRd[2, :] == -99.99)).T)

    # allstars = [[], [], []]
    # allstars = np.append(allstars, RRab, axis=1)
    # allstars = np.append(allstars, RRc, axis=1)
    # allstars = np.append(allstars, RRd, axis=1)



    typescatterplot("i", "RRab", "Period", "I-Band Magnitude", "Period vs I-Band Magnitude for all RRab", 0.2)
    typescatterplot("i", "RRc", "Period", "I-Band Magnitude", "Period vs I-Band Magnitude for all RRc", 0.2)
    typescatterplot("i", "RRd", "Period", "I-Band Magnitude", "Period vs I-Band Magnitude for all RRd", 0.2)
    typescatterplot("v", "RRab", "Period", "I-Band Magnitude", "Period vs V-Band Magnitude for all RRab", 0.2)
    typescatterplot("v", "RRc", "Period", "I-Band Magnitude", "Period vs V-Band Magnitude for all RRc", 0.2)
    typescatterplot("v", "RRd", "Period", "I-Band Magnitude", "Period vs V-Band Magnitude for all RRd", 0.2)

    regionscatterplot("i", "BLG", "Period", "I-Band Magnitude", "Period vs I-Band Magnitude in BLG", 0.2)
    regionscatterplot("i", "LMC", "Period", "I-Band Magnitude", "Period vs I-Band Magnitude in LMC", 0.2)
    regionscatterplot("i", "SMC", "Period", "I-Band Magnitude", "Period vs I-Band Magnitude in SMC", 0.2)
    regionscatterplot("v", "BLG", "Period", "V-Band Magnitude", "Period vs V-Band Magnitude in BLG", 0.2)
    regionscatterplot("v", "LMC", "Period", "V-Band Magnitude", "Period vs V-Band Magnitude in LMC", 0.2)
    regionscatterplot("v", "SMC", "Period", "V-Band Magnitude", "Period vs V-Band Magnitude in SMC", 0.2)

    allscatterplot("i", "Period", "I-Band Magnitude", "Period vs I-Band Magnitude for all RR Lyrae", 0.2)
    allscatterplot("v", "Period", "V-Band Magnitude", "Period vs V-Band Magnitude for all RR Lyrae", 0.2)


rrlyr_PL(BLG_metadata, LMC_metadata, SMC_metadata)
