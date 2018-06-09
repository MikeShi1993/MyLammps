import numpy as np
from sys import argv


def sorting_atoms(filename):
    with open(filename, 'r') as f:
        header = f.readlines()[:8]
    header = ''.join(header)
    data = np.loadtxt(filename, skiprows=9)
    data[:, 0] = range(1, len(data)+1)
    fmt = ['%d', '%d'] + ['%.9f' for i in range(data.shape[1]-2)]
    np.savetxt(filename+'.new', data, fmt=fmt, header=header, comments='')


def main():
    filename = argv[-1]
    sorting_atoms(filename)


if __name__ == "__main__":
    filename = 'data.lmp.active.140'
    sorting_atoms(filename)
