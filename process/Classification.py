import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import os

dir = os.path.dirname(__file__)
dataPeoples = os.path.join(dir,"./data/Users.txt")

def readData():
    Info = np.array([])
    with open(dataPeoples,"r") as f:
        for line in f:
            aline = line.strip().split(",")
