# analysis.py
# Interactive Data Analysis with Marimo
# Author: 23ds3000034@ds.study.iitm.ac.in
#
# This notebook demonstrates how variable dependencies,
# widgets, and dynamic markdown work in Marimo.

import marimo

__generated_with__ = "0.1.0"
app = marimo.App()

# ------------------------------
# Cell 1: Import libraries and load data
# This is the data source used by later cells.
# ------------------------------
@app.cell
def __():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    return np, pd, plt

# ------------------------------
# Cell 2: Generate synthetic dataset
# dependent on numpy (from cell 1).
# ------------------------------
@app.cell
def __(np, pd):
    # Simple dataset: x uniformly spaced, y depends on slope
    x = np.linspace(0, 10, 100)
    base_slope = 2.0
    y = base_slope * x + np.random.normal(0, 2, size=x.shape[0])
    data = pd.DataFrame({"x": x, "y": y})
    data.head()
    return base_slope, data, x, y

# ------------------------------
# Cell 3: Interactive slider
# This adds interactivity: user controls slope.
# ------------------------------
@app.cell
def __():
    from marimo import widgets
    slope_slider = widgets.Slider(start=0.5, stop=5.0, step=0.5, value=2.0, label="Slope")
    slope_slider
    return slope_slider,

# ------------------------------
# Cell 4: Dependent variable update
# Uses slope_slider -> recompute regression line.
# ------------------------------
@app.cell
def __(x, slope_slider, np):
    slope = slope_slider.value
    y_new = slope * x
    (slope, y_new)
    return slope, y_new

# ------------------------------
# Cell 5: Visualization
# Depends on matplotlib and recomputed y values.
# ------------------------------
@app.cell
def __(plt, x, y, y_new, slope):
    fig, ax = plt.subplots()
    ax.scatter(x, y, alpha=0.5, label="Original Data")
    ax.plot(x, y_new, color="red", label=f"Fitted line (slope={slope})")
    ax.legend()
    ax.set_xlabel("X values")
    ax.set_ylabel("Y values")
    ax.set_title("Interactive Relationship between X and Y")
    fig
    return fig,

# ------------------------------
# Cell 6: Dynamic Markdown
# This dynamically shows slope value in rich text.
# ------------------------------
@app.cell
def __(slope):
    import marimo as mo
    mo.md(f"### Current slope selected: **{slope:.2f}**")
    return

if __name__ == "__main__":
    app.run()
