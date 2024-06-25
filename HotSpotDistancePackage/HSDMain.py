#!/usr/bin/env python3
# #########################################################
#
# HSDMain.py
#
# Python3 (NumPy, SciPy, MatPlotLib)
#
# Bereshpolova lab, University of Connecticut
# Victor Serdyukov (svv_vick)
# 2021 - 2024
#
# emails: Victor.Serdyukov@uconn.edu
#         svv_vick@yahoo.com
#
# #########################################################


from Common import LogFileObject as C_LFO
from HotSpotDistancePackage import HSDPlexonData as HSDP_HSDPD


# #########################################################
# Analysis
# #########################################################

def Main(Parameters, PLXFileName, LogFileName, PlotGraphicFileName):
    LFO = C_LFO.CLogFileObject(LogFileName)
    HSDPD = HSDP_HSDPD.CHSDPlexonData(Parameters, LFO.LogFile)
    if len(HSDPD.GetParameters_Channels()) >= 2:
        HSDPD.PlotProcessing(PLXFileName)
        if HSDPD.GetStatusFlag():
            HSDPD.ShowPlots(PlotGraphicFileName)
            HSDPD.PrintParameters()
    else:
        HSDPD.Print(('Wrong setting of parameter \'Channels\'.'))
        HSDPD.Print(('The number of channels should be 2 or bigger.'))
