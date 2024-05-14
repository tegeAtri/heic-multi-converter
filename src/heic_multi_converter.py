""" HEIC photo type converter.

This script contverts all .heic files in a given folder into png or jpg in a defined
destination folder. The type of the resulting file is defined by an script argument.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "tegeAtri"
__authors__ = ["One developer", "And another one", "etc"]
__contact__ = "patrik.tegetmeier@web.de"
__copyright__ = "Copyright $YEAR, $COMPANY_NAME"
__credits__ = ["One developer", "And another one", "etc"]
__date__ = "2024/05/09"
__deprecated__ = False
__email__ = "patrik.tegetmeier@web.de"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.1.0"

###################################################################################################
# Imports

import os
import sys
import argparse
import logging
from PIL import Image
import pillow_heif


###################################################################################################
# Variables (always in capitals)

SUCCESS = 0
FAILED = 1

###################################################################################################
# Functions


def handle_arguments() -> list:
    """
    This function handles the command line arguments

    Returns:
        list: list of handed over command line arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="version : " + __version__ + ", author: " + __author__ + "date: " + __date__,
        help="show program's version, the author, and the version's data",
    )

    parser.add_argument(
        action="store",
        type=str.strip,
        help="the source path from where to load the MEIC typed \
            photos from, default is the current folder",
        dest="src",
        default="./",
    )

    parser.add_argument(
        action="store",
        type=str.strip,
        help="the destination path to where the converted photos shall \
            be stored, default is the current folder",
        dest="dest",
        default="./",
    )

    parser.add_argument(
        "-t",
        "--type",
        choices=["png", "jpeg"],
        default="png",
        dest="type",
        help="select the resulting photo tpye, png and jpeg are possible, default is png",
    )

    parser.add_argument(
        "--verboseOff",
        action="store_true",
        help="turn off the verbosity [default: verbosity on]",
        dest="verboff",
    )

    args: list = parser.parse_args()

    return args


def convert_heic(heic_pic) -> Image:
    """
    This function converts the heic typed picture into a PIL Image object

    Args:
        heic_pic (str): heic typed file including path information

    Returns:
        Image: object of type Image
    """
    logging.debug("heic file %s found", heic_pic)

    heif_file = pillow_heif.open_heif(heic_pic)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
    )

    return image


def handle_picture(input_pic, dest_loc, pic_type):
    """
    This function calls the heic conversion function and saves the
    PIL Image object into a image file typed by the selected type information.

    Args:
        input_pic (str): input heic file including the path to the picture
        dest_loc (str): destination path where the coverted picture shall be stored
        type (str): resuling picture file type
    """
    logging.debug("Source picture file name = %s", input_pic)
    pic_name = os.path.splitext(os.path.basename(input_pic))[0]

    logging.debug("Source picture basename = %s", pic_name)
    img: Image = convert_heic(input_pic)

    tup: tuple = (dest_loc, pic_name)
    img_name: str = "\\".join(tup)

    logging.info("Destination picture name = %s", img_name + "." + pic_type)
    img.save(img_name + "." + pic_type, format(pic_type))


def check_src_dir(src_path: str) -> bool:
    """
    This function checks if the named photo source directory exists

    Args:
        src_path (str): Source path where the heic typed photos shall be hosted

    Returns:
        bool: True if the source folder exists, otherwise False
    """
    success: bool = os.path.isdir(src_path)

    return success


def check_dest_dir(dest_path: str):
    """
    This function checks if the named photo destination directory exists. If
    it is not existing it will be created.

    Args:
        dest_path (str): Destination path where the resulting photos shall be stored to.
    """
    if os.path.isdir(dest_path) is False:
        try:
            os.makedirs(dest_path)
        except OSError as error:
            print(error)
            sys.exit(FAILED)


def main(arguments=None) -> None:
    """
    This function is the main function of the script.
    """
    arguments = handle_arguments()

    if arguments.verboff:
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.WARNING)
    else:
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)

    logging.info("Source location = %s", arguments.src)
    logging.info("Destination location = %s", arguments.dest)
    logging.info("Result photo type = %s", arguments.type)

    if check_src_dir(arguments.src) is False:
        logging.error("Source location is not existing")
        sys.exit(FAILED)

    check_dest_dir(arguments.dest)

    ext = (".heic", ".HEIC")
    for files in os.listdir(arguments.src):
        logging.info("Found file = %s", files)
        if files.endswith(ext):
            tup = (arguments.src, files)
            file: str = "\\".join(tup)
            handle_picture(file, arguments.dest, arguments.type)

    sys.exit(SUCCESS)


################################################################################
# Scripts
if __name__ == "__main__":
    main()
