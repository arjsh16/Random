class MyRange:
    def __init__(self, min_val, max_val, number):
        """
        Initializes the MyRange object.

        Args:
            min_val (int): The minimum value of the range.
            max_val (int): The maximum value of the range.
            number (int): The number to be brought within the range.
        """
        self.min = min_val
        self.max = max_val
        self.number = number

    def bring_in_range(self):
        """
        Brings the number within the specified range.

        Returns:
            int: The number within the range.
        """
        if self.number < self.max and self.number > self.min:
            return self.number
        else:
            if self.number < self.min:
                num = self.min + self.number
                if num > self.max or num < self.min:
                    return MyRange(self.min, self.max, num).bring_in_range()
                else:
                    return num 
            if self.number > self.max:
                num = self.number - self.max 
                if num < self.min or num > self.max:
                    return MyRange(self.min, self.max, num).bring_in_range()
                else:
                    return num
