# Python HTTP Cache Proxy Server

This project implements a HTTP proxy server that listens for client requests, fetches files from either a local cache or a remote server, and returns the response to the client. It can handle multiple client requests and is useful for caching frequently requested resources.

## Features

- Listens for HTTP client requests on a specified port using sockets
- Fetches requested files from a local cache or a remote server.
- Caches files locally to optimize future requests.
- Returns `404 NOT FOUND` for non-existent files.

## Requirements

- Python 3.x
- Access to a localhost server running at `127.0.0.1:8000` for testing remote file fetches.

## Usage

1. Clone this repository to your local machine.
2. Ensure that a server (e.g., Python’s simple HTTP server) is running on `127.0.0.1:8000` to serve test files.

3. Run the proxy server on a specified port:
   ```bash
   python cache.py 8080
   ```

Project Requirements - https://roadmap.sh/projects/caching-server
