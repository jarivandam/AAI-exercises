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
# print(data)
dates = np.genfromtxt("dataset1.csv", delimiter=";", usecols=[0])
labels = generateLabels(dates)

# print(labels)
validationData = loadCsvToNumpy('validation1.csv')

validationDates = np.genfromtxt("validation1.csv", delimiter=";", usecols=[0])
validationLabels = generateLabels(validationDates)

testpoint = [10,20,30,30,30,30,30]

delta = []
k = 3
for i in range(0, len(dates)):
    delta.append(distance.euclidean(testpoint, data[i]))

nearest = [-1, -1, -1]
nearestindex = [0, 0, 0]
for i in range(0, len(delta)):
    for j in range(0, k):
        if delta[i] < nearest[j] or nearest[j] == -1:
            nearest[j] = delta[i]
            nearestindex[j] = i
            # print(labels[i])
            break
print(nearest)
print(nearestindex)
for i in range(0, len(nearestindex)):
    print(labels[nearestindex[i]])

