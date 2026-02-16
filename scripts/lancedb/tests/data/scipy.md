### Simplify Pip Quickstart Guide

Source: https://docs.scipy.org/doc/scipy/-1.11.0/release/1.6.0-notes

This documentation update simplifies the quickstart guide for users installing SciPy via pip. The goal is to make the installation process more straightforward and accessible for new users.

```python
# DOC: simplified pip quickstart guide
# ... (rest of the commit message)
```

--------------------------------

### Simplify Pip Quickstart Guide

Source: https://docs.scipy.org/doc/scipy/-1.7.0/reference/release.1.6.0

This documentation change focuses on simplifying the quickstart guide for installing SciPy using pip. The goal is to make the installation process more accessible and straightforward for new users.

```markdown
```markdown
# SciPy Installation using Pip

To install the latest version of SciPy using pip, open your terminal or command prompt and run:

```bash
pip install scipy
```

This command will download and install SciPy along with its dependencies.

**Note:** For development versions or specific branches, you might need to install from source.
```
```

--------------------------------

### Update Ubuntu Quickstart Guide

Source: https://docs.scipy.org/doc/scipy/-1.11.0/release/1.6.0-notes

This documentation update revises the quickstart guide for Ubuntu users, noting that Conda compilers now work. This aims to improve the installation experience for Ubuntu users relying on Conda.

```python
# DOC: update Ubuntu quickstart; conda compilers now work!
# ... (rest of the commit message)
```

--------------------------------

### Install pip and Set Up Virtual Environment (Ubuntu)

Source: https://docs.scipy.org/doc/scipy/-1.6.0/reference/dev/contributor/quickstart_pip

Installs the pip package installer and demonstrates setting up a Python virtual environment using either virtualenvwrapper or the standard venv module. It emphasizes the importance of working within a virtual environment.

```bash
# Using virtualenvwrapper
python3 -m pip install virtualenvwrapper --user

export WORKON_HOME=$HOME/virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
. $HOME/.local/bin/virtualenvwrapper.sh
mkvirtualenv scipy-dev
# or
workon scipy-dev

# Using standard library venv
sudo apt install -y python3-venv

python3 -m venv scipy-dev
source $HOME/.venvs/scipy-dev/bin/activate
```

--------------------------------

### Update Ubuntu Quickstart; Conda Compilers Now Work

Source: https://docs.scipy.org/doc/scipy/-1.7.0/reference/release.1.6.0

This documentation update provides revised instructions for the Ubuntu quickstart guide, specifically noting that Conda compilers are now functional. This aims to improve the installation experience for Ubuntu users leveraging Conda.

```markdown
```markdown
# SciPy Quickstart Guide (Ubuntu with Conda)

This guide outlines the steps to install SciPy on Ubuntu, ensuring compatibility with Conda compilers.

1.  **Install Miniconda or Anaconda:** If you haven't already, download and install Miniconda or Anaconda for Linux.

2.  **Create a Conda environment (Recommended):**
    ```bash
    conda create -n scipy_env python=3.9
    conda activate scipy_env
    ```

3.  **Install SciPy:**
    ```bash
    conda install scipy
    ```
    *Alternatively, using pip within the Conda environment:*
    ```bash
    pip install scipy
    ```

**Note:** Recent updates ensure that Conda-managed compilers work seamlessly with SciPy installations.
```
```

--------------------------------

### Basinhopping Example Setup with NumPy and SciPy

Source: https://docs.scipy.org/doc/scipy/-1.11.1/reference/generated/scipy.optimize.basinhopping

This code snippet demonstrates the initial setup for using the `basinhopping` function. It imports necessary libraries, defines a sample function with multiple local minima, and sets an initial guess for the solution. This is a common starting point for global optimization problems.

```python
>>> import numpy as np
>>> from scipy.optimize import basinhopping
>>> func = lambda x: np.cos(14.5 * x - 0.3) + (x + 0.2) * x
>>> x0 = [1.]
```

--------------------------------

### Install Python Dependencies and Build SciPy

Source: https://docs.scipy.org/doc/scipy/-1.6.3/reference/dev/contributor/quickstart_pip

Installs essential Python development dependencies (numpy, pytest, cython, pybind11) within an active virtual environment and then builds the SciPy project from its source code using setup.py. Optionally includes running tests.

```bash
python -m pip install numpy pytest cython pybind11

python setup.py build

python runtests.py
```

--------------------------------

### Quickstart Guide Updates in SciPy

Source: https://docs.scipy.org/doc/scipy/-1.11.4/release/1.4.0-notes

General updates and improvements to the SciPy Quickstart Guide. This aims to provide users with a more current and helpful introduction to the library.

```markdown
# DOC: Quickstart Guide updates
```

--------------------------------

### Install System-Level Dependencies for SciPy Build (Ubuntu)

Source: https://docs.scipy.org/doc/scipy/-1.6.0/reference/dev/contributor/quickstart_pip

Installs necessary C, C++, and Fortran compilers, along with LAPACK libraries required for building SciPy on Ubuntu Linux.

```bash
sudo apt install -y gcc g++ gfortran
sudo apt install -y liblapack-dev
```

--------------------------------

### Set up Virtual Environment using virtualenvwrapper

