#!/bin/bash

# Install required libraries
sudo apt update
sudo apt -y upgrade
sudo apt install -y build-essential gfortran

# Make ipopt directory
mkdir ~/.ipopt
cd ~/.ipopt

# Download ipopt
wget https://www.coin-or.org/download/source/Ipopt/Ipopt-3.12.12.tgz

# Extract 
tar -xvzf Ipopt-3.12.12.tgz

# Install third party packages
cd Ipopt-3.12.12/ThirdParty
cd ASL
./get.ASL
cd ../Blas
./get.Blas
cd ../Lapack
./get.Lapack
cd ../Metis
./get.Metis
cd ../Mumps
./get.Mumps
cd ../..

# Make build directory
mkdir build
cd build/

# Run configure
../configure

# make
make

# Test
make test

# Install 
make install

