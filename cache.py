import socket
from urllib.request import Request, urlopen, HTTPError
import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('port', help='enter port number')
    args = parser.parse_args()

    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = int(args.port)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))

    server_socket.listen(1)

    print(f'Server is listening on port {SERVER_PORT}')

    while True:
        client_connection, client_address = server_socket.accept()

        request = (client_connection.recv(1024)).decode()
        print(request)

        headers = request.split('\n')
        top_header = headers[0].split()
        method = top_header[0]
        filename = top_header[1]

        if filename == '/':
            filename = '/index.html'

        content = fetch_file(filename)

        if content:
            response = 'HTTP/1.0 200 OK\n\n' + content
        else:
            response = 'HTTP/1.0 404 NOT FOUND\n\n File not found'

        client_connection.sendall(response.encode())
        client_connection.close()

    server_socket.close()


def fetch_file(filename):

    cached_file = fetch_cached_file(filename)

    if cached_file:
        print('Fetched from cache memory')
        return cached_file

    else:
        print('Fetching from server...')
        server_file = fetch_server_file(filename)

        if server_file:
            save_to_cache(filename, server_file)
            return server_file

        else:
            return None


def fetch_cached_file(filename):

    try:
        find = open('cache' + filename, 'r')
        content = find.read()

        find.close()
        return content

    except IOError:
        return None


def fetch_server_file(filename):

    url = 'http://127.0.0.1:8000' + filename
    query = Request(url)

    try:
        response = urlopen(query)
        content = response.read().decode('utf-8')
        return content

    except HTTPError:
        return None


def save_to_cache(filename, content):

    file1 = open('Cache' + filename, 'w')
    file1.write(content)
    file1.close()


if __name__ == '__main__':
    main()
