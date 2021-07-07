# dependencies
import os
import numpy as np
import matplotlib.pyplot as plt

# data locations; replace with coordinates of LC DAT directory and metadata txt file, respectively
# statsfile = os.path.expanduser(r"~/starplot/DataAnalysis/stats.csv")
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


# functions
def deviationvscolor(statsfile):
    # loadtxt read into numpy ndarrays
    deviations = np.loadtxt(statsfile, skiprows=0, delimiter=',', usecols=0)
    colors = np.loadtxt(statsfile, dtype="str", skiprows=0, delimiter=',', usecols=1)

    # colors[colors == "No color photometric data"] = 0
    for count, color in enumerate(colors):

        if color == "No color photometric data":
            # sentinel values for mask
            colors[count] = "99999"
            deviations[count] = 99999
        # print(count)
        # print(colors[count])
    colors = np.asfarray(colors, float)
    colors = np.ma.masked_equal(colors, 99999)
    deviations = np.ma.masked_equal(deviations, 99999)
    scatterplot(deviations, colors, "RMS Deviation", "Bp_Rp Color", "RMS Deviation vs Color", 0.2)


def deviationvsbrightness(statsfile, metadata):
    # loadtxt read into numpy ndarrays
    deviations = np.loadtxt(statsfile, skiprows=0, delimiter=',', usecols=0)
    avgbrightnesses = np.loadtxt(metadata, skiprows=7, usecols=6)
    fallbackbrightnesses = np.loadtxt(metadata, skiprows=7, usecols=6)

    for count, brightness in enumerate(avgbrightnesses):
        if (brightness == "RRc"):
            avgbrightnesses[count] = fallbackbrightnesses[count]
    avgbrightnesses = np.ma.masked_equal(avgbrightnesses, -99.99)
    # plot
    scatterplot(deviations, avgbrightnesses, "RMS Deviation", "Avg Magnitude", "RMS Deviation vs Avg Magnitude", 0.1)
    # scatterplot(deviations, colors, "RMS Deviation", "Bp_Rp Color", "RMS Deviation vs Color", 0.3)


def periodvsmagnitude(metadata):
    # loadtxt read into numpy ndarrays
    periods = np.loadtxt(metadata, skiprows=7, usecols=8)
    fallbackperiods = np.loadtxt(metadata, skiprows=7, usecols=7)
    ibands = np.loadtxt(metadata, skiprows=7, usecols=6)
    for count, period in enumerate(periods):
        if period < 0.05:
            periods[count] = fallbackperiods[count]
    #        if ibands[count] < 0:
    #            print("less than 0")
    #            print(ibands[count])
    #            np.delete[ibands, count]
    #            np.delete[periods, count]
    ibands = np.ma.masked_equal(ibands, -99.99)
    scatterplot(periods, ibands, "Period Length", "Mean I-Band Magnitude", "Period Lengths vs Mean Magnitude", 0.25)


def amountofdeviation(statsfile):
    # loadtxt read into numpy ndarrays
    # deviation first column in CSV
    deviations = np.loadtxt(statsfile, skiprows=0, delimiter=',', usecols=0)
    deviations = np.ma.masked_greater(deviations, 0.1)
    """
    for deviation in deviations:
        if deviation > 0.1:
            index = np.where(deviations == deviation)
            np.delete(deviations, index)
    """
    # values
    # number = len(deviations)
    histplot(deviations, "RMS Deviation", "Frequency", "RMS Deviation Frequency Histogram")


def amountofcolor(statsfile):
    # loadtxt read into numpy ndarrays
    # colors second column in CSV
    colors = np.loadtxt(statsfile, dtype="str", skiprows=0, delimiter=',', usecols=1)

    for count, color in enumerate(colors):
        if color == "No color photometric data":
            # sentinel values for mask
            colors[count] = "99999"
    colors = np.asfarray(colors, float)
    colors = np.ma.masked_equal(colors, 99999)
    # values
    print(colors)
    print(type(colors))
    print(max(colors))
    # number = len(deviations)
    histplot(colors, "Bp_Rp Color", "Frequency", "Bp_Rp Frequency Histogram")


