import threading
import http.server
import socketserver
import configparser
from urllib.parse import urlparse, urljoin
import os
class RedirectHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = self.path[1:]  # Remove the leading slash from the requested path
        parsed_url = urlparse(parsed_path)
        normalized_path = parsed_url.path.rstrip('/') 
        
        
        for redirect_config in RedirectHandler.redirect_configs:
            config_path = redirect_config['path']
            config_url = redirect_config['url']

            if normalized_path.lower().startswith(config_path.lower()):
                target_path = normalized_path[len(config_path):]
                print(config_url)
                print(target_path)
                target_url = urljoin(config_url, target_path.lstrip('/'))
                print(target_url)
                self.send_response(302)
                self.send_header('Location', target_url)
                self.end_headers()
                return
        
        self.send_response(404)
        self.end_headers()
        self.wfile.write(b'404 Not Found')

def run_server():
    port = int(os.environ.get('PORT', 80)) 
    handler = RedirectHandler

    with socketserver.TCPServer(("", port), handler) as httpd:
        print("Server running on port", port)
        httpd.serve_forever()

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')  # Replace 'config.ini' with the actual path to your config file

    RedirectHandler.redirect_configs = []
    for section in config.sections():
        if section == 'Redirect':
            path = config.get(section, 'path')
            url = config.get(section, 'url')
            redirect_config = {'path': path, 'url': url}
            RedirectHandler.redirect_configs.append(redirect_config)

if __name__ == "__main__":
    read_config()

    server_thread = threading.Thread(target=run_server)
    server_thread.start()
