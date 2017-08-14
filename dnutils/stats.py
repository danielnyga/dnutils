'''
Created on Jan 5, 2017

@author: nyga
'''
import numpy as np
from tabulate import tabulate

from dnutils import ifnone


class Gaussian(object):
    '''
    A Gaussian distribution that can be incrementally updated with new samples
    '''

    def __init__(self, mean=None, cov=None, data=None):
        self.mean = ifnone(mean, None, np.array)
        self.cov = ifnone(cov, None, np.array)
        self.samples = []
        if data is not None:
            self.estimate(data)

    @property
    def dim(self):
        if self.mean is None:
            raise ValueError('no dimensionality specified yet.')
        return len(self.mean)

    def update(self, x):
        '''update the Gaussian distribution with a new data point `x`.'''
        try:
            len(x)
        except AttributeError:
            x = [x]
        if self.mean is None or self.cov is None:
            self.mean = np.zeros(len(x))
            self.cov = np.zeros(shape=(len(x), len(x)))
        n = len(self.samples)
        oldmean = np.array(self.mean)
        oldcov = np.array(self.cov)
        for i, (m, d) in enumerate(zip(self.mean, x)):
            self.mean[i] = ((n * m) + d) / (n + 1)
        self.samples.append(x)
        if n > 0:
            for j in range(self.dim):
                for k in range(self.dim):
                    self.cov[j, k] = (oldcov[j, k] * (n - 1) + n * oldmean[j] * oldmean[k] + x[j] * x[k] - (n + 1) * self.mean[j] * self.mean[k]) / float(n)
        return self

    def update_all(self, data):
        '''Update the distribution with new data points given in `data`.'''
        for x in data:
            self.update(x)
        return self

    def estimate(self, data):
        '''Estimate the distribution parameters with subject to the given data points.'''
        self.mean = self.cov = None
        return self.update_all(data)

    def sample(self, n=1):
        '''Return `n` samples from the distribution subject to the parameters.'''
        if self.mean is None or self.cov is None:
            raise ValueError('no parameters. You have to set mean and covariance before you draw samples.')
        return np.random.multivariate_normal(self.mean, self.cov, size=n)

    def __repr__(self):
        try:
            dim = '%s-dim' % str(self.dim)
            if self.dim == 1:
                dim = 'mu=%.2f, sigma=%.2f' % (self.mean[0], self.cov[0, 0])
        except ValueError:
            dim = '(undefined)'
        return '<Gaussian %s at 0x%s>' % (dim, hex(id(self)))

    def __str__(self):
        return '<Gaussian\nmean=\n%s\nstddev=\n%s>' % (self.mean, tabulate(self.cov))
