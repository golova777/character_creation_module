from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления'
           'квадратного корня из заданного числа')

print(message)


def calculate_square_root(number: float) -> float:
    """Calculate square root."""
    return float(sqrt(number))


def calc(your_number: float) -> None:
    """Print result of calculation."""
    if your_number <= 0:
        return

    result: float = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из '
          f'введённого вами числа. Это будет: {result}')


print(message)
calc(25.5)