def colordevfitplot(statsfile):
    deviations = np.loadtxt(statsfile, skiprows=0, delimiter=',', usecols=0)
    colors = np.loadtxt(statsfile, dtype="str", skiprows=0, delimiter=',', usecols=1)

    # colors[colors == "No color photometric data"] = 0
    for count, color in enumerate(colors):

        if color == "No color photometric data":
            # sentinel values for mask
            colors[count] = "99999"
            deviations[count] = 99999
        # print(count)
        # print(colors[count])
    colors = np.asfarray(colors, float)
    colors = np.ma.masked_equal(colors, 99999)
    deviations = np.ma.masked_equal(deviations, 99999)
    scatterplot(deviations, colors, "RMS Deviation", "Bp_Rp Color", "RMS Deviation vs Color", 0.2)


# plotters
def scatterplot(x, y, xtitle, ytitle, plotname, size):
    fig = plt.figure(figsize=(10, 5))
    fig.suptitle(str(plotname), fontsize=20, fontweight='bold', y=0.96)
    ax = fig.add_subplot(111)
    fig.subplots_adjust(left=0.1, right=0.98, top=0.87, bottom=0.1)
    ax.set_xlabel(xtitle)
    ax.set_ylabel(ytitle)
    ax.invert_yaxis()
    # plot
    ax.scatter(x, y, s=size)

    """
    #fitting line
    grad, yint = np.polyfit(x, y, 1)
    plt.plot(x, grad * x + yint)

    #manual direction fit
    x_manual = [0.013, 0.03]
    y_manual = [0.847, 2.691]
    plt.plot(x_manual, y_manual)
    """

    # show plot if testing in IDE
    # plt.show()
    # save plot
    plt.savefig((outputdir + "/" + (plotname) + ".png"), format="png", dpi=1200)
    # plt.close("all")


def histplot(x, xtitle, ytitle, plotname):
    fig = plt.figure(figsize=(10, 5))
    fig.suptitle(str(plotname), fontsize=20, fontweight='bold', y=0.96)
    ax = fig.add_subplot(111)
    fig.subplots_adjust(left=0.1, right=0.98, top=0.87, bottom=0.1)
    ax.set_xlabel(xtitle)
    ax.set_ylabel(ytitle)

    bins = np.arange(0, 0.04, 0.005)
    print(bins)
    xticks = [(bins[idx + 1] + value) / 2 for idx, value in enumerate(bins[:-1])]
    xlabels = ["{:.2f} - {:.2f}".format(value, bins[idx + 1]) for idx, value in enumerate(bins[:-1])]

    plt.hist(x, bins, rwidth=0.9, edgecolor='black', linewidth=0.8)
    plt.xticks(xticks, labels=xlabels)
    ax.tick_params(axis='x', labelsize=7)

    # show plot if testing in IDE
    plt.show()
    # save plot
    # plt.savefig((outputdir + "/" + (plotname) + ".png"), format="png")
    plt.close("all")


# execution
# periodvsmagnitude(metadata)
# amountofdeviation()
# deviationvscolor(statsfile)
# colordevfitplot(statsfile)
# deviationvsbrightness(statsfile, metadata)
# amountofcolor(statsfile)


