#!/bin/python3
import os
import sys
import pkg_info
from pkg_info import *

#package = sys.argv[1]
#os.system("chmod 755 ./termux_pkg/DEBIAN/*")
#os.system("chmod 755 ./termux_pkg/DEBIAN")
#os.system(f"dpkg -b ./termux_pkg {package}")


pkg_data = open("./termux_pkg/DEBIAN/control", "r+")
pkg_data.write(f"Package: {TERMUX_PKG_NAME}\n")
pkg_data.write(f"Version: {TERMUX_PKG_VERSION}\n")
pkg_data.write(f"Architecture: {TERMUX_PKG_ARCH}\n")
pkg_data.write(f"Maintainer: {TERMUX_PKG_MAINTAINER}\n")
pkg_data.write(f"Installed-Size: {TERMUX_PKG_SIZE}\n")
pkg_data.write(f"Depends: {TERMUX_PKG_DEPENDS}\n")
pkg_data.write(f"Homepage: {TERMUX_PKG_HOMEPAGE}\n")
pkg_data.write(f"Description: {TERMUX_PKG_DESCRIPTION}\n")
pkg_data.close

print("Building package....")
os.system("chmod 755 ./termux_pkg/DEBIAN/*")
os.system("chmod 755 ./termux_pkg/DEBIAN")
os.system(f"dpkg-deb --build ./termux_pkg {TERMUX_PKG_NAME}_{TERMUX_PKG_VERSION}_{TERMUX_PKG_ARCH}.deb")
