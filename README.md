# Random Number Generator

This Python script provides a simple random number generator along with a class to bring numbers within a specified range.

## Usage

To use the random number generator, you can import the `MyRandom` class and create an instance of it. You can then use its methods to generate random numbers.

```python
from random import *

# Create a random number generator object
rng = MyRandom()

# Generate a random integer
random_number = rng.random()

# Generate a random number within a range
random_range_number = rng.random_range(1, 10)
