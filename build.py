#!/bin/python

import os

import sys

package = sys.argv[1]

os.system("chmod 755 ./builder/DEBIAN")

os.system(f"dpkg -b ./builder {package}")
