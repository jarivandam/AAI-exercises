from scipy.spatial import distance
import numpy as np
import random


def loadCsvToNumpy(filename):
    return np.genfromtxt(filename, delimiter=";", usecols=[1, 2, 3, 4, 5, 6, 7], converters={
        5: lambda s: 0 if s == b"-1" else float(s), 7: lambda s: 0 if s == b"-1" else float(s)})


def generateLabelsData(dates):
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


def generateLabelsValidation(dates):
    labels = []
    for label in dates:
        if label < 20010301:
            labels.append("winter")
        elif 20010301 <= label < 20010601:
            labels.append("lente")
        elif 20010601 <= label < 20010901:
            labels.append("zomer")
        elif 20010901 <= label < 20011201:
            labels.append("herfst")
        else:  # from 01-12 to end of year
            labels.append("winter")
    return labels


def findCentroids(data: list, numberOfCentroids: int):
    centroids = []
    for i in range(0, numberOfCentroids):
        centroid = data[random.randint(0, len(data))]
        centroids.append(centroid)
    return centroids


def makeClusters(data: list, centroids: list, k: int):
    clusters = [[]] * k
    for i in range(len(data)):
        distances = []
        for j in range(len(centroids)):
            d = distance.euclidean(data[i], centroids[j])
            distances.append((d, i, j))
        distances.sort(key=lambda x: x[1])
        clusters[distances[0][2]].append(data[distances[0][1]])

    return clusters


def calcMeanPointInCluster(cluster: list, centroid):
    meanPoint = 0
    return meanPoint


def main():
    data = loadCsvToNumpy('dataset1.csv')
    dates = np.genfromtxt("dataset1.csv", delimiter=";", usecols=[0])
    labels = generateLabelsData(dates)

    k = 4
    centroids = findCentroids(data, k)

    clusters = makeClusters(data, centroids, k)

    calcMeanPointInCluster(clusters[0], centroids[0])


if __name__ == "__main__":
    main()
