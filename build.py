#!/bin/python

import os

import sys

package = sys.argv[1]

os.system("chmod 777 ./builder/DEBIAN")

os.system(f"dpkg -b ./builder {package}")