Source: https://docs.scipy.org/doc/scipy/-1.8.1/dev/contributor/quickstart_pip

Demonstrates setting up a Python development environment using the `virtualenvwrapper` package. This involves installing the package, configuring environment variables in `.bashrc`, creating a new virtual environment, and activating it.

```bash
python3 -m pip install virtualenvwrapper --user

export WORKON_HOME=$HOME/virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
. $HOME/.local/bin/virtualenvwrapper.sh

mkvirtualenv scipy-dev
workon scipy-dev
```

--------------------------------

### Add Examples to optimize User Guide

Source: https://docs.scipy.org/doc/scipy/-1.11.3/release/1.9.0-notes

This entry indicates the addition of more examples to the user guide for the `optimize` module. These examples are intended to provide practical demonstrations of various optimization algorithms and techniques available in SciPy.

```python
from scipy.optimize import minimize
import numpy as np

# Example: Minimize a simple quadratic function
def objective(x):
    return x[0]**2 + x[1]**2

x0 = np.array([1.0, 1.0])
result = minimize(objective, x0, method='BFGS')

print("Optimization Result:", result)
```

--------------------------------

### Set up Virtual Environment using standard venv package

Source: https://docs.scipy.org/doc/scipy/-1.6.3/reference/dev/contributor/quickstart_pip

Installs the python3-venv package and demonstrates how to create and activate a virtual environment named 'scipy-dev' using Python's built-in venv module. This is an alternative to virtualenvwrapper.

```bash
sudo apt install -y python3-venv

python3 -m venv scipy-dev
source $HOME/.venvs/scipy-dev/bin/activate
```

--------------------------------

### Install Python Dependencies and Build SciPy

Source: https://docs.scipy.org/doc/scipy/-1.6.0/reference/dev/contributor/quickstart_pip

Installs essential Python packages like NumPy, pytest, Cython, and pybind11 within an activated virtual environment. It then proceeds to build the SciPy library from its source code.

```bash
python -m pip install numpy pytest cython pybind11

python setup.py build
```

--------------------------------

### Set Up SciPy Development Environment with Conda

Source: https://docs.scipy.org/doc/scipy/-1.11.4/dev/dev_quickstart

Instructions for creating and activating a Conda development environment for SciPy. This method ensures all necessary development dependencies are installed automatically.

```bash
# Create an environment with all development dependencies
mamba env create -f environment.yml  # works with `conda` too
# Activate the environment
mamba activate scipy-dev

```

--------------------------------

### Calculate Intervals and Setup Time Comparison

Source: https://docs.scipy.org/doc/scipy/-1.10.0/reference/generated/scipy.stats.sampling.NumericalInverseHermite

This example shows the number of intervals and the setup time for two `NumericalInverseHermite` instances with different `u_resolution` values. It demonstrates that a lower `u_resolution` (higher accuracy requirement) leads to more intervals and a longer setup time, illustrating the performance trade-off.

```python
rng1 = NumericalInverseHermite(dist, u_resolution=1e-10)
rng2 = NumericalInverseHermite(dist, u_resolution=1e-13)
print(f'Intervals for u_resolution=1e-10: {rng1.intervals}')
print(f'Intervals for u_resolution=1e-13: {rng2.intervals}')

time_res10 = timeit(lambda: NumericalInverseHermite(dist, u_resolution=1e-10), number=1)
time_res13 = timeit(lambda: NumericalInverseHermite(dist, u_resolution=1e-13), number=1)
print(f'Setup time for u_resolution=1e-10: {time_res10:.4f}s')
print(f'Setup time for u_resolution=1e-13: {time_res13:.4f}s')
```

--------------------------------

### Set up Virtual Environment using Python's venv module

Source: https://docs.scipy.org/doc/scipy/-1.8.1/dev/contributor/quickstart_pip

Illustrates creating and activating a Python virtual environment using the built-in `venv` module. This method is part of Python's standard library and requires installing the `python3-venv` package.

```bash
sudo apt install -y python3-venv

cd ~
python3 -m venv .venvs/scipy-dev
source $HOME/.venvs/scipy-dev/bin/activate
```

--------------------------------

### Set Up SciPy Development Environment with Conda

Source: https://docs.scipy.org/doc/scipy/-1.10.0/dev/dev_quickstart

Instructions for creating and activating a SciPy development environment using conda and the provided environment.yml file. This method automatically installs necessary compilers and Python development headers.

```bash
# Create an environment with all development dependencies
conda env create -f environment.yml  # works with `mamba` too
# Activate the environment
conda activate scipy-dev
```

--------------------------------

### 1D Minimization Problem Setup with Basinhopping

Source: https://docs.scipy.org/doc/scipy/-0.15.0/reference/generated/scipy.optimize.basinhopping

Sets up a one-dimensional minimization problem with a function `func` and an initial guess `x0`. This example demonstrates the initial setup for using `basinhopping` on a function with multiple local minima.

```python
func = lambda x: cos(14.5 * x - 0.3) + (x + 0.2) * x
x0=[1.]
```

--------------------------------

### Add Examples to SciPy IO Functions (mminfo, mmread, mmwrite)

Source: https://docs.scipy.org/doc/scipy/-1.11.1/release/1.10.0-notes

