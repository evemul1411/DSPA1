# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:41:15 2022

@author: anine
"""

# import sox
# import pysox as psx
import numpy as np
import scipy.io.wavfile as spwav
#from scipy.fft import fft,rfft,rfftfreq, fftfreq
import pylab as pl
#import math

#import wav file and read in the data

audio = "audio.wav"
sample_rate, data = spwav.read(audio)
# Get one side of audio data
data = data[:,1]
data = data/np.max(data) #normalise data between -1 and +1

#find the audio length
duration = len(data)/sample_rate
#Find Sample Size
sample_size = len(data)

#Time Domain
time = np.linspace(0., duration, len(data))

#Frequency Domain
FreqAxis = np.linspace(0., sample_rate, len(data))
xf = np.fft.fft(data)/len(data)
yf = 20*np.log10(abs(xf))



#Checking Sampling Theorem

maxfrequency = np.max(xf)
print(maxfrequency)
print(sample_rate)
print(sample_rate / 2)
print(sample_size)


#plotting

f1 = pl.plot(time,data)
pl.ylabel('Normalised Amplitude')
pl.xlabel('Time [s]')
pl.title('Original Voice Recording Plot')



pl.show()


f2 = pl.plot(FreqAxis,yf)
pl.ylabel('Amplitude [dB]')
pl.xlabel('Frequency [Hz]')
pl.xscale("log")
pl.title('Frequency Domain Recording Plot')


pl.show()

