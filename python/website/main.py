import sys

from wsgiref.simple_server import make_server

from python.website.hello import say_hello


def hello_app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])

    return [
        b'<html><strong>',
        say_hello().encode(),
        b'</strong></html>',
    ]

def main(port):
    with make_server('', port, hello_app) as httpd:
        print(f"Serving HTTP on port {port}...")

        # Respond to requests until process is killed
        httpd.serve_forever()


if __name__ == '__main__':
    main(port=int(sys.argv[1]))
