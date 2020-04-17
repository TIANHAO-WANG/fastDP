import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.stats import norm
import pickle

false_rates_dict = {}

# read in the data from the CSV file
def read_data(file):
    with open(file, 'rb') as f:
        next(f) # skip labels
        X, Y = [], []
        reader = csv.reader(f)
        for row in reader:

            if sum(np.array(row)=='NA'): # leave out all NAs
                continue

            x = map(int, row[:5]) + map(int, row[6:-2]) # map input to integers

            X.append(x)
            Y.append(int(row[5]))

    X, Y = np.array(X), np.array(Y)
    print(X.shape, Y.shape)

    return X, Y


if __name__ == "__main__":
    print(read_data('data/mini_data.csv'))