from .coprimes import generate_coprime
from .primes import generate_prime


def generate_keys(bits: int = 1024) -> tuple[int, int, int]:
    """Gera chaves RSA do tamanho especificado.

    Args:
        bits (int): O tamanho esperado para as chaves RSA.

    Returns:
        tuple[int, int, int]: Os valores utilizados para encriptação, decriptação
        e operação módulo, respectivamente.
    """

    # chaves p e q devem usar metade dos bits para que o resultado de d e e tenha
    # o tamanho esperado (e.g. para chaves de 4 bits, usam-se duas chaves de 2 bits)
    while True:
        p = generate_prime(bits // 2)
        q = generate_prime(bits // 2)

        if p != q:
            break

    n = p * q
    phi = (p - 1) * (q - 1)
    e = generate_coprime(phi, 2, phi - 1)
    d = pow(e, -1, phi)

    return e, d, n
