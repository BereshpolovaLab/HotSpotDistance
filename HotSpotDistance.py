#!/usr/bin/env python3
# #########################################################
#
# HotSpotDistance.py
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


from HotSpotDistancePackage import HSDMain as HSDP_HSDM


# #########################################################
# Parameters
# #########################################################

InputDir = 'Data/'
OutputDir = 'Output/HotSpotDistance/'
BasicFileName = '2019Aug19Bsn2-01'
PLXFileName = F'{InputDir}{BasicFileName}.plx'
LogFileName = F'{OutputDir}{BasicFileName}.txt'
PlotGraphicFileName = F'{OutputDir}{BasicFileName}_Plots.png'

Parameters = {
    'ProtocolNumber': 11, 'VRR': 160, 'VRR_AutoDetectFlag': True,
    'PlexonDigitalCard': 0,
    'FileInterval': (None, None),
    'Filter': 'gaussian',
    'GaussianSigma': 0.5,
    'Interpolation': 'bicubic',
    'InterpolationNumber': 10,

    'Channels': ({

        'Channel': 17,
        'Cluster': 2,
        'Response': 'On',
        'TimeWindow': (20, 45),
        'Threshold': 0.3}, {

        'Channel': 17,
        'Cluster': 3,
        'Response': 'On',
        'TimeWindow': (25, 50),
        'Threshold': 0.4}, {

        'Channel': 17,
        'Cluster': 2,
        'Response': 'Off',
        'TimeWindow': (20, 45),
        'Threshold': 0.3}, {

        'Channel': 17,
        'Cluster': 3,
        'Response': 'Off',
        'TimeWindow': (25, 50),
        'Threshold': 0.4}),

    'PlotGridLineVisible': True,
    'PlotGridLineColor': 'grey',
    'PlotGridLineStyle': 'dotted',
    'PlotGraphicFileDPI': 300}


# ##########################################################
# Analysis
# ##########################################################

HSDP_HSDM.Main(
    Parameters, PLXFileName, LogFileName, PlotGraphicFileName)
