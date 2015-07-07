import cherrypy


class HelloWorld(object):

    def index(self):
        return "Hello World!"
    index.exposed = True

cherrypy.config.update(
    {'server.socket_host': '127.0.0.1', 'server.socket_port': 5555}
)

cherrypy.quickstart(HelloWorld())
