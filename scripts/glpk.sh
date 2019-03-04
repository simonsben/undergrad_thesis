#!/bin/bash

# Install required libraries
sudo apt update
sudo apt -y upgrade
sudo apt install -y build-essential gfortran

# Make ipopt directory
#mkdir ~/.glpk
#cd ~/.glpk

# Download and extract glpk
wget http://ftp.gnu.org/gnu/glpk/glpk-4.65.tar.gz
tar -xvzf glpk-4.65.tar.gz
cd glpk-4.65

# Create build directory
mkdir build
cd build/

# Run configure
../configure

# make
make

# Test
make check

# Install 
sudo make install

# Install additional library
sudo apt install libglpk-dev

