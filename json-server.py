import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status

from views import list_metals, retrieve_metal
from views import list_sizes, retrieve_size
from views import list_styles, retrieve_style
from views import list_orders, retrieve_order

class JSONServer(HandleRequests):
    """Server class to handle incoming HTTP requests for kneel diamonds"""

    def do_GET(self):
        """Method to handle GET requests from a client"""
        pass

    def do_PUT(self):
        """Method to handle PUT requests from a client"""
        pass

    def do_POST(self):
        """Method to handle POST requests from a client"""
        pass

    def do_DELETE(self):
        """Method to handle DELETE requests from a client"""

def main():
    host = ''
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()

if __name__ == "__main__":
    main()