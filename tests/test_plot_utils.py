import sys
import os
import pytest
import pandas as pd
from matplotlib.axes import Axes #imported .axes Axes to reference the actual type
from scr.plot_utils import plot_hist
df=pd.read_csv("/Users/brookeye/RISE/lab-5-eda/data/students (1).csv")
def test_plots(): #need to put tests in a function
    for column in df:
        assert isinstance(plot_hist(df, column), Axes)