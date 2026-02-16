### Seaborn Quickstart Example

Source: https://github.com/mwaskom/seaborn/blob/master/doc/installing.rst

Loads the 'penguins' dataset and creates a pairplot, coloring points by species. Requires matplotlib to display the plot.

```python
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")
sns.pairplot(df, hue="species")
plt.show()
```

--------------------------------

### Install Seaborn

Source: https://github.com/mwaskom/seaborn/blob/master/doc/installing.rst

Installs the official release of Seaborn from PyPI. This command also installs mandatory dependencies.

```bash
pip install seaborn
```

--------------------------------

### Seaborn Introduction and Installation

Source: https://github.com/mwaskom/seaborn/blob/master/doc/index.rst

Provides an overview of Seaborn, its purpose, and how to get started. It links to introductory notes, installation guides, example galleries, API references, tutorials, and release notes. It also mentions the GitHub repository for code and bug reporting, and Stack Overflow for support.

```APIDOC
Seaborn Overview:
  Purpose: High-level interface for drawing attractive and informative statistical graphics.
  Dependencies: matplotlib
  Resources:
    - Introductory Notes: tutorial/introduction
    - Installation Guide: installing
    - Example Gallery: examples/index
    - API Reference: api
    - Tutorials: tutorial
    - Releases: whatsnew/index
    - Citing: citing
    - FAQ: faq
  Support:
    - GitHub Repository: https://github.com/mwaskom/seaborn
    - Stack Overflow: https://stackoverflow.com/questions/tagged/seaborn/
```

--------------------------------

### Install Seaborn with Optional Dependencies

Source: https://github.com/mwaskom/seaborn/blob/master/doc/installing.rst

Installs Seaborn along with optional dependencies for advanced features, such as statistical analysis.

```bash
pip install seaborn[stats]
```

--------------------------------

### Basic Seaborn Setup and Data Loading

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/pointplot.ipynb

Initializes Seaborn with a whitegrid theme and loads the 'penguins' and 'flights' datasets. This is a common starting point for Seaborn visualizations.

```python
import seaborn as sns
sns.set_theme(style="whitegrid")
penguins = sns.load_dataset("penguins")
flights = sns.load_dataset("flights")
```

--------------------------------

### Basic Seaborn Setup and Data Loading

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/regplot.ipynb

Initializes Seaborn's default theme and loads the 'mpg' dataset. This is a common starting point for many Seaborn visualizations.

```python
import numpy as np
import seaborn as sns
sns.set_theme()
mpg = sns.load_dataset("mpg")
```

--------------------------------

### Install Seaborn using Conda

Source: https://github.com/mwaskom/seaborn/blob/master/doc/installing.rst

Installs Seaborn using the conda package manager. It's recommended to use the conda-forge channel for the latest releases.

```bash
conda install seaborn
conda install seaborn -c conda-forge
```

--------------------------------

### Initialize Seaborn Theme

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/kdeplot.ipynb

Initializes the Seaborn theme for enhanced plot aesthetics. This is a common setup step for Seaborn visualizations.

```python
import seaborn as sns; sns.set_theme()
```

--------------------------------

### Seaborn Initialization and Data Loading

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/categorical.ipynb

Initializes Seaborn with a theme, sets a random seed for reproducibility, and loads the 'tips' dataset. This is a common starting point for Seaborn visualizations.

```python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
np.random.seed(sum(map(ord, "categorical")))
```

```python
tips = sns.load_dataset("tips")
```

--------------------------------

### Common Seaborn Imports

Source: https://github.com/mwaskom/seaborn/blob/master/doc/installing.rst

Standard imports for Seaborn, including numpy, pandas, matplotlib, and seaborn.objects, often used in tutorials.

```python
import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
import seaborn.objects as so
```

--------------------------------

### Import Seaborn and Set Theme

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/introduction.ipynb

Imports the Seaborn library and applies the default theme for visualizations. This is a common starting point for Seaborn plots.

```python
# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()
```

--------------------------------

### Basic Plotting Setup

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/objects.Plot.scale.ipynb

Initializes a Seaborn plot with diamonds dataset and loads the mpg dataset.

```python
import seaborn.objects as so
from seaborn import load_dataset
diamonds = load_dataset("diamonds")
mpg = load_dataset("mpg").query("cylinders in [4, 6, 8]")
```

--------------------------------

### Basic Seaborn Setup and Data Loading

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/scatterplot.ipynb

