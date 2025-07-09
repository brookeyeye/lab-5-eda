from setuptools import setup, find_packages
setup(
name="histograms",
version="0.1.0",
packages=find_packages(),
) #this stuff was necessary in order to import my functions into the test file because pytest sucks