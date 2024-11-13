# Caching Proxy Server

This project is a simple, foundational HTTP caching proxy server implemented in Python. It provides basic caching functionality, storing HTTP responses to optimize response times for repeated requests, and reducing the load on target servers.

## Features

### In-Memory Caching
- The server uses the local filesystem to store cached responses for requested files. This approach allows for fast retrievals on subsequent requests for the same file, enhancing efficiency by avoiding redundant fetches from the target server.

### Proxy Functionality
- The proxy server forwards client requests to a target server (default: `127.0.0.1:8000`) and caches the responses locally. If the same request is made again, the proxy returns the cached response, saving both time and resources.

### Simple, Minimalist Design
- This implementation is lightweight and suitable for demonstration or testing purposes. It is not intended for production use without additional improvements, such as enhanced security and error handling.

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
4. Making Requests
   - go to your browser and enter:
   ```browser
   http://localhost:8080/index.html
   ```

## Limitations

### Memory Usage
- Cached files are stored on the local filesystem and are only limited by available disk space. For large datasets or high traffic, consider implementing a more sophisticated caching mechanism or storing the cache in a database.

### No Cache Eviction Policy
- This server does not implement a cache eviction policy. Cached files will persist until manually cleared, which could lead to increased storage usage over time. Adding an eviction policy like Least Recently Used (LRU) would be a recommended improvement.

## Conclusion
This project serves as a basic example of a caching proxy server. While it is minimalistic, it demonstrates core caching principles and proxy functionality, serving as a solid foundation for building more complex and production-ready caching solutions.  

Project Requirements - https://roadmap.sh/projects/caching-server
