#!/usr/bin/env python3
# #########################################################
#
# HSDPlexonData.py
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


import math
import matplotlib.pyplot as plt
import tabulate

from Common import BasicPlexonData as C_BPD
from Common import ToolObject as C_TO
from HotSpotDistancePackage import HSDChannelData as HSDP_HSDCD


# ##########################################################
# CHSDPlexonData
# ##########################################################

class CHSDPlexonData(C_BPD.CBasicPlexonData, C_TO.CToolObject):

    def __init__(self, Parameters, LogFile):
        super().__init__(Parameters, LogFile)

        self.ChannelDataList = [
            HSDP_HSDCD.CHSDChannelData(CHP, self.GridSize, LogFile)
            for CHP in self.GetParameters_Channels()]

#
# GetParameters - functions
#

    def GetParameters_InterpolationNumber(self):
        return self.DictionaryParameter(
            self.Parameters, 'InterpolationNumber')

#
# Analysis - functions
#

    def PlotProcessing(self, PLXFileName):
        self.LoadData_CheckSpikesAndTTLEvents(PLXFileName)
        if self.StatusFlag and self.ChannelDataList[0].GetStatus() and \
                self.ChannelDataList[1].GetStatus():
            self.StimulusTimeStampCorrection()
            for CD in self.ChannelDataList:
                CD.ReverseCorrelationFilterThresholdData(
                    self.OnOffStimuliList, self.GetParameters_Filter(),
                    self.GetParameters_GaussianSigma())
                CD.InterpolationAndMaximumPosition(
                    self.GetParameters_InterpolationNumber())

    def ShowPlots(self, PlotGraphicFileName):
        fig, aspect, pad_fraction = plt.figure(), 20, 1.0
        fig.suptitle('Plots', fontsize=20)

        SubplotGridSizeTuple = ((len(self.ChannelDataList) + 1) // 2, 2)
        for J_CD, CD in enumerate(self.ChannelDataList):
            IJTuple = (J_CD // 2, J_CD % 2)
            self.PresentPlot(
                CD, CD.GetPlotData(), aspect, pad_fraction,
                SubplotGridSizeTuple, IJTuple)
        self.ShowAndSave(
            fig, PlotGraphicFileName, 'PlotGraphicFileDPI', 'plot')

    def PrintParameters(self):
        PositionList, Count, D_String = [], 1, None
        self.Print(('\nPositions CH.CL-R: I, J:\n'))
        HeaderList, VList = ['CH.CL-R', 'I', 'J'], []
        for I_CD, CD in enumerate(self.ChannelDataList):
            Tuple, IString, JString = CD.PrintPosition()
            VList.append([Tuple[0], IString, JString])
            PositionList.append(Tuple)
        Tabulate = tabulate.tabulate(VList, headers=HeaderList)
        self.Print((Tabulate, '\n'))

        self.Print(('Distances and angles between CH.CL-R and CH.CL-R\n'))
        HeaderList, VList = ['CH.CL-R_1', 'CH.CL-R_2', 'D', 'Angle'], []
        Length = len(PositionList)
        for I_D in range(Length-1):
            for J_D in range(I_D + 1, Length):
                I_Tuple, J_Tuple = PositionList[I_D], PositionList[J_D]
                D_String = self.GetDistanceString(I_Tuple[1:], J_Tuple[1:])
                Angle_String = self.GetAngleString(
                    I_Tuple[1:], J_Tuple[1:], -1.0)
                VList.append([I_Tuple[0], J_Tuple[0], D_String, Angle_String])
                Count += 1
        Tabulate = tabulate.tabulate(VList, headers=HeaderList)
        self.Print((Tabulate, '\n\n'))