def test(BLG_metadata, LMC_metadata, SMC_metadata):
    def regionscatterplot(iv, type, xtitle, ytitle, plotname, size):
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
                ax.legend(["BLG", "LMC", "SMC"])
            if type == "RRc":
                ax.scatter(BLG_RRc[0], BLG_RRc[1], s=size, color="#332288")
                ax.scatter(LMC_RRc[0], LMC_RRc[1], s=size, color="#88CCEE")
                ax.scatter(SMC_RRc[0], SMC_RRc[1], s=size, color="#44AA99")
                ax.legend(["BLG", "LMC", "SMC"])
            if type == "RRd":
                ax.scatter(BLG_RRd[0], BLG_RRd[1], s=size, color="#332288")
                ax.scatter(LMC_RRd[0], LMC_RRd[1], s=size, color="#88CCEE")
                ax.scatter(SMC_RRd[0], SMC_RRd[1], s=size, color="#44AA99")
                ax.legend(["BLG", "LMC", "SMC"])
        elif iv == "v":
            if type == "RRab":
                ax.scatter(BLG_RRab[0], BLG_RRab[2], s=size, color="#332288")
                ax.scatter(LMC_RRab[0], LMC_RRab[2], s=size, color="#88CCEE")
                ax.scatter(SMC_RRab[0], SMC_RRab[2], s=size, color="#44AA99")
                ax.legend(["BLG", "LMC", "SMC"])
            if type == "RRc":
                ax.scatter(BLG_RRc[0], BLG_RRc[2], s=size, color="#332288")
                ax.scatter(LMC_RRc[0], LMC_RRc[2], s=size, color="#88CCEE")
                ax.scatter(SMC_RRc[0], SMC_RRc[2], s=size, color="#44AA99")
                ax.legend(["BLG", "LMC", "SMC"])
            if type == "RRd":
                ax.scatter(BLG_RRd[0], BLG_RRd[2], s=size, color="#332288")
                ax.scatter(LMC_RRd[0], LMC_RRd[2], s=size, color="#88CCEE")
                ax.scatter(SMC_RRd[0], SMC_RRd[2], s=size, color="#44AA99")
                ax.legend(["BLG", "LMC", "SMC"])
        plt.show
        plt.savefig((outputdir + "/" + (plotname) + ".png"), format="png", dpi=1200)

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

    # names = np.loadtxt(metadata, usecols=(0), skiprows=7, dtype=str)
    BLG_subtypes = np.loadtxt(BLG_metadata, usecols=(2), skiprows=7, dtype=str)
    BLG_ibands = np.loadtxt(BLG_metadata, usecols=(5), skiprows=7, dtype=float)
    # ibands = np.ma.masked_equal(ibands, -99.99)
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

    # RRab = [[[], [], []], [[], [], []], [[], [], []]]
    # RRc = [[[], [], []], [[], [], []], [[], [], []]]
    # RRd = [[[], [], []], [[], [], []], [[], [], []]]

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

    #scatterplot(RRab[0], RRab[1], "Period", "I-Band Magnitude", "Period vs I-Band Magnitude for RRab", 0.2)
    #scatterplot(RRc[0], RRc[1], "Period", "I-Band Magnitude", "Period vs I-Band Magnitude for RRc", 0.2)
    #scatterplot(RRd[0], RRd[1], "Period", "I-Band Magnitude", "Period vs I-Band Magnitude for RRd", 0.2)
    #scatterplot(RRab[0], RRab[2], "Period", "V-Band Magnitude", "Period vs V-Band Magnitude for RRab", 0.2)
    #scatterplot(RRc[0], RRc[2], "Period", "V-Band Magnitude", "Period vs V-Band Magnitude for RRc", 0.2)
    #scatterplot(RRd[0], RRd[2], "Period", "V-Band Magnitude", "Period vs V-Band Magnitude for RRd", 0.2)

    regionscatterplot("i", "RRab", "Period", "I-Band Magnitude", "Period vs I-Band Magnitude for all RRab", 0.2)
    regionscatterplot("i", "RRc", "Period", "I-Band Magnitude", "Period vs I-Band Magnitude for all RRc", 0.2)
    regionscatterplot("i", "RRd", "Period", "I-Band Magnitude", "Period vs I-Band Magnitude for all RRd", 0.2)
    regionscatterplot("v", "RRab", "Period", "I-Band Magnitude", "Period vs V-Band Magnitude for all RRab", 0.2)
    regionscatterplot("v", "RRc", "Period", "I-Band Magnitude", "Period vs V-Band Magnitude for all RRc", 0.2)
    regionscatterplot("v", "RRd", "Period", "I-Band Magnitude", "Period vs V-Band Magnitude for all RRd", 0.2)




    allscatterplot("i", "Period", "I-Band Magnitude", "Period vs I-Band Magnitude for all RR Lyrae", 0.2)
    allscatterplot("v", "Period", "V-Band Magnitude", "Period vs V-Band Magnitude for all RR Lyrae", 0.2)


test(BLG_metadata, LMC_metadata, SMC_metadata)
