#!/usr/bin/env python
# encoding: utf-8
# vim: shiftwidth=4 expandtab
#
# phpbb-python © Copyright 2010 Santtu Pajukanta
# http://pajukanta.fi
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 or later of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://opensource.org/licenses/gpl-license.php>.
#

import sys
from pprint import pprint

STARTS_WITH = '<?php return array('
ENDS_WITH = ');'

HEADER = """
#
# WARNING! AUTOGENERATED FROM phpBB3/includes/utf/data/confusables.php
# DO NOT EDIT MANUALLY!
#
# Use phpbb-python/bin/process_confusables.py instead.
#

confusables = """

def parse_character(char):
    if not (char.startswith("'") and char.endswith("'")):
        raise ValueError(char)

    return char[1:-1].decode("UTF-8")

def parse_confusables(input_file):
    data = input_file.read()
    
    if not (data.startswith(STARTS_WITH) and data.endswith(ENDS_WITH)):
        raise ValueError

    data = data[len(STARTS_WITH):-len(ENDS_WITH)]

    for pair in data.split(','):
        try:
            before, after = pair.split('=>')
        except ValueError:
            continue

        before = parse_character(before)
        after = parse_character(after)

        yield (before, after)

def print_confusables(confusables, output_file):
    if type(confusables) is not dict:
        confusables = dict(confusables)

    output_file.write(HEADER)
    pprint(confusables, stream=output_file)

def main(input_filename, output_filename):
    with open(output_filename, 'wb') as output_file:
        with open(input_filename, 'rb') as input_file:
            print_confusables(parse_confusables(input_file), output_file)

if __name__ == "__main__":
    main(*sys.argv[1:])