#!/usr/bin/env python3
# #########################################################
#
# HSDPlotData.py
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


from scipy.interpolate import RectBivariateSpline

import numpy as np

from Common import BasicPlotData as C_BPD


# #########################################################
# CHSDPlotData
# #########################################################

class CHSDPlotData(C_BPD.CBasicPlotData):

    def __init__(self, PlotParameters, GridSize, LogFile):
        super().__init__(PlotParameters, GridSize, LogFile)

#
# Analysis - functions
#

    def InterpolationAndMaximumPosition(self, InterpolationNumber):
        I_Number, J_Number = self.FilteredThresholdData2DNPArray.shape

        def CreateLinspaces(Number):
            Delta = 0.5 / Number
            I_Array = np.linspace(Delta, I_Number - Delta, Number * I_Number)
            J_Array = np.linspace(Delta, J_Number - Delta, Number * J_Number)
            return I_Array, J_Array

        I_Array, J_Array = CreateLinspaces(1)
        InterpolationSpline = RectBivariateSpline(
            I_Array, J_Array, self.FilteredThresholdData2DNPArray)
        I_Array, J_Array = CreateLinspaces(InterpolationNumber)
        Z = InterpolationSpline(I_Array, J_Array)

        Indexes = np.where(Z == np.max(Z))

        def GetPosition(Count, IJArray):
            Number = len(Indexes[Count])
            return IJArray[Indexes[Count][0]] if Number == 1 else \
                np.sum([IJArray[Index] for Index in Indexes[Count]]) / Number

        self.SetIJMaximumPosition([
            GetPosition(0, I_Array), GetPosition(1, J_Array)])
