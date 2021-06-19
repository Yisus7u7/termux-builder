#!/bin/bash 
PKG="termux_pkg"
DATA="termux_builder_data.tar"
rm -rf ./$PKG
rm ./pkg_info.py
tar -xvf ./$DATA
echo "new project create now $PKG"
