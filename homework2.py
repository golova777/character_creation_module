from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number: float) -> float:
    """Calculates square root of a number."""
    return sqrt(number)


def calc(your_number: float) -> None:
    """Generates output with calculated square roon of a number."""
    if your_number > 0:
        print(f'Мы вычислили квадратный корень из введённого вами числа. '
              f'Это будет: {calculate_square_root(your_number)}')


print(message)
calc(25.5)
