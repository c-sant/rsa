import time
from socket import AF_INET, SOCK_STREAM, socket

import rsa

from .communication import receive_message, send_message


def client_loop(
    host: str = "localhost",
    port: int = 1300,
    bufsize: int = 4096,
    max_retries: int = 2,
    retry_cooldown: int = 2,
) -> socket:
    """Inicia uma conexão do cliente com o servidor.

    Args:
        host (str, optional): Endereço do servidor.
        port (int, optional): Porta aberta do servidor.
        bufsize (int, optional): Tamanho máximo de mensagem em bits.
        max_retries (int, optional): Número máximo de tentativas de conexão.
        retry_cooldown (int, optional): Tempo em segundos a esperar entre cada tentativa
        de conexão.
    """

    address = (host, port)
    retry_count = 0

    while retry_count <= max_retries:
        try:
            with socket(AF_INET, SOCK_STREAM) as client:
                client.connect(address)

                e, n = receive_message(client, bufsize)

                while True:
                    message = input("> user: ")
                    message = rsa.encrypt(message, e, n)
                    send_message(client, message)
                    response = rsa.decrypt(receive_message(client, bufsize), e, n)

                    print(f"> server: {response}")

        except (ConnectionRefusedError, TimeoutError):
            if retry_count >= max_retries:
                raise

            retry_count += 1
            print(
                f"Connection failed ({retry_count}), trying again in {retry_cooldown} seconds..."
            )
            time.sleep(retry_cooldown)
