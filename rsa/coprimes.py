import math
import random


def are_coprimes(a: int, b: int) -> bool:
    """Determina se dois números são coprimos.

    Números coprimos são números que não possuem divisor comum além de 1.

    Args:
        a (int): Um número.
        b (int): Outro número.

    Returns:
        bool: True se forem coprimos; Falso se não forem.
    """

    return math.gcd(a, b) == 1


def generate_coprime(n: int, lower_bound: int, upper_bound: int) -> int:
    """Gera um número coprimo ao número passado como argumento dentro de um intervalo.

    Args:
        n (int): Um número.
        lower_bound (int): Limite inferior do intervalo do número gerado.
        upper_bound (int): Limite superior do intervalo do número gerado.

    Returns:
        int: Um número coprimo ao número passado como argumento.
    """

    while True:
        candidate = random.randint(lower_bound, upper_bound)

        if are_coprimes(n, candidate):
            return candidate
