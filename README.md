# How to Run

python main_module.py


# TODO
- fix known issues.
- generify variable naming in modules.
------> COMPLETE
- choose which regression to perform via command line argument
  - e.g. `python main_module.py "Hotel Occupancy Taxes Collected.csv" (-linear | -quadratic | -exponential)
------> FEATURE IMPLEMENTED - Sat. 12/2/2017
- save plot as an image file with a given name via command line argument.
  - e.g. `python main_module.py "Hotel Occupancy Taxes Collected.csv" (-linear | -quadratic | -exponential) ("Hotel Occupancy Taxes Collected.png")
------> FEATURED IMPLEMENTED - Sat. 12/2/2017


# Passing Command Line Arguments
- e.g. python main_module.py (inputFileName) (linear | exponential | quadratic) (outputFileName)

- Example: python main_module.py "Hotel Occupancy Taxes Collected.csv" "exponential" "outputPic.png"

# Known issues
- cannot plot projections because the "raw data", "model", and, "x-values" arrays will have different lengths.
------> Currently being worked on at this time - Sat. 12/2/2017