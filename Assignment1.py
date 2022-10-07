# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:41:15 2022

@author: anine
"""

# import sox
# import pysox as psx
import numpy as np
import scipy.io.wavfile as spwav
import scipy.fft as spfft
import pylab as pl

#import wav file and read in the data
audio = "audio.wav"
sample_rate, data = spwav.read(audio)

#find the audio length
duration = len(data)/sample_rate

#normalise x,y axis
datax, datay = np.split(data,2,axis=1)
norm_datay = datay/np.max(datay)
time = np.arange(0, duration, (1/sample_rate))

#fft stuff
f_domain = spfft.fft(time)
dataydb = 20*np.log10(abs(norm_datay))

#plotting
pl.plot(f_domain,dataydb)
pl.ylabel('Normalised Amplitude')
pl.xlabel('Time [s]')
pl.title('Original Voice Recording Plot')
pl.show()