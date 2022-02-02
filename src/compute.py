from src.lib import validateInputs


def add(a, b):
    validateInputs (a, b)
    return a + b


def subtract(a, b):
    validateInputs (a, b)
    return a - b


def multiply(a, b):
    validateInputs (a, b)
    return a * b


def divide(a, b):
    validateInputs (a, b)
    return a / b