Introduces an 'Examples' section to the documentation for `scipy.io.mminfo`, `scipy.io.mmread`, and `scipy.io.mmwrite`. This guides users on how to read, write, and inspect Matrix Market files.

```python
from scipy.io import mmwrite, mmread
import numpy as np

# Create a sparse matrix
matrix = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])

# Write the matrix to a file
mmwrite('my_matrix.mtx', matrix)

# Read the matrix back
read_matrix = mmread('my_matrix.mtx')

print(read_matrix.toarray())
```

--------------------------------

### Set Up SciPy Development Environment with pip and venv

Source: https://docs.scipy.org/doc/scipy/-1.10.0/dev/dev_quickstart

Steps to set up a SciPy development environment using Python's venv module and pip. This requires system-level dependencies for compilers to be installed beforehand. It installs core development packages like numpy, pytest, and build tools.

```bash
# Create the virtual environment
python -m venv scipy-dev
# Activate the environment
source $HOME/.venvs/scipy-dev/bin/activate
# Install python-level dependencies
python -m pip install numpy pytest cython pythran pybind11 meson ninja
```

--------------------------------

### Alternative SciPy Development Setup with Symlink Install

Source: https://docs.scipy.org/doc/scipy/-0.11.0/reference/hacking

Demonstrates an alternative method for setting up a SciPy development version using a symlink installation, which can be useful for managing local packages.

```bash
python setupegg.py develop --prefix=${HOME}
```

--------------------------------

### Set Up SciPy Development Environment with Virtualenv

Source: https://docs.scipy.org/doc/scipy/-1.11.0/dev/dev_quickstart

This snippet shows how to set up a SciPy development environment using Python's built-in `venv` module. It includes creating the environment, activating it, and installing Python-level dependencies like NumPy, SciPy, and build tools.

```shell
# Create the virtual environment
python -m venv $HOME/.venvs/scipy-dev
# Activate the environment
source $HOME/.venvs/scipy-dev/bin/activate
# Install python-level dependencies
python -m pip install numpy pytest cython pythran pybind11 meson ninja pydevtool rich-click
```

--------------------------------

### Set up Virtual Environment using virtualenvwrapper

Source: https://docs.scipy.org/doc/scipy/-1.6.3/reference/dev/contributor/quickstart_pip

Installs the virtualenvwrapper package and configures environment variables in .bashrc to manage virtual environments for SciPy development. It includes commands to create and activate a new virtual environment named 'scipy-dev'.

```bash
python3 -m pip install virtualenvwrapper --user

export WORKON_HOME=$HOME/virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
. $HOME/.local/bin/virtualenvwrapper.sh

mkvirtualenv scipy-dev

workon scipy-dev
```

--------------------------------

### Set up SciPy Development Environment using Python's venv

Source: https://docs.scipy.org/doc/scipy/-1.7.0/dev/contributor/quickstart_pip

Details the process of setting up a Python development environment for SciPy using the built-in 'venv' module. This includes installing the venv package, creating a virtual environment directory, creating the environment, and activating it.

```bash
sudo apt install -y python3-venv

cd ~ 
mkdir .venvs
python3 -m venv scipy-dev

source $HOME/.venvs/scipy-dev/bin/activate
```

--------------------------------

### SciPy Install Plan JSON Example

Source: https://docs.scipy.org/doc/scipy/-1.10.1/dev/contributor/meson_advanced

This JSON snippet from 'intro-install_plan.json' shows the installation destination and tag for a compiled SciPy module (_decomp_update.cpython-310-x86_64-linux-gnu.so). It indicates where runtime files are placed within the build environment.

```json
"/home/username/code/scipy/build/scipy/linalg/_decomp_update.cpython-310-x86_64-linux-gnu.so":{
   "destination":"{py_platlib}/scipy/linalg/_decomp_update.cpython-310-x86_64-linux-gnu.so",
   "tag":"runtime"
}
```

--------------------------------

### Git Configuration File Example

Source: https://docs.scipy.org/doc/scipy/-1.5.1/reference/dev/gitwash/development_setup

An example of the content found in the .git/config file after setting up remotes and branch configurations. This file stores your local repository's settings.

```ini
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = false
[remote "origin"]
	url = https://github.com/your-user-name/scipy.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[remote "upstream"]
	url = https://github.com/scipy/scipy.git
	fetch = +refs/heads/*:refs/remotes/upstream/*
[branch "master"]
	remote = upstream
	merge = refs/heads/master
```

--------------------------------

### Build and Install SciPy using Spin Interface

Source: https://docs.scipy.org/doc/scipy/-1.17.0/building/compilers_and_options

Uses the 'spin' interface to build and install SciPy after initial configuration. This command assumes the project has already been configured, for example, using 'meson setup'.

```bash
spin -s linalg
```

--------------------------------

### Using stats.mstats.winsorize with No NaNs

Source: https://docs.scipy.org/doc/scipy/-1.17.0/tutorial/stats/outliers

Example of applying `stats.mstats.winsorize` to an array without NaN values, demonstrating the output after winsorization. The `.data` attribute is accessed to get the underlying NumPy array.

```python
stats.mstats.winsorize(x, (p, p), inclusive=(False, False)).data
```

--------------------------------

### Initialize DiscreteGuideTable with Guide Factor (Python)

