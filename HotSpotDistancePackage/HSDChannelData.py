#!/usr/bin/env python3
# #########################################################
#
# HSDChannelData.py
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


from Common import BasicChannelData as C_BCD
from HotSpotDistancePackage import HSDPlotData as HSDP_HSDPD


# ##########################################################
# CHSDChannelData
# ##########################################################

class CHSDChannelData(C_BCD.CBasicChannelData):

    def __init__(self, CHP, GridSize, LogFile):
        super().__init__(CHP, LogFile)
        self.PlotData = HSDP_HSDPD.CHSDPlotData(CHP, GridSize, LogFile)

#
# Get - functions
#

    def GetFilteredThresholdData2DNPArray(self):
        return self.PlotData.GetFilteredThresholdData2DNPArray()

    def GetFilteredThresholdData2DNPArray_Maximum(self):
        return self.PlotData.GetFilteredThresholdData2DNPArray_Maximum()

    def GetPlotData(self): return self.PlotData

    def GetIJMaximumPosition(self): return self.PlotData.GetIJMaximumPosition()

#
# Analysis - functions
#

    def ReverseCorrelationFilterThresholdData(
            self, OnOffStimuliList, Filter, GaussianSigma):
        self.PlotReverseCorrelationFilterData(
            self.PlotData, OnOffStimuliList, Filter, GaussianSigma)
        self.ThresholdData(self.PlotData)

    def InterpolationAndMaximumPosition(self, InterpolationNumber):
        self.PlotData.InterpolationAndMaximumPosition(InterpolationNumber)

#
# Output - functions
#

    def PrintPosition(self):
        ChannelString = (
            F'{self.GetCHP_Channel():2d}.'
            F'{self.GetCHP_Channel():1d}-{self.GetCHP_Response().ljust(3)}')
        I, J = self.GetIJMaximumPosition()
        IString = F'{I:>6.3f}' if I is not None and J is not None else 'XX'
        JString = F'{J:>6.3f}' if I is not None and J is not None else 'XX, XX'
        return (ChannelString, I, J), IString, JString
