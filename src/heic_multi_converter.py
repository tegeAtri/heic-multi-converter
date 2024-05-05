""" Short description of this Python module.

Longer description of this module.

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
__date__ = "2024/05/02"
__deprecated__ = False
__email__ =  "patrik.tegetmeier@web.de"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"

################################################################################
# Imports
import os
import sys
import argparse
import logging
import time
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG,
    format="%(asctime)s - %(filename)s/%(funcName)s(%(lineno)d) - %(levelname)s - %(message)s")
logging.disable(logging.DEBUG)

start_time = time.time()

################################################################################
# Variables (always in capitals)
@dataclass
class ExitCodes:
    """
    This data class describes the exit codes
    """
    SUCCESS = 0
    FAILED = 1

################################################################################
# Functions

def handle_arguments() -> list:
    """
    This function handles the command line arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="version : " + __version__ + ", author: " + __author__ + "date: " + __date__,
        help="show program's version, the author, and the version's data"
    )

    parser.add_argument(
        action="store",
        type=str.strip,
        help="the source path from where to load the MEIC typed photos from, default is the current folder",
        dest="src",
        default="./"
    )

    parser.add_argument(
        action="store",
        type=str.strip,
        help="the destination path to where the converted photos shall be stored, default is the current folder",
        dest="dest",
        default="./"
    )

    parser.add_argument(
        "-t",
        "--type",
        choices=['png', 'jpeg'],
        default="png",
        dest="type",
        help="select the resulting photo tpye, png and jpeg are possible, default is png"
    )

    parser.add_argument(
        "--verboseOff",
        action="store_true",
        help="turn off the verbosity [default: verbosity on]",
        dest="verboff"
    )

    args: list = parser.parse_args()

    return args


def logger_example():
    """Example logging function

    """
    logging.info("This is an info message")
    logging.debug("This is an debug message")
    logging.warning("This is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")


def convert_meic(heic_pic):


def main():
    """
    This function is the main function of the script
    """
    arguments: list = handle_arguments()

    if arguments.verboff:
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.WARNING)
    else:
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)

    logging.info("Source location = %s", arguments.src)
    logging.info("Destination location = %s", arguments.dest)
    logging.info("Result photo type = %s", arguments.type)

    sys.exit(ExitCodes.SUCCESS)



################################################################################
# Scripts
if __name__ == "__main__":
    main()