Source: https://docs.scipy.org/doc/scipy/-1.15.2/tutorial/stats/sampling_dgt

Shows how to set the `guide_factor` parameter when initializing DiscreteGuideTable. A larger guide factor can lead to faster sampling but requires more setup time and memory.

```python
>>> guide_factor = 2
>>> rng = DiscreteGuideTable(pv, random_state=urng, guide_factor=guide_factor)
>>> rng.rvs()
2     # may vary
```

--------------------------------

### Activate SciPy Development Environment in Codespaces

Source: https://docs.scipy.org/doc/scipy/-1.11.0/dev/dev_quickstart

Once a SciPy Codespace is started, this command activates the pre-configured development environment. This allows you to immediately start building, testing, and developing SciPy within the browser-based environment.

```shell
mamba activate scipy-dev
```

--------------------------------

### Build and Test SciPy from Source

Source: https://docs.scipy.org/doc/scipy/-1.10.1/dev/dev_quickstart

Commands to build the SciPy project for development and run the full test suite. Assumes the development environment is already set up.

```bash
python dev.py build
python dev.py test

```

--------------------------------

### Update setup.

Source: https://docs.scipy.org/doc/scipy/-1.8.1/release.1.8.0

No description

--------------------------------

### Install SciPy Python Dependencies and Build

Source: https://docs.scipy.org/doc/scipy/-1.7.0/dev/contributor/quickstart_pip

Installs essential Python packages like NumPy, pytest, and Cython required for SciPy development within an active virtual environment. It then proceeds to build SciPy from source.

```bash
python -m pip install numpy pytest cython pythran pybind11

python setup.py build
```

--------------------------------

### Get example image (scipy.misc.lena)

Source: https://docs.scipy.org/doc/scipy/-0.17.1/reference/misc

The lena() function previously returned an example image. In newer versions, it might be deprecated or return a placeholder. Refer to specific SciPy version documentation for its current behavior.

```python
from scipy import misc

# The behavior of lena() might vary across SciPy versions.
# try:
#     lena_img = misc.lena()
#     print(lena_img.shape)
# except AttributeError:
#     print('lena() function not available or deprecated in this version.')
```

--------------------------------

### Add Examples to integrate.quadpack Documentation

Source: https://docs.scipy.org/doc/scipy/-1.15.3/release/1.9.0-notes

This documentation update includes new examples for the `integrate.quadpack` module, demonstrating how to perform numerical integration using its functions. This aims to make the module more accessible to users.

```python
from scipy.integrate import quadpack
import numpy as np

# Example usage of quadpack functions would go here
```

--------------------------------

### SciPy Module Setup Configuration

Source: https://docs.scipy.org/doc/scipy/-1.6.1/reference/api

Defines the configuration function for a SciPy module using numpy.distutils. This function is essential for building and installing the module as part of the SciPy package.

```python
def configuration(parent_package='', top_path=None):
    import numpy as np

    from numpy.distutils.misc_util import Configuration
    from numpy.distutils.command.build_src import build_src

    config = Configuration('yyy', parent_package, top_path)
    # Add subdirectories
    config.add_subdirs('tests')

    # Add modules
    config.add_library('yyy', sources=['yyy.c'])
    config.add_extension('yyy', sources=['yyy.c'])

    return config

```

--------------------------------

### Clone SciPy Repository and Set Up Remotes

Source: https://docs.scipy.org/doc/scipy/-1.10.0/dev/dev_quickstart

This snippet shows how to clone the SciPy repository from GitHub, update submodules, and add the upstream remote for contributing.

```bash
git clone git@github.com:YOURUSERNAME/scipy.git scipy
cd scipy
git submodule update --init
git remote add upstream https://github.com/scipy/scipy.git
```

--------------------------------

### Set Up SciPy Development Environment with Conda

Source: https://docs.scipy.org/doc/scipy/-1.11.0/dev/dev_quickstart

This section details how to create and activate a SciPy development environment using `mamba` (or `conda`). It installs all necessary development dependencies defined in `environment.yml`.

```shell
# Create an environment with all development dependencies
mamba env create -f environment.yml  # works with `conda` too
# Activate the environment
mamba activate scipy-dev
```

--------------------------------

### Build Source Distribution with Setup.py

Source: https://docs.scipy.org/doc/scipy/-1.3.0/reference/dev/index

An alternative method to build source archives using `python setup.py sdist`. This can be used if `pavement.py` causes issues, with manual steps for release notes.

```python
python setup.py sdist
```

--------------------------------

### View All Git Branches

Source: https://docs.scipy.org/doc/scipy/-1.4.0/reference/dev/gitwash/development_setup

Lists all local and remote branches available in your repository. This is useful for understanding the current branch and available remote tracking branches.

```bash
git branch -a
```

--------------------------------

### Initialize Git Submodules and Build SciPy

Source: https://docs.scipy.org/doc/scipy/-1.7.1/reference/dev/contributor/quickerstart_conda

This snippet covers initializing git submodules and building SciPy for development, including running tests. It provides two alternative commands for building SciPy.

```bash
# Initialize git submodules
git submodule update --init

# Build SciPy for development work plus run tests
python runtests.py    # Alternatively, it's fine to use `python setup.py develop`
```

--------------------------------

### Load and inspect ECG data using SciPy

