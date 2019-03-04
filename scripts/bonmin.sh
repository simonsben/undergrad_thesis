#!/bin/bash

# Make folder
#mkdir ~/.bonmin
#cd ~/.bonmin

# Download solver
wget https://www.coin-or.org/download/source/Bonmin/Bonmin-1.8.7.tgz

# Extract files
tar -xvzf Bonmin-1.8.7.tgz
cd Bonmin-1.8.7

# Install Third Party packages
cd ThirdParty/ASL
./get.ASL
cd ../Blas
./get.Blas
cd ../Lapack
./get.Lapack
cd ../Metis
./get.Metis
cd ../Mumps
./get.Mumps

# Make build directory and configure solver
mkdir ../../build
cd ../../build
../configure

# Make, test, and install
make
make test
make install
