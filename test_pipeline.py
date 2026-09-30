import sys
sys.path.insert(0, "src")
from analysis import load_data, preprocess_data
import statistics

z = preprocess_data(load_data())
assert abs(statistics.mean(z)) < 1e-9, "mean of z-scores should be 0"
assert abs(statistics.pstdev(z) - 1.0) < 1e-9, "sd of z-scores should be 1"
print("OK")
