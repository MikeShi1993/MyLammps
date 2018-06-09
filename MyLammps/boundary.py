import numpy as np
from sys import argv


def GetBoundary(filename, skiprows=9):
    data = np.loadtxt(filename, skiprows=skiprows)
    minz = data[:, -1].min()
    miny = data[:, -2].min()
    minx = data[:, -3].min()
    maxz = data[:, -1].max()
    maxy = data[:, -2].max()
    maxx = data[:, -3].max()
    print("minx, maxx: %.6f %.6f" % (minx, maxx))
    print("miny, maxy: %.6f %.6f" % (minx, maxy))
    print("minz, maxz: %.6f %.6f" % (minx, maxz))


def main():
    filename = argv[-1]
    GetBoundary(filename)


if __name__ == "__main__":
    print(argv)
    filename = argv[-1]
    GetBoundary(filename)
