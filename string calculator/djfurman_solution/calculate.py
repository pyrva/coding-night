import re

def calculate(data: str) -> float:
    # Splits on comma OR newline into an interable
    inputs = re.split(",|\n", data)
    
    # List interpolation to cast each item as int
    cast_inputs = [int(i) for i in inputs]
    
    return sum(cast_inputs)  # sum everything in the list and return
