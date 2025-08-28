import math

import numpy as np
from matplotlib import pyplot as plt


class BraggModel:
    """
    Class for the simple Bragg model, which is described by the equation:
    $I(theta, lambda, d) = sin^2(0.5 k d nu M)/sin^2(0.5 k d v)
    where k = 2pi/lambda, nu = 2cos(theta), M is the number of lamella,
    d is the spacing between the lamella, lambda the wavelength and theta the incidence angle

    Parameters:
        :param theta: incidence angle
        :param d: spacing between lamella
        :param m: amount of lamella
        -theta: incidence angle
        -d: spacing between lamella
        -m: amount of lamella
    """
    def __init__(self, theta: float, d: float, m: int):
        self.theta = theta
        self.d = d
        self.m = m
        self.nu = 2*math.cos(theta)

    def calc_single_intensity(self, lamb: float) -> float:
        """
        Calculates the intensity according to the simple Bragg model of the wavelength lamb

        :return: (float) intensity of the specified Bragg model
        """
        k = 2 * math.pi / lamb
        intensity = math.sin(0.5 * k * self.d * self.nu * self.m) / math.sin(0.5 * k * self.d * self.nu)
        intensity = intensity**2
        return intensity

    def calc_intensity_interval(self, lamb_min: float, lamb_max: float, amount: int) -> tuple:
        """
        Calculates the wavelengths and the associated intensities in the interval [lamb_min, lamb_max]
        with a total of "amount" points
        :param lamb_min: (float) minimal wavelength
        :param lamb_max: (float) maximal wavelength
        :param amount: (int) amount of points in the interval
        :return: (tuple(np.array, np.array)) the interval containing the wavelengths and the interval
                 containing the intensities
        """

        d_lamb = (lamb_max - lamb_min) / amount
        lamb_array = np.arange(lamb_min, lamb_max, d_lamb)

        intensity_arr = np.array(list(map(self.calc_single_intensity, lamb_array)))

        return lamb_array, intensity_arr

    def plot_intensity_interval(self, lamb_min: float, lamb_max: float, amount: int) -> None:
        """
        Plots the wavelengths and the associated intensities in the interval [lamb_min, lamb_max]
        with a total of "amount" points
        :param lamb_min: (float) minimal wavelength
        :param lamb_max: (float) maximal wavelength
        :param amount: (int) amount of points in the interval
        """
        lamb_array, intensity_arr = self.calc_intensity_interval(lamb_min, lamb_max, amount)
        intensity_max = np.max(intensity_arr)
        intensity_arr = intensity_arr / intensity_max

        plt.plot(lamb_array, intensity_arr, ls='-', label=fr"${self.m}$th harmonic")
        plt.xlabel(r'$\lambda $')
        plt.ylabel(r'$I(\lambda )$')
        plt.grid()
        plt.legend()
        plt.show()





