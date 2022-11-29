class Calculator: 

    def __init__(self):
        pass

    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def multi(self, *args):
        result = 1
        for number in args:
            if number == 0:
                raise ValueError
            result = result * number
        return result
    
    def division(self, a, b):
        if not b == 0:
            return float(a / b)
        return float("inf")

    def average(self, numbers, ut = None, lt = None):
        new_numbers = numbers
        if not ut == None:
            new_numbers = [i for i in new_numbers if i <= ut]
        if not lt == None:
            new_numbers = [i for i in new_numbers if i >= lt]
        if len(new_numbers) == 0:
            return 0
        return sum(new_numbers) / len(new_numbers) 