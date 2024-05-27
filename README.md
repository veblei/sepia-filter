# Sepia Filter

## Instapy

Instapy is a package that takes an image and runs it through a grayscale-
or sepia-filter based on the users input. The user can also choose between
four different implementations for the filters: pure python, numpy, numba,
or cython. Pure python is considerably slower than the other implementations.

## Dependencies

To install the package you have to navigate to the instapy-folder and run this
command:

    python3 -m pip install .

This package uses numpy, pillow, line-profiler, cython, and numba. To install
the dependencies (if you don't have them installed already) run this command:

    pip install numpy pillow line-profiler cython numba

## Usage

To use the package, be in the folder you downloaded the package and run this
command:

    python3 -m instapy <file>

There are also several flags you can add to the command to customize the
excecution and output. For more information run this command:

    python3 -m instapy -h