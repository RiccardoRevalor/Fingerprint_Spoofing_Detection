import numpy as np

def loadDataSet(path, numFeatures):
    rawData = np.genfromtxt(path, delimiter=',', dtype = "str")

    #extract the 6 feature for each footprint
    features = rawData[:, 0:numFeatures]
    features = np.array(features, dtype= np.float64).T

    #extract the labels: 1->True, 0->False
    labels = rawData[:, -1]
    labels = np.array(labels, dtype=np.int16)

    return features, labels

