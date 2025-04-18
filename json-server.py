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
        response_body = ""
        url = self.parse_url(self.path)

        if url["requested_resource"] == "metals":
            if url["pk"] != 0:
                response_body = retrieve_metal(url['pk']) 
                return self.response(response_body, status.HTTP_200_SUCCESS.value)
            
            response_body = list_metals()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)
       
        elif url["requested_resource"] == "sizes":
            if url["pk"] != 0:
                response_body = retrieve_size(url["pk"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)
            
            response_body = list_sizes()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)
        
        elif url["requested_resource"] == "styles":
            if url["pk"] != 0:
                response_body = retrieve_style(url["pk"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)
            
            response_body = list_styles()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)
        
        elif url["requested_resource"] == "orders":
            if url["pk"] != 0:
                response_body = retrieve_order(url["pk"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)
            
            response_body = list_orders()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

        else:
            return self.response(response_body, status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

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