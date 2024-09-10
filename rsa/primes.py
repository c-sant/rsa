import random


def generate_prime(bits: int, max_iterations: int = None) -> int:
    """Gera um número primo do tamanho especificado.

    Se um número máximo de iterações for definido e alcançado, levanta uma exceção
    para evitar um possível loop infinito.

    Args:
        bits (int): Tamanho do número desejado em bits.
        max_iterations (int, optional): Número máximo de iterações.

    Raises:
        Exception: Se o número máximo de iterações for definido e alcançado.

    Returns:
        int: Um número primo aleatório do tamanho especficado.
    """

    i = 0
    while (max_iterations is None) or (i <= max_iterations):
        candidate = _generate_random_odd_number(bits)

        if is_prime(candidate):
            return candidate

    raise Exception(
        f"Couldn't generate a prime number under {max_iterations} iterations."
    )


def is_prime(n: int, k: int = 40) -> bool:
    """Determina se um número é primo ou não.

    Utiliza a abordagem probabilística de Miller-Rabin para determinar se um
    número é primo ou não.

    Args:
        n (int): Um número que pode ou não ser primo.
        k (int, optional): Número de iterações de teste. Controla a precisão e a
        confiabilidade do teste em detrimento da velocidade.

    Returns:
        bool: True se o número for primo; False se não for.
    """

    if n in (2, 3):
        return True

    if n % 2 == 0 or n <= 1:
        return False

    r = 0
    d = n - 1

    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def _generate_random_odd_number(bits: int) -> int:
    return random.getrandbits(bits) | (1 << (bits - 1)) | 1
