""" test for HEIC photo type converter.

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

##################################################################################################
# Imports

import shlex
import pytest
from src.heic_multi_converter import main, check_src_dir, check_for_file_type


def test_shlex():
    """
    Testing shlex functionality
    """
    # I want to write this
    command = "--verboseOff -s '.\\doof'"

    # command parsers want this
    as_list = ["--verboseOff", "-s", ".\doof"]

    # shlex.split() does the work for me
    assert shlex.split(command) == as_list


test_cases_sys_exit = [
    ("", "error: the following arguments are required: -s"),  # no argument passed
    ("s", "error: the following arguments are required: -s"),  # no flag passed
    ("+s", "error: the following arguments are required: -s"),  # wrong type of flag passe
    ("-p", "error: the following arguments are required: -s"),  # wrong argument name
    (
        "-s .\testdata -t jpg",
        "error: argument -t/--type: invalid choice: 'jpg' (choose from 'png', 'jpeg')",
        # not supported picture type for argument -t
    ),
    (
        "-s .\testdata -t",
        "error: argument -t/--type: expected one argument",
    ),  # missing argument for option -t
    (
        "-s .\testdata -t jpeg -d",
        "error: argument -d/--destination: expected one argument",
    ),  # destination argument without data
]


@pytest.mark.parametrize("command, expected_output", test_cases_sys_exit)
def test_argparse_heic_multi_converter_sys_exit(capsys, command, expected_output):
    """
    This function test the argparse arguments handling

    Args:
        capsys (_type_): _description_
        command (str): the command line arguments for the test
        expected_output (str): the expected output depending for the test case
    """
    with pytest.raises(SystemExit):  # Expecting SystemExit due to argparse error
        main(shlex.split(command))
    captured = capsys.readouterr()  # Capture both stdout and stderr
    output = captured.err + captured.out  # Combine stdout and stderr
    assert expected_output in output


def test_that_source_folder_is_not_avail():
    """
    This function checks that a not existing source folder will result in a sys.exit(3)
    """
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        check_src_dir("./doof")
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 3


def test_if_picture_types_are_avail_in_source():
    """
    This function checks that no picture files in the handed over source folder will result in
    a sys.exit(4)
    """
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        check_for_file_type("./test")
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 4