Source: https://docs.scipy.org/doc/scipy/-1.15.2/reference/generated/scipy.datasets.electrocardiogram

Loads the electrocardiogram dataset using `scipy.datasets.electrocardiogram` and displays its shape, mean, and standard deviation. This is a basic example to get started with the dataset.

```python
>>> from scipy.datasets import electrocardiogram
>>> ecg = electrocardiogram()
>>> ecg
array([-0.245, -0.215, -0.185, ..., -0.405, -0.395, -0.385], shape=(108000,))
>>> ecg.shape, ecg.mean(), ecg.std()
((108000,), -0.16510875, 0.5992473991177294)
```

--------------------------------

### Add Examples to integrate.quadpack Documentation

Source: https://docs.scipy.org/doc/scipy/-1.11.3/release/1.9.0-notes

This update adds code examples to the documentation for functions within `integrate.quadpack`. These examples will help users understand how to use these numerical integration routines effectively.

```python
from scipy.integrate import quad
import numpy as np

# Example: Integrate a simple function from 0 to 1
def integrand(x):
    return x**2

result, error = quad(integrand, 0, 1)
print(f"Integral of x^2 from 0 to 1: {result}")

# Example: Integrate a more complex function
def complex_integrand(x):
    return np.sin(x) * np.exp(-x)

result_complex, error_complex = quad(complex_integrand, 0, np.pi)
print(f"Integral of sin(x)*exp(-x) from 0 to pi: {result_complex}")
```

--------------------------------

### Build Source Archives with Setup.py

Source: https://docs.scipy.org/doc/scipy/-1.6.1/reference/dev/core-dev/index

An alternative method to build source archives using 'python setup.py sdist'. This can be used if 'pavement.py' causes issues. Release notes tasks may need to be performed manually.

```bash
python setup.py sdist

```

--------------------------------

### View Git Remote Configuration

Source: https://docs.scipy.org/doc/scipy/-1.4.0/reference/dev/gitwash/development_setup

Displays the URLs for your configured Git remotes. This helps verify that both your fork ('origin') and the main repository ('upstream') are correctly linked.

```bash
git remote -v
```

--------------------------------

### InterpolatedUnivariateSpline Example in Python

Source: https://docs.scipy.org/doc/scipy/-0.13.0/reference/tutorial/interpolate

Demonstrates the creation and usage of InterpolatedUnivariateSpline. This spline always passes through all data points. It takes x and y data as input and can be called with new x-values to get interpolated y-values. The example includes plotting the interpolated spline against the original data and the true sine wave.

```python
x = np.arange(0,2*np.pi+np.pi/4,2*np.pi/8)
y = np.sin(x)
s = interpolate.InterpolatedUnivariateSpline(x,y)
xnew = np.arange(0,2*np.pi,np.pi/50)
ynew = s(xnew)
```

```python
plt.figure()
plt.plot(x,y,'x',xnew,ynew,xnew,np.sin(xnew),x,y,'b')
plt.legend(['Linear','InterpolatedUnivariateSpline', 'True'])
plt.axis([-0.05,6.33,-1.05,1.05])
plt.title('InterpolatedUnivariateSpline')
plt.show()
```

--------------------------------

### Differential Evolution: Constrained Minimization Setup

Source: https://docs.scipy.org/doc/scipy/-1.17.0/reference/generated/scipy.optimize.differential_evolution

Illustrates the setup for performing a constrained minimization using differential_evolution. It imports necessary classes for defining constraints and bounds.

```python
>>> from scipy.optimize import LinearConstraint, Bounds
```

--------------------------------

### Add Examples of Integrals to integrate.quadpack

Source: https://docs.scipy.org/doc/scipy/-1.11.2/release/1.9.0-notes

This documentation update adds examples demonstrating the use of integrals with the `integrate.quadpack` module, helping users understand its capabilities.

```python
DOC: Add examples of integrals to integrate.quadpack
```

--------------------------------

### Set up Intel Compilers

Source: https://docs.scipy.org/doc/scipy/-1.17.0/building/index

This section explains how to set up Intel compilers using their activation script. Running `setvars.bat` makes the Intel compilers available on the system path for use in the shell.

```shell
# Activate Intel oneAPI compilers
"C:\Program Files (x86)\Intel\oneAPI\setvars.bat"
```

--------------------------------

### Set Custom BLAS Distribution on Linux (Debian/Ubuntu)

Source: https://docs.scipy.org/doc/scipy/-1.9.3/dev/contributor/building_faq

This example illustrates how to install and set a custom BLAS library (OpenBLAS) on Debian/Ubuntu systems using `apt-get` and `update-alternatives`. It also shows how to preload a self-built BLAS library without administrator rights.

```bash
$ sudo apt-get install libopenblas-base libatlas3-base
$ sudo update-alternatives --set libblas.so.3 /usr/lib/openblas-base/libopenblas.so.0

# Preloading a self-built library:
$ LD_PRELOAD=/path/to/libatlas.so.3 ./my-application
```

--------------------------------

### InterpolatedUnivariateSpline Example

Source: https://docs.scipy.org/doc/scipy/-0.17.0/reference/tutorial/interpolate

