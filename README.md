# Comunicação TCP com RSA

Esse projeto foi desenvolvido como um trabalho para a disciplina de Tópicos Avançados de Rede na Faculdade Engenheiro Salvador Arena. Trata-se de um aplicativo Python que demonstra a comunicação segura entre um servidor e um cliente TCP utilizando criptografia RSA.

## Estrutura do projeto

O projeto está organizado da seguinte forma:

```
├── rsa                     # pacote que gerencia processos de RSA
│   ├── __init__.py 
│   ├── coprimes.py         # geração de números coprimos
│   ├── cryptography.py     # criptografar/descriptografar texto usando RSA
│   ├── keys.py             # geração de chaves RSA
│   └── primes.py           # geração de números primos
├── tcp                     # pacote que gerencia a comunicação TCP
│   ├── __init__.py
│   ├── client.py           # loop do cliente TCP
│   ├── communication.py    # funções auxiliares para envio/recebimento de dados
│   └── server.py           # loop do servidor TCP
├── .gitignore
├── client.py               # ponto de entrada do cliente
└── server.py               # ponto de entrada do servidor
```

## Uso

### Execução do servidor

Para iniciar o servidor, execute o seguinte comando:

```bash
python server.py
```

Isso iniciará o servidor em `localhost` na porta `1300`. Você pode ajustar o host, a porta e outros parâmetros na função `server_loop` (no arquivo de entrada `server.py`), se necessário.

Após isso, aguarde a abertura do servidor, que será indicada por uma mensagem que segue o modelo abaixo:

```
TCP server started at localhost:1300.
```

### Execute o cliente

Para iniciar o cliente, execute o seguinte comando:

```
python client.py
```

Isso conectará o cliente ao servidor em `localhost` na porta `1300`. Se o host ou a porta forem alterados, é necessário que se adapte o código do cliente também.

## Requisitos

Certifique-se de ter o Python 3.11+ instalado. O projeto não utiliza dependências externas, baseando-se nas bibliotecas padrão do Python.