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

# Sidebar for user inputs
st.sidebar.header('Option Parameters')
S = st.sidebar.number_input("Spot Price (S)", min_value=0.0, value=100.0)
K = st.sidebar.number_input("Strike Price (K)", min_value=0.0, value=100.0)
vol = st.sidebar.number_input("Volatility (vol)", min_value=0.0, value=0.3, step=0.01, format="%.2f")
T = st.sidebar.number_input("Time to Maturity (T)", min_value=0.1, value=5.0, step=0.1, format="%.1f")
r = st.sidebar.number_input("Risk-Free Rate (r)", min_value=0.0, value=0.02, step=0.01, format="%.2f")

# Compute option prices
Vcall, Vput = option_price(S, K, vol, T, r)

# Display results
st.subheader("Option Prices")
st.write(f"Call Option Price: {Vcall:.2f}")
st.write(f"Put Option Price: {Vput:.2f}")

# Dynamic range for time and option prices
time = np.linspace(0.1, T, 100)  # Generate 100 points from 0.1 to T
Vcalls = [option_price(S, K, vol, t, r)[0] for t in time]  # Compute call prices for each time

# Plot call option prices
fig, ax = plt.subplots()
ax.plot(time, Vcalls, label="Call Option Price")
ax.set_xlabel("Time to Maturity (Years)")
ax.set_ylabel("Call Option Price")
ax.set_title("Call Option Price vs. Time to Maturity")
ax.legend()
ax.grid()

# Display the plot in Streamlit
st.pyplot(fig)
