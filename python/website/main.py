import sys

from wsgiref.simple_server import make_server

from python.website.hello import say_hello


def hello_app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])

    return [
        '<html><strong>',
        say_hello(),
        '</strong></html>',
    ]


def main(port):
    server = make_server('localhost', port, hello_app)
    server.serve_forever()


if __name__ == '__main__':
    main(int(sys.argv[1]))