Imports necessary libraries (numpy, pandas, seaborn, matplotlib) and sets the Seaborn theme. It then loads the 'tips' dataset from Seaborn and displays the first few rows.

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
```

```python
tips = sns.load_dataset("tips")
tips.head()
```

--------------------------------

### Basic Seaborn Setup and Histogram

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/histplot.ipynb

Initializes Seaborn with a white theme and loads the penguins dataset to create a basic histogram of flipper length.

```python
import seaborn as sns
sns.set_theme(style="white")

penguins = sns.load_dataset("penguins")
sns.histplot(data=penguins, x="flipper_length_mm")
```

--------------------------------

### Import Libraries and Setup

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/aesthetics.ipynb

Imports necessary libraries (NumPy, Seaborn, Matplotlib) and sets up the plotting environment for inline display and random seed initialization.

```python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

%matplotlib inline
np.random.seed(sum(map(ord, "aesthetics")))
```

--------------------------------

### Basic Seaborn Setup and Data Loading

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/relational.ipynb

Imports necessary libraries (numpy, pandas, matplotlib, seaborn) and sets the Seaborn theme to 'darkgrid'. It also loads the 'tips' dataset.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")
```

```python
%matplotlib inline
np.random.seed(sum(map(ord, "relational")))
```

```python
tips = sns.load_dataset("tips")
```

--------------------------------

### Seaborn Theme and Seed Setup

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/error_bars.ipynb

Initializes Seaborn with a darkgrid theme and sets a random seed for reproducibility.

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
sns.set_theme(style="darkgrid")

np.random.seed(sum(map(ord, "errorbars")))
```

--------------------------------

### Basic Seaborn Setup and Boxplot

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/boxplot.ipynb

Initializes Seaborn with a theme, loads the Titanic dataset, and creates a simple boxplot of the 'age' column.

```python
import seaborn as sns
sns.set_theme(style="whitegrid")
titanic = sns.load_dataset("titanic")
```

```python
sns.boxplot(x=titanic["age"])
```

--------------------------------

### Initialize Seaborn Theme

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/clustermap.ipynb

Sets the Seaborn theme for plots. This is a common starting point for Seaborn visualizations.

```python
import seaborn as sns
sns.set_theme()
```

--------------------------------

### Seaborn Plotting Setup

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/objects.Plot.on.ipynb

Initializes Seaborn plotting backend and loads the diamonds dataset for plotting examples. Sets the figure format to 'retina' for higher resolution.

```python
%config InlineBackend.figure_format = "retina"
import seaborn as sns
import seaborn.objects as so
import matplotlib as mpl
import matplotlib.pyplot as plt
from seaborn import load_dataset
diamonds = load_dataset("diamonds")
```

--------------------------------

### Seaborn Initialization and Data Loading

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/barplot.ipynb

Initializes Seaborn with a whitegrid theme and loads the 'penguins' and 'flights' datasets. This is a common setup for Seaborn visualizations.

```python
import seaborn as sns
sns.set_theme(style="whitegrid")
penguins = sns.load_dataset("penguins")
flights = sns.load_dataset("flights")
```

--------------------------------

### Setting Seaborn Theme and Displaying Colormaps

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/husl_palette.ipynb

Sets the default Seaborn theme and displays the colormap patches. This is a general setup for Seaborn visualizations.

```python
import seaborn as sns
sns.set_theme()
sns.palettes._patch_colormap_display()
```

--------------------------------

### Initialize Seaborn Theme and Load Dataset

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/move_legend.ipynb

Sets the Seaborn theme to 'darkgrid' and loads the 'penguins' dataset. This is a common setup for Seaborn visualizations.

```python
import seaborn as sns
sns.set_theme()
penguins = sns.load_dataset("penguins")
```

--------------------------------

### Install Seaborn with Documentation Dependencies

Source: https://github.com/mwaskom/seaborn/blob/master/doc/README.md

Installs Seaborn along with the additional dependencies required for building the documentation, including stats and docs packages.

```bash
pip install seaborn[stats,docs]
```

--------------------------------

### Initialize Seaborn Theme

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/pairplot.ipynb

Sets the visual theme for Seaborn plots to 'ticks'. This is a common starting point for customizing plot aesthetics.

```python
import seaborn as sns
sns.set_theme(style="ticks")
```

--------------------------------

### Generate Cubehelix Palette with Custom Start Value

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/cubehelix_palette.ipynb

Generates a cubehelix color palette with a custom starting point for the color rotation. The 'start' parameter influences the initial hue of the palette.

```python
sns.cubehelix_palette(start=2)
```

--------------------------------

### Initialize Seaborn Theme and Colormap Display

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/color_palette.ipynb

Sets the Seaborn theme to default and patches the colormap display for better visualization. This is a common setup step for Seaborn plots.

```python
import seaborn as sns
sns.set_theme()
sns.palettes._patch_colormap_display()
```

--------------------------------

### Initialize Seaborn Theme and Palette Display

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/cubehelix_palette.ipynb

Sets the Seaborn theme to default and patches the colormap display for better visualization. This is a common setup step for Seaborn visualizations.

```python
import seaborn as sns
sns.set_theme()
sns.palettes._patch_colormap_display()
```

--------------------------------

### Install Seaborn

Source: https://github.com/mwaskom/seaborn/blob/master/README.md

Installs the latest stable release of Seaborn and its dependencies from PyPI. It also shows how to install with optional statistical dependencies.

```bash
pip install seaborn

