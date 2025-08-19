# analysis.py
# Interactive Data Analysis with Marimo
# Author: 23ds3000034@ds.study.iitm.ac.in
#
# Demonstrates variable dependencies, widgets, and dynamic markdown in Marimo.

import marimo

__generated_with__ = "0.1.0"
app = marimo.App()

# ------------------------------
# Cell 1: Import libraries
# ------------------------------
@app.cell
def __():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    return np, pd, plt

# ------------------------------
# Cell 2: Generate synthetic dataset
# ------------------------------
@app.cell
def __(np, pd):
    x = np.linspace(0, 10, 100)
    base_slope = 2.0
    y = base_slope * x + np.random.normal(0, 2, size=x.shape[0])
    data = pd.DataFrame({"x": x, "y": y})
    data.head()
    return base_slope, data, x, y

# ------------------------------
# Cell 3: Interactive slider
# ✅ FIXED: Must display the widget explicitly
# ------------------------------
@app.cell
def __():
    import marimo as mo
    slope_slider = mo.ui.slider(0.5, 5.0, step=0.5, value=2.0, label="Select slope")
    slope_slider  # displaying widget
    return slope_slider,

# ------------------------------
# Cell 4: Dependent values (line with chosen slope)
# ------------------------------
@app.cell
def __(x, slope_slider, np):
    slope = slope_slider.value
    y_new = slope * x
    (slope, y_new)  # returns recalculated slope line
    return slope, y_new

# ------------------------------
# Cell 5: Visualization
# ------------------------------
@app.cell
def __(plt, x, y, y_new, slope):
    fig, ax = plt.subplots()
    ax.scatter(x, y, alpha=0.5, label="Original Data")
    ax.plot(x, y_new, color="red", label=f"Fitted line (slope={slope:.2f})")
    ax.legend()
    ax.set_xlabel("X values")
    ax.set_ylabel("Y values")
    ax.set_title("Interactive Slope Fitting")
    fig
    return fig,

# ------------------------------
# Cell 6: Dynamic Markdown
# ✅ responds to slider changes
# ------------------------------
@app.cell
def __(slope):
    import marimo as mo
    mo.md(f"### Current slope selected: **{slope:.2f}**")
    return

if __name__ == "__main__":
    app.run()
