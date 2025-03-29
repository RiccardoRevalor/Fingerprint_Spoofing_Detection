import numpy as np

def normalizeDataSet(features, mu):
    #compute std
    std = features.std(1)
    std = std.reshape((std.shape[0], 1))

    #normalize features
    normalizedFeatures = (features - mu) / std

    return normalizedFeatures