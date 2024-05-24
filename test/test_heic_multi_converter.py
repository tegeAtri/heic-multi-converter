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
__version__ = "0.0.1"

################################################################################
# Imports
import pytest
from src.heic_multi_converter import main
import shlex

# test_cases = [
#     (
#         "-t png --verboseOff -s C:\git-repos\heic-multi-converter\testdataa -d C:\git-repos\heic-multi-converter\testdata",
#         "ERROR: Source location is not existing",
#     ),
#     (
#         "-t png --verboseOff -s C:\git-repos\heic-multi-converter\testdata -d C:\git-repos\heic-multi-converter\testdata",
#         "",
#     ),
# ]


# @pytest.mark.parametrize("command, expected_output", test_cases)
# def test_not_existing_src_folder_give_an_error(capsys, command, expected_output):
#     """
#     This function tests that heic-multi-converter returns an error if a non-existing
#     folder is handed over as source for photos.
#     """
#     main(shlex.split(command))
#     captured = capsys.readouterr()
#     output = captured.out + captured.err
#     assert expected_output in output


test_cases_sys_exit = [
    ("", "error: the following arguments are required: -s/--src"),  # no argument passed
    ("s", "error: the following arguments are required: -s/--src"),  # no flag passed
    ("+s", "error: the following arguments are required: -s/--src"),  # wrong type of flag passe
    ("-p", "error: the following arguments are required: -s/--src"),  # wrong argument name
    ("--verboseOff --src", "ERROR: Source location is not existing"),
]


@pytest.mark.parametrize("command, expected_output", test_cases_sys_exit)
def test_argparse_heic_multi_converter_sys_exit(capsys, command, expected_output):
    with pytest.raises(SystemExit):  # Expecting SystemExit due to argparse error
        main(shlex.split(command))
    captured = capsys.readouterr()  # Capture both stdout and stderr
    output = captured.err + captured.out  # Combine stdout and stderr
    assert expected_output in output
