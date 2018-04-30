import numpy as np
import os.path

Dict_Elem2num = {b'C': 1, b'H': 2, b'O': 3}
Dict_Num2elem = {1: 'C', 2: 'H', 3: 'O'}


def elem2num(element):
    element = element.strip()
    return Dict_Elem2num[element]


def xyzReFormat(filename):
    with open(filename, 'r') as f:
        row1, row2 = f.readlines()[:2]
    data = np.loadtxt(filename, skiprows=2, converters={0: elem2num})
    data[:, 1] = data[:, 1] - data[:, 1].min()
    data[:, 2] = data[:, 2] - data[:, 2].min()
    data[:, 3] = data[:, 3] - data[:, 3].min()
    with open(filename+'.output', 'w') as f:
        f.write(row1)
        f.write(row2)
        for i in data:
            f.write('%s %.6f %.6f %.6f \n' %
                    (Dict_Num2elem[int(i[0])], i[1], i[2], i[3]))


if __name__ == "__main__":
    xyzReFormat('carbon.xyz')
