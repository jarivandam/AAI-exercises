from scipy.spatial import distance
import numpy as np


def loadCsvToNumpy(filename):
    return np.genfromtxt(filename, delimiter=";", usecols=[1, 2, 3, 4, 5, 6, 7], converters={
        5: lambda s: 0 if s == b"-1" else float(s), 7: lambda s: 0 if s == b"-1" else float(s)})


def generateLabels(dates):
    labels = []
    for label in dates:
        if label < 20000301:
            labels.append("winter")
        elif 20000301 <= label < 20000601:
            labels.append("lente")
        elif 20000601 <= label < 20000901:
            labels.append("zomer")
        elif 20000901 <= label < 20001201:
            labels.append("herfst")
        else:  # from 01-12 to end of year
            labels.append("winter")
    return labels


data = loadCsvToNumpy('dataset1.csv')
dates = np.genfromtxt("dataset1.csv", delimiter=";", usecols=[0])
labels = generateLabels(dates)

validationData = loadCsvToNumpy('validation1.csv')

validationDates = np.genfromtxt("validation1.csv", delimiter=";", usecols=[0])
validationLabels = generateLabels(validationDates)


for i in range(0, len(dates)-1):
    distance = np.zeros(7)
    for j in range(0, len(dates)-1):
        delta = data[i] - data[j]
        if delta.all() < distance.all():
            distance = delta
    print(distance)