```

```bash
pip install seaborn[stats]

```

--------------------------------

### Seaborn Plot for Edge Properties Setup

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/properties.ipynb

Sets up a base Seaborn plot configuration, likely for demonstrating edge properties like `edgewidth` or `stroke`. It customizes the theme by removing specific spines and setting tick label sizes and margins.

```python
import seaborn as sns
import numpy as np

x = np.arange(0, 21) / 5
y = [0 for _ in x]
edge_plot = (
    sns.Plot(x, y)
    .layout(size=(9, .5), engine=None)
    .theme({
        **axes_style("ticks"),
        **{f"axes.spines.{side}": False for side in ["left", "right", "top"]},
        "xtick.labelsize": 12,
        "axes.xmargin": .02,
    })
    .scale(
        x=sns.Continuous().tick(every=1, minor=4),
        y=sns.Continuous().tick(count=0),
    )
)
```

--------------------------------

### Create and Use Named Color Palettes

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/color_palette.ipynb

Demonstrates creating color palettes using predefined names like 'pastel', 'husl', 'Set2', and 'Spectral'. It also shows how to get a palette as a colormap.

```python
sns.color_palette("pastel")
```

```python
sns.color_palette("husl", 9)
```

```python
sns.color_palette("Set2")
```

```python
sns.color_palette("Spectral", as_cmap=True)
```

--------------------------------

### Seaborn Theme and Palette Display

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/dark_palette.ipynb

Sets the Seaborn theme to default and patches the colormap display for palette visualization. This is a general setup for using Seaborn.

```python
import seaborn as sns
sns.set_theme()
sns.palettes._patch_colormap_display()
```

--------------------------------

### Matplotlib Figure Setup for Errorbar Visualization

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/error_bars.ipynb

Creates a Matplotlib figure with subplots to visually represent different errorbar types and their configurations.

```python
import io
from IPython.display import SVG
f = mpl.figure.Figure(figsize=(8, 5))
axs = f.subplots(2, 2, sharex=True, sharey=True,)

plt.setp(axs, xlim=(-1, 1), ylim=(-1, 1), xticks=[], yticks=[])
for ax, color in zip(axs.flat, ["C0", "C2", "C3", "C1"]):
    ax.set_facecolor(mpl.colors.to_rgba(color, .25))

kws = dict(x=0, y=.2, ha="center", va="center", size=18)
axs[0, 0].text(s="Standard deviation", **kws)
axs[0, 1].text(s="Standard error", **kws)
axs[1, 0].text(s="Percentile interval", **kws)
axs[1, 1].text(s="Confidence interval", **kws)

kws = dict(x=0, y=-.2, ha="center", va="center", size=18, font="Courier New")
axs[0, 0].text(s='errorbar=("sd", scale)', **kws)
axs[0, 1].text(s='errorbar=("se", scale)', **kws)
axs[1, 0].text(s='errorbar=("pi", width)', **kws)
axs[1, 1].text(s='errorbar=("ci", width)', **kws)

kws = dict(size=18)
axs[0, 0].set_title("Spread", **kws)
axs[0, 1].set_title("Uncertainty", **kws)
axs[0, 0].set_ylabel("Parametric", **kws)
axs[1, 0].set_ylabel("Nonparametric", **kws)

