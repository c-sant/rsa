from socket import AF_INET, SOCK_STREAM, socket

import rsa

from .communication import receive_message, send_message


def server_loop(
    host: str = "localhost",
    port: int = 1300,
    backlog: int = 5,
    bufsize: int = 4096,
    rsa_key_length: int = 4096,
) -> socket:
    """Inicia um servidor TCP.

    Args:
        host (str, optional): O endereço IP do servidor.
        port (int, optional): A porta do servidor.
        backlog (int, optional): Número máximo de requisições por conexão.
        bufsize (int, optional): Tamanho máximo de mensagem em bits.
    """

    e, d, n = rsa.generate_keys(rsa_key_length)

    address = (host, port)

    with socket(AF_INET, SOCK_STREAM) as server:
        server.bind(address)
        server.listen(backlog)

        print(f"TCP server started at {host}:{port}.")

        conn, _ = server.accept()

        print("Connection estabilished.")

        with conn:
            send_message(conn, (e, n))

            while True:
                message = receive_message(conn, bufsize=bufsize)

                if str(message).strip() != "":
                    message = rsa.decrypt(message, d, n)

                    print(f"> user: {message}")

                    send_message(conn, rsa.encrypt(message.upper(), d, n))

                    print("> server: Reply sent.")
