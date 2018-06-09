from setuptools import setup

setup(
    name='MyLammps',
    version='0.0.5',
    description='Mylammps small tools',
    author='Linyuan Shi',
    author_email='sly1993@ufl.edu',
    license='MIT',
    packages=['MyLammps'],
    entry_points={
        'console_scripts': ['getboundary=MyLammps.boundary:main'],
        'console_scripts': ['sortingatoms=MyLammps.sorting_atoms:main'],
    },
    zip_safe=False)
