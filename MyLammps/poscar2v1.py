import numpy as np
import os.path


def POSCAR2V1(filename):
    data_array = np.loadtxt(filename, skiprows=8)
    with open(filename, 'r') as f:
        data_header = f.readlines()
        vectors = data_header[2:5]
        number_of_atoms = int(data_header[6].strip())
        atom_type = data_header[5].strip()
    if number_of_atoms != len(data_array):
        raise ValueError('%d atoms is not equal the length of array %d' %
                         (number_of_atoms, len(data_array)))
    prefix = os.path.splitext(filename)[0]
    with open(prefix+'.v1', 'w') as f:
        f.write('Unit cell vectors:\n')
        f.write('va= %s' % vectors[0])
        f.write('vb= %s' % vectors[1])
        f.write('vc= %s' % vectors[2])
        f.write('%d\n' % number_of_atoms)
        for i in data_array:
            f.write('%s %.10f %.10f %.10f \n' % (atom_type, i[0], i[1], i[2]))


if __name__ == "__main__":
    POSCAR2V1('./carbon.poscar')
