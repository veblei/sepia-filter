"""Command-line (script) interface to instapy"""

import argparse
from cProfile import run
import sys

import numpy as np
from PIL import Image

from . import io
from instapy.python_filters import *
from instapy.numpy_filters import *
from instapy.numba_filters import *
from instapy.cython_filters import *
from instapy.timing import time_one


def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1,
    runtime: bool = False,
) -> None:
    """Run the selected filter"""
    # load the image from a file
    image = Image.open(file)
    if scale != 1:
        # Resize image, if needed
        image = image.resize((image.width // scale, image.height // scale))

    # Apply the filter
    pixels = np.asarray(image)
    func = globals()[f"{implementation}_{filter}"]
    filtered = func(pixels)

    # Runtime:
    if runtime:
        print(f"Average time over 3 runs: {time_one(func, pixels, 3):.3}s")
    
    if out_file:
        # save the file
        io.write_image(filtered, out_file)
    else:
        # not asked to save, display it instead
        io.display(filtered)


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()

    # filename is positional and required
    parser.add_argument("file", help="The filename to apply filter to")
    parser.add_argument("-o", "--out", help="The output filename")

    # Add required arguments
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-g", "--gray", help="Select gray filter", action="store_true")
    group.add_argument("-se", "--sepia", help="Select sepia filter", action="store_true")

    parser.add_argument("-sc", "--scale", help="Scale factor to resize image", type=int, default=1)
    parser.add_argument("-i", "--implementation", help="The implementation", choices=["python","numpy","numba","cython"], default="python")
    
    parser.add_argument("-r", "--runtime", help="Runtime of implementation", action="store_true")

    # parse arguments and call run_filter
    args = parser.parse_args()

    filter = None
    if args.gray:
        filter = "color2gray"
    elif args.sepia:
        filter = "color2sepia"

    runtime = False
    if args.runtime:
        runtime = True

    run_filter(args.file, args.out, args.implementation, filter, args.scale, runtime)