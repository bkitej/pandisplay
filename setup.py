from setuptools import find_packages
from setuptools import setup

setup(
    name='pandisplay',
    version='0.1.0',
    packages=find_packages(),
    description='Pandas display methods for DataFrame visualization in Jupyter Notebooks.',
    author='Ben Johnson',
    author_email='bkitej@gmail.com',
    install_requires=[
        'pandas',
        'ipython'
    ],
)