Demonstrates creating and using an InterpolatedUnivariateSpline. This class ensures the spline passes through all provided data points. It takes x and y coordinates as input and can be called with new x-values to get interpolated y-values. The example also includes plotting the interpolated spline against the original data and the true sine function.

```python
x = np.arange(0, 2*np.pi+np.pi/4, 2*np.pi/8)
y = np.sin(x)
s = interpolate.InterpolatedUnivariateSpline(x, y)
xnew = np.arange(0, 2*np.pi, np.pi/50)
ynew = s(xnew)

plt.figure()
plt.plot(x, y, 'x', xnew, ynew, xnew, np.sin(xnew), x, y, 'b')
plt.legend(['Linear', 'InterpolatedUnivariateSpline', 'True'])
plt.axis([-0.05, 6.33, -1.05, 1.05])
plt.title('InterpolatedUnivariateSpline')
plt.show()
```

--------------------------------

### Example: Integration with Arguments

Source: https://docs.scipy.org/doc/scipy/-0.14.0/reference/generated/scipy.integrate.quad

Illustrates how to pass additional arguments to the integrand function using the `args` parameter in the `quad` function.

```APIDOC
## Example: Integration with Arguments

### Description
Demonstrate passing additional arguments to the integrand function.

### Request Example
```python
from scipy import integrate
f = lambda x, a: a * x
y, err = integrate.quad(f, 0, 1, args=(1,))
print(y)
y, err = integrate.quad(f, 0, 1, args=(3,))
print(y)
```

### Response Example
```
0.5
1.5
```
```

--------------------------------

### New Workflows: Building SciPy with Meson and meson-python

Source: https://docs.scipy.org/doc/scipy/building/distutils_equivalents

Illustrates commands for building and installing SciPy using the modern Meson and meson-python build systems. These commands are for setting up development environments and creating installable packages.

```bash
spin
```

```bash
pip install -e . --no-build-isolation
```

```bash
python -m build --no-isolation
pip install dist/scipy*.whl
```

```bash
pip install .
```

--------------------------------

### Get Sign of Gamma Function (Python)

Source: https://docs.scipy.org/doc/scipy/-1.5.3/reference/generated/scipy.special.gammasgn

Demonstrates how to use `scipy.special.gammasgn` to determine the sign of the gamma function for real arguments. It shows examples for positive and negative real numbers, illustrating its behavior.

```python
import scipy.special as sc

# It is 1 for x > 0.
print(sc.gammasgn([1, 2, 3, 4]))

# It alternates between -1 and 1 for negative integers.
print(sc.gammasgn([-0.5, -1.5, -2.5, -3.5]))
```

--------------------------------

### Get Unit of Physical Constant (Python)

Source: https://docs.scipy.org/doc/scipy/-1.1.0/reference/generated/scipy.constants.unit

Retrieves the unit of a physical constant from the `scipy.constants.physical_constants` dictionary using its string key. Requires the SciPy library to be installed. Returns a string representing the unit.

```python
from scipy import constants

# Example: Get the unit for 'proton mass'
unit_of_proton_mass = constants.unit(u'proton mass')
print(unit_of_proton_mass)  # Output: 'kg'
```

--------------------------------

### Example: Basic Integration

Source: https://docs.scipy.org/doc/scipy/-0.15.1/reference/generated/scipy.integrate.quad

Demonstrates a simple integration of a function `x^2` over finite limits and compares it with the analytical result.

```APIDOC
## Example: Basic Integration

### Description
This example shows how to calculate the definite integral of `x^2` from 0 to 4 using `scipy.integrate.quad` and verifies the result against the analytical solution.

### Method
`scipy.integrate.quad(func, a, b, ...)`

### Endpoint
`integrate.quad`

### Request Example
```python
from scipy import integrate
x2 = lambda x: x**2
result = integrate.quad(x2, 0, 4)
print(result)
# Expected output: (21.333333333333332, 2.3684757858670003e-13)
print(4**3 / 3.)  # analytical result
# Expected output: 21.3333333333
```
```

--------------------------------

### Fix `scipy.signal.lsim2` Docstring Example

Source: https://docs.scipy.org/doc/scipy/-1.9.3/release.1.5.0

This documentation update unifies the examples for `scipy.signal.lsim` and `scipy.signal.lsim2`. By providing a consistent and clear example, users can more easily understand and apply both functions for simulating linear time-invariant systems, reducing confusion between the two.

```python
# Conceptual update to unify examples for lsim and lsim2
# The example code in the docstrings of both functions will be made consistent
# to demonstrate similar system responses and usage patterns.
```

--------------------------------

### Fast Setup for Multiple Gamma Distributions in Python

Source: https://docs.scipy.org/doc/scipy/-1.9.3/tutorial/stats/sampling_srou

Illustrates the advantage of SimpleRatioUniforms for fast setup when generating samples from distributions with varying shape parameters, such as the Gamma distribution. It iterates through different shape parameters, initializes SROU for each, and generates samples.