f.tight_layout()
f.subplots_adjust(hspace=.05, wspace=.05 * (4 / 6))
f.savefig(svg:=io.StringIO(), format="svg")
SVG(svg.getvalue())
```

--------------------------------

### Basic Plot Setup with Seaborn Objects

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/objects.KDE.ipynb

Initializes a Seaborn plot with the penguins dataset, mapping flipper length to the x-axis. This sets up the base for adding marks and transformations.

```python
import seaborn.objects as so
from seaborn import load_dataset
penguins = load_dataset("penguins")
```

--------------------------------

### Load Data and Initialize Plot

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/objects.Jitter.ipynb

Loads the 'penguins' dataset and initializes a Seaborn plot object. This is a common starting point for creating visualizations with seaborn.objects.

```python
import seaborn.objects as so
from seaborn import load_dataset
penguins = load_dataset("penguins")
```

--------------------------------

### Initialize FacetGrid

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/FacetGrid.ipynb

Loads the 'tips' dataset and initializes a FacetGrid without plotting anything. This sets up the grid structure based on the dataset.

```python
import seaborn as sns
tips = sns.load_dataset("tips")
g = sns.FacetGrid(tips)
```

--------------------------------

### Set Seaborn Theme and Display Colormap Patch

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/blend_palette.ipynb

Sets the default Seaborn theme and displays a patch for colormap display. This is a common setup for Seaborn visualizations.

```python
import seaborn as sns
sns.set_theme()
sns.palettes._patch_colormap_display()
```

--------------------------------

### Seaborn Theme and Palette Display

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/hls_palette.ipynb

Sets the Seaborn theme to default and patches the colormap display for better visualization. This is a common setup for using Seaborn.

```python
import seaborn as sns
sns.set_theme()
sns.palettes._patch_colormap_display()
```

--------------------------------

### Initialize Seaborn and Load Dataset

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/ecdfplot.ipynb

Initializes the seaborn theme and loads the penguins dataset, which is commonly used in seaborn examples.

```python
import seaborn as sns; sns.set_theme()
```

```python
penguins = sns.load_dataset("penguins")
```

--------------------------------

### Seaborn FacetGrid Initialization

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/function_overview.ipynb

Initializes a Seaborn FacetGrid with the penguins dataset.

```python
g = sns.FacetGrid(penguins)
```

--------------------------------

### Robust Seaborn Installation with Pip

Source: https://github.com/mwaskom/seaborn/blob/master/doc/faq.rst

Provides alternative methods for installing seaborn using pip to avoid environment-related import issues. It suggests using 'python -m pip install <package>' or '%pip install <package>' in Jupyter notebooks for more robust installations.

```python
python -m pip install seaborn
```

```jupyter
%pip install seaborn
```

--------------------------------

### Set Seaborn Theme and Display Colormap Patch

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/light_palette.ipynb

Sets the default Seaborn theme and displays a patch for colormap display. This is a common setup for Seaborn visualizations.

```python
import seaborn as sns
sns.set_theme()
sns.palettes._patch_colormap_display()
```

--------------------------------

### Set Seaborn Theme and Display Colormap Patch

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/mpl_palette.ipynb

Sets the default seaborn theme and displays a patch for colormap display. This is a common setup step for using seaborn's plotting functionalities.

```python
import seaborn as sns
sns.set_theme()
sns.palettes._patch_colormap_display()
```

--------------------------------

### Import Libraries and Set Theme

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/lineplot.ipynb

Imports necessary libraries (numpy, pandas, seaborn, matplotlib) and sets the Seaborn theme for enhanced plot aesthetics. This is a common setup for data visualization tasks.

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
sns.set_theme()
```

--------------------------------

### Initialize Seaborn Theme

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/data_structure.ipynb

Imports necessary libraries (NumPy, Pandas, Seaborn) and sets the Seaborn theme to 'darkgrid' for enhanced plot aesthetics.

```python
import numpy as np
import pandas as pd
import seaborn as sns
sns.set_theme()
```

--------------------------------

### Install Development Dependencies and Test Seaborn

Source: https://github.com/mwaskom/seaborn/blob/master/README.md

Installs additional dependencies required for testing Seaborn using the 'dev' extra. It also describes how to run tests and check code style.

```bash
pip install .[dev]

```

```bash
make test

```

```bash
make lint

```

```bash
pre-commit install

```

--------------------------------

### Load and Inspect Tips Dataset

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/relplot.ipynb

Loads the 'tips' dataset from Seaborn and displays the first few rows to understand its structure.

```python
tips = sns.load_dataset("tips")
tips.head()
```

--------------------------------

### Get Discrete Samples from Viridis Colormap

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/mpl_palette.ipynb

