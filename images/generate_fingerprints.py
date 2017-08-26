import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pathlib

for filename in ['grasr-fortran.csv', "grasr-python.csv"]:
    print(filename)
    stem = pathlib.Path(filename).stem
    df = pd.read_csv(filename)
    df = df.pivot(index='y', columns='x', values='score')
    array = np.array(df)[::-1]

    plt.figure()
    plt.imshow(array, cmap="seismic")
    max_score = np.max(array)
    min_score = np.min(array)
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    ticks = [min_score, (max_score + min_score) / 2, max_score]
    plt.xticks([0, len(array) - 1], ['0', '1'])
    plt.yticks([0, len(array) - 1], ['1', '0'])
    plt.colorbar(ticks=ticks)
    plt.savefig(f'{stem}.png', dpi=800)
