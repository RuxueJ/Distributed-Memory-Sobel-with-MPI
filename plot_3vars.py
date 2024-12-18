"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot

Inputs: the named file "sample_data_3vars.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, ScalarFormatter
import numpy as np


fname = "sample_data_3vars.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

print("var names =", var_names)

# split the df into individual vars
# assumption: column order - 0=problem size, 1=blas time, 2=basic time

problem_sizes = df[var_names[0]].values.tolist()
# print(problem_sizes)
code1_time = df[var_names[1]].values.tolist()
# print(code1_time)
code2_time = df[var_names[2]].values.tolist()
# print(code2_time)
code3_time = df[var_names[3]].values.tolist()
# print(code3_time)
#



scatter_time = [36.29 / time for time in code1_time]
sobel_time = [ 51.18 / time for time in code2_time]
gather_time = [ 28.84 / time for time in code3_time]



xlocs = [i for i in range(len(problem_sizes))]

plt.figure(figsize=(10, 6))

plt.xticks(xlocs, problem_sizes)


plt.plot(scatter_time, "r-o")
plt.plot(sobel_time, "b-x")
plt.plot(gather_time, "g-^")


plt.xlabel("concurrency")
plt.ylabel("runtime speedup")
plt.title("Tile Slab: Speedup of Scatter, Sobel, and Gather Time")  # Set title for

#plt.xscale("log")
# plt.yscale("log")


# varNames = [ var_names[2], var_names[3]]
varNames = [var_names[1], var_names[2], var_names[3]]
plt.legend(varNames, loc="best")

plt.grid(axis='both')

plt.show()

# EOF
