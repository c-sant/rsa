import pickle
import struct
from socket import socket
from typing import Any


def send_message(conn: socket, message: Any):
    """Converte mensagem para bytes e envia.

    Args:
        conn (socket): Interface de conexão que enviará os dados.
        message (Any): Mensagem a ser enviada.
    """

    data = pickle.dumps(message)
    data_length = struct.pack("!I", len(data))

    conn.sendall(data_length)
    conn.sendall(data)


def receive_message(conn: socket, bufsize: int) -> Any:
    """Recebe mensagem e converte para string.

    Args:
        conn (socket): Interface de conexão que receberá os dados.
        bufsize (int): Quantidade máxima de dados.

    Returns:
        Any: A mensagem recebida e estruturada.
    """

    data_length = conn.recv(4)
    if not data_length:
        return None

    data_length = struct.unpack("!I", data_length)[0]

    received_data = b""

    while len(received_data) < data_length:
        chunk = conn.recv(min(bufsize, data_length - len(received_data)))
        if not chunk:
            raise ConnectionError("Connection lost during message reception")

        received_data += chunk

    return pickle.loads(received_data)
