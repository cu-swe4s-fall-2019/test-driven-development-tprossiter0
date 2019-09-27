#Test Driven Development

## Purpose
This repository contains several modules that allow:
- computation of the arithemetic mean and standard deviation of a column from stdin
- plotting of this data in a boxplot, histogram, or both using matplotlib

This repository also contains viz.py, a script which combines the modules (math_lib.py, get_data.py, and data_viz.py)
which executes all of these with the corresponding input from a user

## Usage
- math_lib.py
 - list_mean
 Computes and returns arithmetic mean of a list of floats and/or integers. Takes in 1 list arg
 - list_stdev
 Computes and returns standard deviation of a list of floats and/or integers. Takes in 1 list arg

- get_data.py
 - read_stdin_col
 Returns a list of integers and float from a specified column given in stdin. Takes 1 integer to specify column index. (Also needs stdin data)

- data_viz.py
 - boxplot, histogram, combo
 All take arguments of (L, out_file_name). L = list of ints/floats. out_file_name = file in which to save the plot
 boxplot creates boxplot, histogram creates histogram, combo creates both

- viz.py
	Writes a data plot, mean, and stdev to an output file given the following informaton/arguments:

 Script that takes in 3 required arguments into argparse:
 	--plot_type : plot type (boxplot, histogram, combo ( <- both hist and boxplot ))
 	--out_file_name : name of output file to be created in which the specified plot will be saved 
 	--col_num : column number in stdin to read in



## Testing
For each module:
- math_lib.py
 - test_math_lib.py 
 provides unit testing of the list_mean() and list_stdev() methods

- get_data.py
 - test_get_data.py
 provides unit testing of read_stdin_col method

- data_viz.py
 - test_data_viz.py
 provides unit testing of plotting methods (boxplot(), histogram(), combo())

## Minimum Requirements to run

- Python 3.7.4
- matplotlib
- numpy