Retrieves discrete color samples from the 'viridis' colormap. By default, it returns a list of colors suitable for plotting.

```python
sns.mpl_palette("viridis")
```

--------------------------------

### Seaborn FacetGrid Initialization with Column Faceting

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/function_overview.ipynb

Initializes a Seaborn FacetGrid with the penguins dataset, faceting by the 'sex' column.

```python
g = sns.FacetGrid(penguins, col="sex")
```

--------------------------------

### Initialize Seaborn Theme and Load Data

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/PairGrid.ipynb

Sets the Seaborn theme to 'darkgrid' and loads the 'penguins' dataset for plotting.

```python
import seaborn as sns;
sns.set_theme();
import matplotlib.pyplot as plt;

penguins = sns.load_dataset("penguins");
g = sns.PairGrid(penguins);
g.map(sns.scatterplot);
```

--------------------------------

### Create Dark Palette from Color Name

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/dark_palette.ipynb

Generates a dark color palette starting from the color 'seagreen'. Seaborn infers the number of colors and format.

```python
sns.dark_palette("seagreen")
```

--------------------------------

### Import Libraries and Set Theme

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/function_overview.ipynb

Imports necessary libraries (numpy, pandas, seaborn, matplotlib, IPython.display) and sets the Seaborn theme to 'darkgrid'.

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import HTML
sns.set_theme()
```

--------------------------------

### Seaborn KDEplot Example

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/function_overview.ipynb

Generates a Kernel Density Estimate plot of flipper length for penguins, with different species distinguished by color and stacked.

```python
sns.kdeplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
```

--------------------------------

### Seaborn Displot Example (KDE)

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/function_overview.ipynb

Generates a figure-level Kernel Density Estimate plot of flipper length for penguins, with different species distinguished by color and stacked.

```python
sns.displot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack", kind="kde")
```

--------------------------------

### Initialize Seaborn Objects API

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/objects_interface.ipynb

Imports the seaborn.objects module, which provides a declarative interface for creating complex visualizations.

```python
import seaborn.objects as so
```

--------------------------------

### Get Viridis Colormap as a Matplotlib Colormap Object

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/mpl_palette.ipynb

Retrieves the 'viridis' colormap and returns it as a matplotlib colormap object, which can be used for continuous color mapping in plots.

```python
sns.mpl_palette("viridis", as_cmap=True)
```

--------------------------------

### Build Seaborn Documentation

Source: https://github.com/mwaskom/seaborn/blob/master/doc/README.md

Builds the Seaborn documentation, including converting Jupyter notebooks and generating gallery examples. The output will be located in the `_build/html` directory.

```bash
make notebooks html
```

--------------------------------

### Load Data and Initialize Plot

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/objects.Range.ipynb

Imports necessary libraries and loads the penguins dataset for plotting.

```python
import seaborn.objects as so
from seaborn import load_dataset
penguins = load_dataset("penguins")
```

--------------------------------

### Load Dataset and Create Relational Plot

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/introduction.ipynb

Loads the 'tips' dataset and creates a relational plot showing the relationship between 'total_bill' and 'tip', faceted by 'time' and styled by 'smoker'. Demonstrates basic data loading and plot creation.

```python
# Load an example dataset
tips = sns.load_dataset("tips")

# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)
```

--------------------------------

### Initialize Seaborn Theme

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/relplot.ipynb

Sets the visual theme for Seaborn plots to 'ticks' and imports necessary libraries for plotting.

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks")
```

--------------------------------

### Initialize Seaborn Theme

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/swarmplot.ipynb

Sets the visual theme for Seaborn plots to 'whitegrid'. This is a common first step in Seaborn visualizations.

```python
import seaborn as sns
sns.set_theme(style="whitegrid")
```

--------------------------------

### Annotated Plot Example

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/objects_interface.ipynb

Demonstrates creating a plot with annotations, including rectangles and text labels, using Matplotlib and Seaborn color palettes. This example illustrates mapping data to visual elements and adding explanatory text.

