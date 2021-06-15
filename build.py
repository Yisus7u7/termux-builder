#!/bin/python

import os

import sys

package = sys.argv[1]

os.system("chmod 755 ./termux_pkg/DEBIAN/*")
os.system("chmod 755 ./termux_pkg/DEBIAN")

os.system(f"dpkg -b ./termux_pkg {package}")
