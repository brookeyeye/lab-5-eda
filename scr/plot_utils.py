import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt #.pyplot is important
def plot_hist(df, col, bins=20):
    plot = sns.histplot(data=df, x=col, kde=True)
    plt.title(f"Distribution of {col}")
    plt.show()
    return plot #had to return the plot to check data type