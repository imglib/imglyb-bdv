# imglyb-bdv

`imglyb-bdv` extends [imglyb](https://github.com/imglib/imglyb) with convenience
methods and structures from [BigDataViewer](https://github.com/bigdataviewer/bigdataviewer-core)

If you are interested in using `imglyb-bdv`, have a look at the `examples` folder
and extend the examples as needed!

## Installation

### Prerequisites

`imglyb-bdv` has been tested on Linux, macOS, and Windows.

The following tools are required:

 * Python 3
 * Java 8 or 11 JDK (JRE is not enough)
 * [Apache Maven](https://maven.apache.org/)

If you use [conda](https://conda.io/), these will be installed for you.

### Installing with conda

```shell
conda install -c conda-forge imglyb-bdv
```

### Installing with pip

First, install the prerequisites above. Then run:

```shell
pip install imglyb-bdv
```

It is recommended to do this from inside a virtualenv or conda environment,
rather than system-wide.

### Installing from source

First, install the prerequisites above. Then run:

```shell
git clone git://github.com/imglib/imglyb-bdv
cd imglyb-bdv
pip install -e .
```

It is recommended to do this from inside a virtualenv or conda environment,
rather than system-wide.

## Usage

It is suggested to follow and extend the examples in the `examples` folder
according to your needs. Note that the examples have additional dependencies
(`hdf5` and/or `dask`).

Or, for a higher-level way to use `imglyb`, check out
[pyimagej](https://github.com/imagej/pyimagej).
