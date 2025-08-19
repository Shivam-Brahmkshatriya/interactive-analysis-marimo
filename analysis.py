# analysis.py
# Author: Shivam
# Email: 23ds3000034@ds.study.iitm.ac.in
# This Marimo notebook demonstrates interactive data analysis with dependencies

import marimo as mo

# Cell 1: Import libraries and create synthetic dataset
# Data flow: This dataset will be used by later cells for analysis
import numpy as np
import pandas as pd

x = np.linspace(0, 10, 100)
y = 2 * x + np.random.normal(0, 1, 100)  # Linear relation with noise
data = pd.DataFrame({"x": x, "y": y})

# Cell 2: Create an interactive slider (must return it to render!)
# Data flow: The slider value will be used in the regression visualization
slider = mo.ui.slider(1, 50, label="Select sample size")
slider

# Cell 3: Dynamic subset of data based on slider
# Data flow: Depends on slider and dataset from Cell 1
sample = data.sample(slider.value)
sample.head()

# Cell 4: Display dynamic markdown output
# Data flow: Updates whenever slider value changes
mo.md(f"### Current sample size: {slider.value} \n\nShowing {slider.value} points 🟢")

# Cell 5: Plotting relationship between variables
# Data flow: Depends on sample created in Cell 3
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.scatter(sample["x"], sample["y"], color="blue", alpha=0.7, label="Sampled Data")
ax.set_xlabel("X variable")
ax.set_ylabel("Y variable")
ax.set_title("Interactive Relationship between X and Y")
ax.legend()
mo.mpl(fig)
