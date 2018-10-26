# Thesis

## Goals

* Generate network
* Simulate Polya

## Current task

* Need to refine plotting
  * Make new colormap to make more useful
  * Show colormap legend
  * Plot values
* Calculate network exposure
* Calculate more quantitative metrics
* Multi-thread polya runs (let us test on larger sets)
  * Structure already designed to make transition easy, just need to implement

## Design

Current ides is to store nodes in a list, with each node having initial balls, 
drawn balls, and neighbours. 

## Files

* Network
  * Contains class to generate and plot network
* Plot
  * Contains code to plot network and generate network (using built-in library for now)
* Polya
  * Contains code to run polya process on list of nodes
  * *NOTE* this is where the multi-threading should go
* Polya node
  * Contains class for nodes in polya network
* Utilities
  * Contains global *static* variables (functions to come)