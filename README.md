# Thesis

## Purpose

This repo is for work related to our 4th year thesis project on network contagion modelling.
Specifically, we are using the Polya contagion model to allow for easy computation and micro level modelling (vs. macro level in more commonly used techniques sych as SIS).

## Current state
The project is currently able to

* Generate random networks
* Generate networks from edgelists or adjacency matrices
* Optimize exposure metric for time 1
* Run Polya contagion for n steps
* Plot contagion over time for given network
* Numerically check for a nash equilibrium

## Directories

The files are broken-up into the following directories

* data
    * Contains raw data files
* execute
    * Script to run a specific simulation
* Model
    * This is where the base class and function files are kept (ex. network, nodes, etc.)
* Notes
    * Notes on installation, and plotting (notes to self) so far
* Results
    * This is where data from simulations is saved
* Scripts
    * Bash scripts to facilitate installation of solvers
* Tests
    * Temporary simulation files
* Three-node
    * Small-scale simulation for a 3-node path graph
* Utilities
    * Various utilities for plotting, io, statistics, etc.