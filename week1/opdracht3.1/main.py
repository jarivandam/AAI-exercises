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

def k_NearestNeighbours(data, testpoint, datalabels, validationlabels, k):
    delta = []
    for i in range(0, len(dates)):
        delta.append(distance.euclidean(testpoint, data[i]))

    nearest = [-1, -1, -1, -1, -1]
    nearestindex = [0, 0, 0, 0, 0]

    for i in range(0, len(delta)):
        for j in range(0, k):
            if delta[i] < nearest[j] or nearest[j] == -1:
                nearest[j] = delta[i]
                nearestindex[j] = i
                break
    print(nearest)
    print(nearestindex)
    # for i in range(0, len(nearestindex)):
    #     print(labels[nearestindex[i]])
    return mostOccurringLabel(nearest, labels)

def mostOccurringLabel(array, label):
    valueCounts = [0,0,0,0]
    labels = ['winter', 'lente', 'zomer', 'herfst']
    for i in range(0, len(array)):
        if label[i] == 'winter':
            valueCounts[0] += 1
        elif label[i] == 'lente':
            valueCounts[1] += 1
        elif label[i] == 'zomer':
            valueCounts[2] += 1
        elif label[i] == 'herfts':
            valueCounts[3] += 1

        else:
            raise ValueError


    return labels[valueCounts.index(max(valueCounts))]






data = loadCsvToNumpy('dataset1.csv')
# print(data)
dates = np.genfromtxt("dataset1.csv", delimiter=";", usecols=[0])
labels = generateLabels(dates)

# print(labels)
validationData = loadCsvToNumpy('validation1.csv')

validationDates = np.genfromtxt("validation1.csv", delimiter=";", usecols=[0])
validationLabels = generateLabels(validationDates)

testpoint = [10,20,30,30,30,30,30]

k = 5
for i in range(0, len(validationData)):
    print(k_NearestNeighbours(data, validationData[i], labels, validationLabels, k))


