#!/bin/bash 
PKG="termux_pkg"
DATA="pkg_data.tar.xz"
rm -rf ./$PKG
tar -xvf ./$DATA

echo "new project create now $PKG"