```python
from io import StringIO
from IPython.display import SVG
C = sns.color_palette("deep")
f = mpl.figure.Figure(figsize=(7, 3))
ax = f.subplots()
fontsize = 18
ax.add_artist(mpl.patches.Rectangle((.13, .53), .45, .09, color=C[0], alpha=.3))
ax.add_artist(mpl.patches.Rectangle((.22, .43), .235, .09, color=C[1], alpha=.3))
ax.add_artist(mpl.patches.Rectangle((.49, .43), .26, .09, color=C[2], alpha=.3))
ax.text(.05, .55, "Plot(data, 'x', 'y', color='var1')", size=fontsize, color=".2")
ax.text(.05, .45, ".add(Dot(pointsize=10), marker='var2')", size=fontsize, color=".2")
annots = [
    ("Mapped\nin all layers", (.35, .65), (0, 45)),
    ("Set directly", (.35, .4), (0, -45)),
    ("Mapped\nin this layer", (.63, .4), (0, -45)),
]
for i, (text, xy, xytext) in enumerate(annots):
    ax.annotate(
        text, xy, xytext,
        textcoords="offset points", fontsize=14, ha="center", va="center",
        arrowprops=dict(arrowstyle="->", color=C[i]), color=C[i],
    )
ax.set_axis_off()
f.subplots_adjust(0, 0, 1, 1)
f.savefig(s:=StringIO(), format="svg")
SVG(s.getvalue())
```

--------------------------------

### Seaborn Marker Plot Configuration

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/properties.ipynb

Configures a Seaborn plot for displaying markers. It sets the y-axis scale, theme properties like removing spines and adjusting tick label sizes, and margins. This setup is then used to add various marker styles.

```python
import seaborn as sns
import matplotlib as mpl
import numpy as np
from seaborn._core.properties import Marker

marker_plot = (
    sns.Plot()
    .scale(marker=None, y=sns.Continuous().tick(count=0))
    .layout(size=(10, .5), engine=None)
    .theme({
        **axes_style("ticks"),
        "axes.spines.left": False,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "xtick.labelsize":12,
        "axes.xmargin": .02,
    })
)
marker_mark = sns.Dot(pointsize=15, color=".2", stroke=1.5)
```

--------------------------------

### Initialize Seaborn with Matplotlib Inline

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/distributions.ipynb

Sets up the Seaborn environment for plotting within a Jupyter Notebook or similar environment by enabling matplotlib's inline backend and applying a default Seaborn theme.

```python
%matplotlib inline
import seaborn as sns; sns.set_theme()
```

--------------------------------

### Get 10 Discrete Samples from Set2 Palette

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/mpl_palette.ipynb

Retrieves exactly 10 discrete color samples from the 'Set2' qualitative palette. This allows for precise control over the number of colors used from a named palette.

```python
sns.mpl_palette("Set2", 10)
```

--------------------------------

### Initialize Seaborn Objects Plot

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/objects.Count.ipynb

Loads the 'tips' dataset and initializes a Seaborn objects Plot with 'day' on the x-axis.

```python
import seaborn.objects as so
from seaborn import load_dataset
tips = load_dataset("tips")
```

--------------------------------

### Seaborn Catplot Example

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/stripplot.ipynb

Illustrates the use of Seaborn's catplot function to create a faceted visualization. This example plots 'total_bill' against 'time', colored by 'sex', and creates separate columns ('col="day"') for each day, with a specified aspect ratio.

```python
sns.catplot(data=tips, x="time", y="total_bill", hue="sex", col="day", aspect=.5)
```

--------------------------------

### Get Default Discrete Samples from Set2 Palette

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/mpl_palette.ipynb

Retrieves discrete color samples from the predefined 'Set2' qualitative palette. The number of colors returned is determined by seaborn's default for this palette.

```python
sns.mpl_palette("Set2")
```

--------------------------------

### Initialize Seaborn Theme

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/heatmap.ipynb

Sets the default Seaborn theme for plots. This is often the first step when using Seaborn for visualization.

```python
import seaborn as sns
sns.set_theme()
```

--------------------------------

### Load Data and Initialize Plot

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/objects.Path.ipynb

Loads the 'healthexp' dataset and initializes a Seaborn plot object with specified aesthetics.

```python
import seaborn.objects as so
from seaborn import load_dataset
healthexp = load_dataset("healthexp").sort_values(["Country", "Year"])
```

--------------------------------

### Custom Plotting Function

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/aesthetics.ipynb

Defines a reusable function `sinplot` to generate sinusoidal plots, which is used throughout the examples to visualize styling changes.

```python
def sinplot(n=10, flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, n + 1):
        plt.plot(x, np.sin(x + i * .5) * (n + 2 - i) * flip)
```

--------------------------------

### Seaborn Displot Example (Column Faceting)

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/function_overview.ipynb

Generates a figure-level plot of flipper length for penguins, faceted by species into different columns.

