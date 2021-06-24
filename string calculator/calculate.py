def calculate(data: str) -> float:
    inputs = data.split(",")
    cast_inputs = [int(i) for i in inputs]
    return sum(cast_inputs)
