#!/usr/bin/env python
from __future__ import print_function

import fnmatch
import os
import subprocess
import sys
import glob

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'src')

masks = ['*.h', '*.cc']

filenames = []
for root, dirnames, files in os.walk(path, path):
    for mask in masks:
        for filename in fnmatch.filter(files, mask):
            filenames.append(os.path.relpath(os.path.join(root, filename), path).replace('\\','/'))

cmake = """
# Auto-generated file. Do not edit
# Use update-sources.py

set(
    SOURCES
    """ + "\n    ".join(['${PROJECT_SOURCE_DIR}/src/' + f for f in filenames]) + """
)
"""

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sources.cmake'), "w") as f:
    f.write(cmake)
