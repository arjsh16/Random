
import datetime
from range import *

class MyRandom:
    """
    A simple random number generator.
    """

    def __init__(self):
        """
        Initialize the random number generator.
        """
        self.seed = datetime.datetime.now().microsecond // 1000

    def random(self):
        """
        Generate a random integer.
        """
        self.seed = self.seed * 4 % 593
        return self.seed

    def random_range(self, min_val, max_val):
        """
        Generate a random number within a given range.
        
        Args:
            min_val (int): The minimum value of the range.
            max_val (int): The maximum value of the range.

        Returns:
            int: A random number within the specified range.
        """
        if min_val > max_val:
            return "Please provide a valid range.\n"
        elif min_val == max_val:
            return f"In the range {min_val} and {max_val}, this code will give:\n{max_val}"
        else:
            self.seed = self.seed * 4000 % 593
            rand_range = MyRange(min_val, max_val, self.seed)
            return rand_range.bring_in_range()
