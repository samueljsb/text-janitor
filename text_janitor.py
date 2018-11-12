#! /usr/bin/env python3
"""
Text Janitor
Clean malicious code from text files in a directory.
Author: Samuel Searles-Bryant
Date: 2018-11-12
"""

import argparse
import os
import re
from binaryornot.check import is_binary

parser = argparse.ArgumentParser(
    description='Clean malicious code from text files in a directory.')
parser.add_argument('directory', type=str,
                    help='the directory containing the website')
parser.add_argument('output_dir', type=str,
                    help='the directory the edited files will be written to')
parser.add_argument('patterns', type=str,
                    help='file containing the regex patterns to remove')
args = parser.parse_args()

patterns = []
with open(args.patterns, 'r') as f:
    for line in f:
        regex = re.compile(line.strip())
        patterns.append(regex)

if args.output_dir:
    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)

for dir_name, sub_dir_list, file_list in os.walk(args.directory):
    rel_dir = os.path.relpath(dir_name, args.directory)
    output_dir = os.path.join(args.output_dir, rel_dir)
    for file_name in file_list:
        file_path = os.path.join(dir_name, file_name)
        if not is_binary(file_path):
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            with open(os.path.join(output_dir, file_name), 'w') as f_out:
                with open(file_path, 'r') as f_in:
                    try:
                        for line in f_in:
                            for regex in patterns:
                                line = regex.sub('', line)
                            f_out.write(line + '\n')
                    except UnicodeDecodeError:
                        pass
