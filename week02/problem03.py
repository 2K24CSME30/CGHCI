# Name: Kuldeep Kumar
# Roll number: 2K24/CSME/30
# GitHub username: 2K24CSME30
#
import numpy as np
# TODO 1: Added all 9 values, divide by 9, and round the answer.
def mean_filter_3x3(neighborhood: np.ndarray) -> int:
    """Return the rounded average of 9 pixels."""
    return int(round(float(np.sum(neighborhood)) / 9))

problem_3_input = np.array([[10, 20, 10], [30, 50, 30], [10, 20, 10]], dtype=np.uint8)

# TODO 2: Removed # symb
assert mean_filter_3x3(problem_3_input) == 21
print(mean_filter_3x3(problem_3_input))
