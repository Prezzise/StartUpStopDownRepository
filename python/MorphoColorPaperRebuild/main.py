import numpy as np

from ClassBraggModel import BraggModel
from ClassTMMModel import TMMModel

if __name__ == '__main__':
    ## Brag model calculations
    # theta = 0
    # d = 550
    # m = 4
    # bm1 = BraggModel(theta, d, m)
    #
    # lamb_min = 200.
    # lamb_max = 800.
    # amount = 1000
    # bm1.plot_intensity_interval(lamb_min, lamb_max, amount)

    ## TMM calculation 91,67
    d_list = [np.inf]
    n_list = [1.]
    x = 70.
    for i in range(4):
        d_list.append(91.67)
        n_list.append(1.5)

        d_list.append(137.5)
        n_list.append(1.)
    d_list.append(np.inf)
    n_list.append(1.)
    tmm1 = TMMModel(d_list, n_list)
    tmm1.plot_reflection_and_transmission_amplitude(lamb_max=2_000)
