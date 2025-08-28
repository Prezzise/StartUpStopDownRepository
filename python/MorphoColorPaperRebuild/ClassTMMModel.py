import numpy as np
from matplotlib import pyplot as plt
from tmm import coh_tmm


class TMMModel:
    """
    Class for making TMM (transfer matrix method) calculations.
    It takes as an input the expansion of the different segments, their n coefficient
    and the incident angle.
    Parameters
    :param d_list: (list) list containing the expansion of the different segments. Has to start and end with np.inf
    :param n_list (list) list containing the n coefficient for the different segments
    :param theta (float) incident angle
    """
    def __init__(self, d_list: list, n_list: list, theta: float = 0.):
        # list of layer thicknesses in nm
        self.d_list = d_list
        # list of refractive indices
        self.n_list = n_list
        self.theta = theta

    def calculate_tmm(self, lamb_min: float = 250., lamb_max: float = 850., amount: int = 1000) -> list:
        """
        Makes a TMM calculation for the geometry defined by the object for each wavelengths described by the
        parameters "lamb_min", "lamb_max" and "amount"
        ''
        :param lamb_min:
        :param lamb_max:
        :param amount:
        :return:
        """

        lamb_list = np.linspace(lamb_min, lamb_max, num=amount)

        # initialize lists of y-values to plot
        result = []
        for lamb in lamb_list:
            res_i = coh_tmm('s', self.n_list, self.d_list, self.theta, lamb)
            result.append(res_i)

        return result

    def plot_reflection_and_transmission_amplitude(self, lamb_min: float = 250.,
                                                   lamb_max: float = 850.,
                                                   amount: int = 1000):
        values = self.calculate_tmm(lamb_min, lamb_max, amount)
        lamb_list = [val['lam_vac'] for val in values]

        r_dict = {'key': 'R',
                  'description': r"Reflection amplitude"}
        t_dict = {'key': 'T',
                  'description': r"Transmission amplitude"}
        plot_info = [r_dict, t_dict]

        print('Plotting the reflection and transmission amplitude of the model')
        # Plot reflection amplitude
        for dict_info in plot_info:
            y_list = [val[dict_info['key']] for val in values]
            plt.plot(lamb_list, y_list, ls='-', label=dict_info['description'])
            plt.xlabel(r'$\lambda $')
            plt.ylabel(fr'${dict_info['key']}$')
            plt.grid()
            plt.legend()
            plt.title(dict_info['description'])
            plt.show()