```python
import math
from scipy.stats.sampling import SimpleRatioUniforms
import numpy as np

class GammaDist:
    def __init__(self, p):
        self.p = p
    def pdf(self, x):
        # Avoid potential warnings for x=0 when p<1
        if x == 0 and self.p < 1:
            return 0.0
        return x**(self.p-1) * np.exp(-x)

urng = np.random.default_rng()
p = np.arange(1.5, 5, 0.003) # Adjusted step for more parameters
res = np.empty((len(p), 100))

for i in range(len(p)):
    dist = GammaDist(p[i])
    # Mode for Gamma(p) is p-1
    mode = p[i] - 1
    # PDF area for Gamma(p) is Gamma(p)
    pdf_area = math.gamma(p[i])
    
    rng = SimpleRatioUniforms(dist, mode=mode,
                              pdf_area=pdf_area,
                              random_state=urng)
    
    # Suppress warnings that might arise from numerical issues with extreme values
    with np.suppress_warnings() as sup:
        sup.filter(RuntimeWarning, "invalid value encountered in double_scalars")
        sup.filter(RuntimeWarning, "overflow encountered in exp")
        res[i] = rng.rvs(100)

# 'res' now contains 100 samples for each of the 1000 different Gamma distributions.
```

--------------------------------

### Constrained Minimization Setup

Source: https://docs.scipy.org/doc/scipy/-0.11.0/reference/generated/scipy.optimize.minimize

Sets up a constrained minimization problem by defining the objective function and inequality constraints. This is a precursor to using optimization methods that handle constraints.

```python
fun = lambda x: (x[0] - 1)**2 + (x[1] - 2.5)**2
cons = ({'type': 'ineq', 'fun': lambda x:  x[0] - 2 * x[1] + 2})
```

--------------------------------

### Add Examples for SciPy Stats Mode Docstring

Source: https://docs.scipy.org/doc/scipy/-1.9.1/release.1.5.0

This documentation update adds examples to the docstring of `scipy.stats.mode`. This provides users with clear, executable examples demonstrating how to use the function and interpret its output.

--------------------------------

### Add Pybind11 to SciPy Quickstart Guides

Source: https://docs.scipy.org/doc/scipy/-1.11.4/release/1.4.0-notes

Documentation update to include `pybind11` in the relevant sections of the SciPy quickstart guides. This informs users about its role, likely in building extensions.

```markdown
# DOC: add pybind11 to the other part of quickstart guides
```

--------------------------------

### SLSQP with Inequality and Equality Constraints

Source: https://docs.scipy.org/doc/scipy/-1.15.2/tutorial/optimize

Shows how to set up and solve a constrained minimization problem using the 'SLSQP' method. This example defines both inequality and equality constraints using dictionaries, specifying their type, function, and Jacobian. It also includes bounds for the variables.

```python
import numpy as np
from scipy.optimize import minimize

# Assume rosen, rosen_der, bounds are defined

ineq_cons = {'type': 'ineq',
             'fun' : lambda x: np.array([1 - x[0] - 2*x[1],
                                         1 - x[0]**2 - x[1],
                                         1 - x[0]**2 + x[1]]),
             'jac' : lambda x: np.array([[-1.0, -2.0],
                                         [-2*x[0], -1.0],
                                         [-2*x[0], 1.0]])}
eq_cons = {'type': 'eq',
            'fun' : lambda x: np.array([2*x[0] + x[1] - 1]),
            'jac' : lambda x: np.array([2.0, 1.0])}

x0 = np.array([0.5, 0])
res = minimize(rosen, x0, method='SLSQP',
               jac=rosen_der,
               constraints=[eq_cons, ineq_cons], options={'ftol': 1e-9, 'disp': True},
               bounds=bounds)
```

--------------------------------

### Improve SciPy Signal Module Examples

Source: https://docs.scipy.org/doc/scipy/-1.9.1/release.1.5.0

This update focuses on enhancing the documentation for the SciPy signal module by unifying and correcting examples for functions like `lsim` and `lsim2`. It also includes adding examples for `qspline1d` and `qspline_eval`, and fixing ODE-related examples in `impulse` and `impulse2` docstrings.

```python
# Example for scipy.signal.lsim2 (unified with lsim)
import numpy as np
from scipy.signal import lsim2

t = np.linspace(0, 1, 100)
# Define system matrices A, B, C, D
A = np.array([[-1, -2], [3, -4]])
B = np.array([[1], [0]])
C = np.array([[0, 1]])
D = np.zeros((1, 1))

# Define input signal u
u = np.sin(t)

t_out, y_out, x_out = lsim2((A, B, C, D), u, t)
# Plotting or further analysis of y_out and x_out would follow
```

```python
# Example for scipy.signal.qspline1d and qspline_eval
import numpy as np
from scipy.signal import qspline1d, qspline_eval

x = np.array([0, 1, 2, 3])
y = np.array([0, 1, 0, -1])
# Compute the spline coefficients
cs = qspline1d(x, y)

# Evaluate the spline at new points
x_new = np.linspace(0, 3, 50)
y_new = qspline_eval(cs, x, x_new)
# Plotting or further analysis of y_new would follow
```

```python
# Example for scipy.signal.impulse and impulse2 (corrected ODE)
import numpy as np
from scipy.signal import impulse, impulse2

# Define system matrices A, B, C, D
A = np.array([[-1, -2], [3, -4]])
B = np.array([[1], [0]])
C = np.array([[0, 1]])
D = np.zeros((1, 1))

# Calculate impulse response
t_out, y_out = impulse((A, B, C, D))
# Plotting or further analysis of y_out would follow

# Similar calculation for impulse2
```