```python
sns.displot(data=penguins, x="flipper_length_mm", hue="species", col="species")
```

--------------------------------

### Seaborn Pairplot Example

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/function_overview.ipynb

Generates a pairplot for the penguins dataset, showing pairwise relationships between numerical features, with points colored by species.

```python
sns.pairplot(data=penguins, hue="species")
```

--------------------------------

### Load Data and Create Basic Swarmplot

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/swarmplot.ipynb

Loads the 'tips' dataset and creates a basic swarm plot showing the distribution of 'total_bill'. This demonstrates the fundamental usage of swarmplot.

```python
tips = sns.load_dataset("tips")
sns.swarmplot(data=tips, x="total_bill")
```

--------------------------------

### Load Seaborn Datasets

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/objects_interface.ipynb

Loads various sample datasets provided by Seaborn, such as 'tips', 'penguins', 'diamonds', and 'healthexp'. It also demonstrates sorting and filtering the 'healthexp' dataset for specific use cases.

```python
import seaborn as sns
import matplotlib as mpl
tips = sns.load_dataset("tips")
penguins = sns.load_dataset("penguins").dropna()
diamonds = sns.load_dataset("diamonds")
healthexp = sns.load_dataset("healthexp").sort_values(["Country", "Year"])
healthexp = healthexp.query("Year <= 2020")
```

--------------------------------

### Install Seaborn with Pip

Source: https://github.com/mwaskom/seaborn/blob/master/doc/whatsnew/v0.2.0.rst

Installation via pip automatically handles most dependency requirements.

```bash
pip install seaborn
```

--------------------------------

### Applying Different Styles

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/aesthetics.ipynb

Demonstrates switching between various Seaborn styles ('dark', 'white', 'ticks') and visualizing the effect on the `sinplot`.

```python
sns.set_style("dark")
sinplot()

sns.set_style("white")
sinplot()

sns.set_style("ticks")
sinplot()
```

--------------------------------

### Get Default Color Palette

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/color_palette.ipynb

Retrieves the current default color palette used by Seaborn. This is useful for understanding the active color scheme.

```python
sns.color_palette()
```

--------------------------------

### Install Seaborn with Conda

Source: https://github.com/mwaskom/seaborn/blob/master/README.md

Installs Seaborn using the conda package manager. It notes that conda-forge typically updates releases faster than the main anaconda repository.

```bash
conda install seaborn

```

--------------------------------

### Matplotlib Subplots Initialization

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/function_overview.ipynb

Initializes a matplotlib figure and axes object for plotting.

```python
f, ax = plt.subplots()
```

--------------------------------

### Seaborn Scatterplot with Hue by Size

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/scatterplot.ipynb

Visualizes the 'tips' dataset with points colored according to the 'size' of the party.

```python
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="size")
```

--------------------------------

### Seaborn Histplot Example

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/function_overview.ipynb

Generates a histogram of flipper length for penguins, with different species distinguished by color and stacked.

```python
penguins = sns.load_dataset("penguins")
sns.histplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
```

--------------------------------

### Load and Display Flights Dataset

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/data_structure.ipynb

Loads the 'flights' dataset from Seaborn's built-in datasets and displays the first few rows using the .head() method.

```python
flights = sns.load_dataset("flights")
flights.head()
```

--------------------------------

### Seaborn Distribution Plot with KDE Overlay

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/distributions.ipynb

Generates a distribution plot for 'carat' with an overlaid Kernel Density Estimate curve.

```python
sns.displot(diamonds, x="carat", kde=True)
```

--------------------------------

### Line Plot with Hue and Style (Repeated Event)

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/relational.ipynb

Shows a line plot for 'fmri' data using 'hue' and 'style' for 'event', similar to a previous example.

```python
sns.relplot(
    data=fmri, kind="line",
    x="timepoint", y="signal", hue="event", style="event",
)
```

--------------------------------

### Seaborn Theme and Data Loading

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/axis_grids.ipynb

Sets the Seaborn theme to 'ticks' and loads the 'tips' dataset. Also includes matplotlib configuration for inline plotting and seeding NumPy for reproducibility.

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="ticks")

%matplotlib inline
import numpy as np
np.random.seed(sum(map(ord, "axis_grids")))
```

--------------------------------

### Seaborn Displot Example (Histogram)

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/function_overview.ipynb

Generates a figure-level histogram of flipper length for penguins, with different species distinguished by color and stacked.

```python
sns.displot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
```

--------------------------------

### Seaborn Plot Initialization and Layering

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/objects_interface.ipynb

Shows the basic initialization of a Seaborn plot object with data and aesthetic mappings. It then demonstrates how to add different plot layers like lines, areas, and stacks to an existing plot object.

```python
import seaborn.objects as so

