import numpy as np
from slsim.Util import check_params


class GaussianMixtureModel:
    """A Gaussian Mixture Model (GMM) class.

    This class is used to represent a mixture of Gaussian distributions, each of which
    is defined by its mean, standard deviation and weight.
    """

    @check_params
    def __init__(self, means: list[float], stds: list[float], weights:list[float]):
        """
        The constructor for GaussianMixtureModel class. The default values are the
        means, standard deviations, and weights of the fits to the data in the table
        2 of https://doi.org/10.1093/mnras/stac2235 and others. See "_params" for
        defaults and validation logic.

        :param means: the mean values of the Gaussian components.
        :type means: list of float
        :param stds: The standard deviations of the Gaussian components.
        :type stds: list of float
        :param weights: The weights of the Gaussian components in the mixture.
        :type weights: list of float
        """
        self.means = means
        self.stds = stds
        self.weights = weights

    @check_params
    def rvs(self, size: int):
        """Generate random variables from the GMM distribution.

        :param size: The number of random variables to generate.
        :type size: int
        :return: An array of random variables sampled from the GMM distribution.
        :rtype: np.array
        """
        components = np.random.choice(len(self.means), size=size, p=self.weights)
        return np.array(
            [
                np.random.normal(self.means[component], self.stds[component])
                for component in components
            ]
        )
