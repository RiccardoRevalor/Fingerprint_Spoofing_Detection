# CORRELATION

#Compute Pearson correlation coefficient

import numpy as np
from mean_covariance import vcol, vrow

def computeCorrelation(C):
    """
    Compute the Pearson correlation coefficient

    Parameters:
    - C: the covariance matrix of shape (numFeatures, numFeatures)

    Returned Values:
    - Corr: the correlation matrix of shape (numFeatures, numFeatures) where each element is the Pearson correlation coefficient between two features

    """


    Corr = C / ( vcol(C.diagonal()**0.5) * vrow(C.diagonal()**0.5) )

    return Corr