# Assuming 'healthexp' dataset is loaded
# Example: healthexp = sns.load_dataset('healthexp')
p = so.Plot(healthexp, "Year", "Spending_USD", color="Country")

# Adding a line plot
p.add(so.Line())

# Adding an area plot with stacking
p.add(so.Area(), so.Stack())
```

--------------------------------

### Initialize Seaborn Theme

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/displot.ipynb

Sets the visual theme for Seaborn plots to 'ticks'. This is a common first step when creating plots with Seaborn.

```python
import seaborn as sns;
sns.set_theme(style="ticks")
```

--------------------------------

### Seaborn Scatterplot with Hue and Size Mapping

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/scatterplot.ipynb

Displays the 'tips' dataset with points colored by 'size' and sized proportionally to the 'size' of the party.

```python
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="size", size="size")
```

--------------------------------

### Seaborn regplot: Customized Plotting Options

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/regplot.ipynb

An example demonstrating several customization options for regplot, including confidence interval level, marker style, color, and line properties.

```python
sns.regplot(
    data=mpg, x="weight", y="horsepower",
    ci=99, marker="x", color=".3", line_kws=dict(color="r")
)
```

--------------------------------

### Seaborn FacetGrid Initialization with Column Faceting and Sizing

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/function_overview.ipynb

Initializes a Seaborn FacetGrid with the penguins dataset, faceting by the 'sex' column, and specifying height and aspect ratio.

```python
g = sns.FacetGrid(penguins, col="sex", height=3.5, aspect=.75)
```

--------------------------------

### FacetGrid with Histograms

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/axis_grids.ipynb

Creates a FacetGrid with histograms of 'tip' for each 'time' category in the 'tips' dataset. Demonstrates mapping a plotting function to the grid.

```python
tips = sns.load_dataset("tips")
g = sns.FacetGrid(tips, col="time")
g.map(sns.histplot, "tip")
```

--------------------------------

### Seaborn Color Blending Example

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/color_palettes.ipynb

Shows how to create a custom color palette by blending existing colors using Seaborn's `blend_palette` function. This example demonstrates blending a desaturated color with a base color and also blending multiple specified colors.

```python
c = sns.color_palette("muted")[0]
sns.blend_palette([sns.desaturate(c, 0), c], 8)
```

```python
sns.blend_palette([".1", c, ".95"], 8)
```

--------------------------------

### Querying Current Style

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/aesthetics.ipynb

Retrieves and displays the currently active Seaborn style settings.

```python
sns.axes_style()
```

--------------------------------

### Get Hex Codes of a Color Palette

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/color_palette.ipynb

Shows how to retrieve the hexadecimal color codes for a given Seaborn color palette, which can be useful for custom color definitions.

```python
print(sns.color_palette("pastel6").as_hex())
```

--------------------------------

### Create Dark Palette from Hex Code

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/dark_palette.ipynb

Generates a dark color palette starting from the hex color code '#79C'. Seaborn automatically converts the hex code.

```python
sns.dark_palette("#79C")
```

--------------------------------

### Initialize Seaborn Theme

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/JointGrid.ipynb

Sets the Seaborn theme to 'darkgrid' for enhanced plot aesthetics. This is a common first step in Seaborn visualizations.

```python
import seaborn as sns
sns.set_theme()
```

--------------------------------

### Create Dark Palette with Specific Number of Colors

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/dark_palette.ipynb

Generates a dark color palette starting from 'xkcd:golden' and specifies that the palette should contain 8 distinct colors.

```python
sns.dark_palette("xkcd:golden", 8)
```

--------------------------------

### Seaborn regplot: Weight vs. Acceleration

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_docstrings/regplot.ipynb

A basic example of using regplot to visualize the relationship between 'weight' and 'acceleration' from the 'mpg' dataset. It includes a linear regression model fit.

```python
sns.regplot(data=mpg, x="weight", y="acceleration")
```

--------------------------------

### Seaborn KDE Plot for Total Bill

Source: https://github.com/mwaskom/seaborn/blob/master/doc/_tutorial/distributions.ipynb

Visualizes the Kernel Density Estimate for the 'total_bill' column in the tips dataset.

```python
sns.displot(tips, x="total_bill", kind="kde")
```