#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 18:21:38 2017

@author: Creative
"""

import matplotlib.pyplot as plt
values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values,bins=3)
plt.show()