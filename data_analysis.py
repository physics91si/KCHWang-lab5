#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def wavepacket(x, k, sigma):
    """This function creates a wavepacket on the interval defined by x with
    wavevector k and standard deviation sigma."""
    return np.sin(k*x) *  np.exp(-(x**2)/(2*sigma**2))


def main():
    """This function sould call noisy_packet() to get a Gaussian wave
    packet, call clean_data() to apply a low pass filter to the data and
    finally plot the result."""
    x_values = np.arange(-np.pi, np.pi, 0.01)
    noisy_y = noisy_packet(x_values, k = 5, sigma = 1, noise_amplitude = 0.2)
    clean_y = wavepacket(x_values,k = 5, sigma = 1)
    noisy_cleaned_y = clean_data(x_values,noisy_y)
    
    plt.figure(1)
    plt.title('original wave')
    plt.plot(x_values, clean_y)
    
    plt.figure(2)
    plt.title('noisy wave')
    plt.plot(x_values, noisy_y)
    
    plt.figure(3)
    plt.title('cleaned wave')
    plt.plot(x_values, noisy_cleaned_y)
    
    plt.show()

def noisy_packet(x_values, k, sigma, noise_amplitude):
    """This function returns a noisy Gaussian wavepacket with wave
    vector k, standard deviation sigma and Gaussian noise of standard
    deviation noise_amplitude."""
    clean_y = wavepacket(x_values,k,sigma)
    noisy_y = clean_y + noise_amplitude*np.random.randn(len(x_values))
    return noisy_y

def clean_data(x_values,y_values):
    """This function should take a set of y_values, perform the Fourier
    transform on it, filter out the high frequency noise, transform the
    signal back into real space, and return it."""
    y_fft = np.fft.rfft(y_values) # Fourier transform
    
    low_pass_filter = np.ones(y_fft.shape) # build low pass filter for Fourier function
    num_freq = y_fft.size
    low_pass_filter[num_freq//25:num_freq] = 0
    
    y_clean_fft = np.multiply(y_fft, low_pass_filter) # perform low pass filter
    
    y_clean_values = np.fft.irfft(y_clean_fft, len(y_values)) # Inverse Fourier transform
    return y_clean_values

main()  # calls your main function
