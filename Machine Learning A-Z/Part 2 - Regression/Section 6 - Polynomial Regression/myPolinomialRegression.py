#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:14:40 2017

@author: Luiz Nachtigall
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing data
dataset =pd.read_csv("Position_Salaries.csv")
matrizX = dataset.iloc[:,:-1]
matrizY = dataset.iloc[:,-1]


