# How to Run
```
python main_module.py "Hotel Occupancy Taxes Collected.csv"
```

# TODO
- fix known issues.
- generify variable naming in modules.
- choose which regression to perform via command line argument
  - e.g. `python main_module.py "Hotel Occupancy Taxes Collected.csv" (-linear | -quadratic | -exponential)`
- save plot as an image file with a given name via command line argument.
  - e.g. `python main_module.py "Hotel Occupancy Taxes Collected.csv" (-linear | -quadratic | -exponential) ("Hotel Occupancy Taxes Collected.png")`

# Known issues
- cannot plot projections because the "raw data", "model", and, "x-values" arrays will have different lengths.
