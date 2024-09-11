from .keys import generate_keys


def encrypt(message: str, e: int, n: int) -> list[int]:
    """Criptografa uma mensagem utilizando RSA.

    Converte caracteres em números inteiros de acordo com a tabela ASCII e aplica
    o método RSA de criptografia.

    Args:
        message (str): Mensagem que será criptografada.
        e (int): Expoente público.
        n (int): Módulo.

    Returns:
        list[int]: Mensagem criptografada.
    """

    return [pow(ord(c), e, n) for c in message]


def decrypt(message: list[int], d: int, n: int) -> str:
    """Descriptografa uma mensagem utilizando RSA.

    Args:
        message (list[int]): Mensagem criptografada por RSA.
        d (int): Expoente privado.
        n (int): Módulo.

    Returns:
        str: Mensagem descriptografada.
    """

    return "".join([chr(pow(c, d, n)) for c in message])
