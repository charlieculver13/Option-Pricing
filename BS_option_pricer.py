#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:57:03 2024

@author: charlieculver
"""

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import streamlit as st

# Function to calculate option prices
def option_price(S, K, vol, T, r):
    d1 = (np.log(S / K) + (r + (1 / 2) * vol**2) * T) / (vol * np.sqrt(T))
    d2 = d1 - vol * np.sqrt(T)
    
    Vcall = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    Vput = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    
    return Vcall, Vput

st.title("Options pricing app")

S = 100
K = 70
vol = 0.5
T = 1
r = 0.5

Vcall, Vput = option_price(S, K, vol, T, r)

st.write(f"Call Option Price is: {Vcall}")
st.write(f"Put Option Price is: {Vput}")