--------------------------------

### Build SciPy and Run Tests

Source: https://docs.scipy.org/doc/scipy/-1.11.0/dev/dev_quickstart

This command builds the SciPy project, including recompiling any necessary C/C++/Fortran extensions, and then executes the test suite. It's a convenient way to ensure your changes integrate correctly.

```shell
python dev.py test  # this will always (re)build as needed first
```

--------------------------------

### Example Git Configuration File

Source: https://docs.scipy.org/doc/scipy/-1.10.1/dev/gitwash/development_setup

Illustrates the content of a local Git configuration file (`.git/config`) after setting up remotes and branch tracking for the SciPy repository. It shows the 'origin' and 'upstream' remote configurations and the 'main' branch settings.

```ini
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
        ignorecase = true
        precomposeunicode = false
[remote "origin"]
        url = https://github.com/your-user-name/scipy.git
        fetch = +refs/heads/*:refs/remotes/origin/*
[remote "upstream"]
        url = https://github.com/scipy/scipy.git
        fetch = +refs/heads/*:refs/remotes/upstream/*
[branch "main"]
        remote = upstream
        merge = refs/heads/main
```

--------------------------------

### Cython Optimize Zeros Example

Source: https://docs.scipy.org/doc/scipy/-1.9.1/reference/optimize.cython_optimize

Provides a comprehensive example of using `scipy.optimize.cython_optimize` by defining a Cython `.pyx` file, importing a root finder, writing a callback function with a user-defined struct, and creating wrapper and Python functions to execute the solver.

```APIDOC
## Example Usage of cython_optimize

### Description
Demonstrates the steps required to use `scipy.optimize.cython_optimize`, including creating a Cython file, defining a callback, and calling a root-finding function.

### Method
Cython Compilation and Execution

### Endpoint
N/A

### Parameters
#### Path Parameters
None

#### Query Parameters
None

#### Request Body
(Not applicable for this example, as it involves file creation and compilation)

### Request Example
1. **Create a Cython `.pyx` file (e.g., `myexample.pyx`):**
```python
from scipy.optimize.cython_optimize cimport brentq
from libc cimport math

myargs = {'C0': 1.0, 'C1': 0.7}  # a dictionary of extra arguments
XLO, XHI = 0.5, 1.0  # lower and upper search boundaries
XTOL, RTOL, MITR = 1e-3, 1e-3, 10  # other solver parameters

# user-defined struct for extra parameters
ctypedef struct test_params:
    double C0
    double C1


# user-defined callback
cdef double f(double x, void *args):
    cdef test_params *myargs = <test_params *> args
    return myargs.C0 - math.exp(-(x - myargs.C1))


# Cython wrapper function
cdef double brentq_wrapper_example(dict args, double xa, double xb,
                                   double xtol, double rtol, int mitr):
    # Cython automatically casts dictionary to struct
    cdef test_params myargs = args
    return brentq(
        f, xa, xb, <test_params *> &myargs, xtol, rtol, mitr, NULL)


# Python function
def brentq_example(args=myargs, xa=XLO, xb=XHI, xtol=XTOL, rtol=RTOL,
                   mitr=MITR):
    """Calls Cython wrapper from Python."""
    return brentq_wrapper_example(args, xa, xb, xtol, rtol, mitr)
```

2. **Compile the Cython file.**

3. **Call the function from Python:**
```python
from myexample import brentq_example

x = brentq_example()
# Expected output: 0.6999942848231314
```

### Response
#### Success Response (Execution)
- **x** (double) - The root found by the `brentq` solver.

#### Response Example
```
0.6999942848231314
```
```

--------------------------------

### Get Unit of Physical Constant (Python)

Source: https://docs.scipy.org/doc/scipy/-0.17.0/reference/generated/scipy.constants.unit

Retrieves the unit of a physical constant from the scipy.constants module using its key. Requires the SciPy library to be installed. Takes a string key as input and returns a string representing the unit.

```python
from scipy import constants

# Example: Get the unit for 'proton mass'
unit = constants.unit(u'proton mass')
print(unit)  # Output: 'kg'
```

--------------------------------

### Add Examples to SciPy I/O Module Documentation (Python)

Source: https://docs.scipy.org/doc/scipy/-1.12.0/release/1.10.0-notes

Introduces new 'Examples' sections to the docstrings of functions within the `scipy.io` module, specifically for `mminfo`, `mmread`, `mmwrite`, and `whosmat`. This aims to provide practical usage demonstrations for these I/O functions.

```python
from scipy.io import mmread, mmwrite

# Example for mmread and mmwrite
# ... (example code) ...
```

```python
from scipy.io import whosmat

# Example for whosmat
# ... (example code) ...
```

--------------------------------

### Get Non-Zero Indices of Sparse Matrix (Python)

Source: https://docs.scipy.org/doc/scipy/-0.14.0/reference/generated/scipy.sparse.coo_matrix.nonzero

Retrieves the indices of non-zero elements from a SciPy sparse matrix. This is useful for understanding the structure and accessing specific elements of the matrix. It requires the SciPy library to be installed.

```python
from scipy.sparse import csr_matrix
A = csr_matrix([[1,2,0],[0,0,3],[4,0,5]])
A.nonzero()
```