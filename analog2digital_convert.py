#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math

import matplotlib.pyplot as plt

Ts=0.01 ; tn = np.arange(0, 4+Ts, Ts)

sampling_Ts = 0.1 ; sampling_tn = np.arange(0, 4+sampling_Ts, sampling_Ts)



# 아날로그 신호
amplitude=17*np.sin(np.pi * tn)
plt.plot(tn, amplitude)
print('')


# 샘플링 신호
sampling_amplitude=17*np.sin(np.pi * sampling_tn)
print("SAMPLING AMPLITUDE")
print(sampling_amplitude)
plt.stem(sampling_tn, sampling_amplitude, 'r')
print('')

# 양자화 신호
quantization_amplitude = np.around(sampling_amplitude).astype(np.int64)
print("QUANTIZATION AMPLITUDE")
print(quantization_amplitude)
plt.stem(sampling_tn, quantization_amplitude, 'g')
print('')

# 부호화 
coding_amplitude = []
for i in quantization_amplitude:
    coding_amplitude.append(bin(i))
print("CODING AMPLITUDE")
print(coding_amplitude)

plt.show()